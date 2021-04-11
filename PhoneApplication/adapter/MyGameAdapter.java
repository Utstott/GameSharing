package com.example.bip.adapter;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.example.bip.R;
import com.example.bip.eventbus.MyUpdateCartEvent;
import com.example.bip.listener.ICartLoadListener;
import com.example.bip.listener.IRecyclerViewClickListener;
import com.example.bip.model.CartModel;
import com.example.bip.model.GameModel;
import com.google.android.gms.tasks.OnFailureListener;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import org.greenrobot.eventbus.EventBus;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.Unbinder;

public class MyGameAdapter extends RecyclerView.Adapter<MyGameAdapter.MyGameViewHolder> {
    ImageView Info;
    private Context context;
    private List<GameModel> gameModelList;
    private ICartLoadListener iCartLoadListener;

    public MyGameAdapter(Context context, List<GameModel> gameModelList, ICartLoadListener iCartLoadListener) {
        this.context = context;
        this.gameModelList = gameModelList;
        this.iCartLoadListener = iCartLoadListener;
    }


    @NonNull
    @Override
    public MyGameViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        return new MyGameViewHolder(LayoutInflater.from(context)
                .inflate(R.layout.layout_game_item,parent,false));
    }

    @Override
    public void onBindViewHolder(@NonNull MyGameViewHolder holder, int position) {
        Glide.with(context)
                .load(gameModelList.get(position).getImage())
                .into(holder.imageView);
        holder.txtPrice.setText(new StringBuilder("$").append(gameModelList.get(position).getPrice()));
        holder.txtName.setText(new StringBuilder().append(gameModelList.get(position).getName()));
        holder.setListener((view,adapterPosition)-> {
            addToCart(gameModelList.get(position));
        });
    }

    private void addToCart(GameModel gameModel) {
        DatabaseReference userCart= FirebaseDatabase
                .getInstance()
                .getReference("Cart")
                .child("UNIQUE_USER_ID");

        userCart.child(gameModel.getKey())
                .addListenerForSingleValueEvent(new ValueEventListener() {
                    @Override
                    public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                        if(dataSnapshot.exists())
                        {
                            CartModel cartModel=dataSnapshot.getValue(CartModel.class);
                            cartModel.setQuantity(cartModel.getQuantity()+1);
                            Map<String,Object> updateData=new HashMap<>();
                            updateData.put("quantity",cartModel.getQuantity());
                            updateData.put("totalPrice",cartModel.getQuantity()*Float.parseFloat(cartModel.getPrice()));
                            updateData.put("descr", cartModel.getDescr());

                            userCart.child(gameModel.getKey())
                                    .updateChildren(updateData)
                                    .addOnSuccessListener(aVoid -> {
                                        iCartLoadListener.onCartLoadFailed("Add To Cart Success");
                                    })
                                    .addOnFailureListener(e -> iCartLoadListener.onCartLoadFailed(e.getMessage()));
                        }
                        else
                        {
                            CartModel cartModel= new CartModel();
                            cartModel.setName(gameModel.getName());
                            cartModel.setImage(gameModel.getImage());
                            cartModel.setKey(gameModel.getKey());
                            cartModel.setPrice(gameModel.getPrice());
                            cartModel.setDescr(gameModel.getDescr());
                            cartModel.setQuantity(1);
                            cartModel.setTotalPrice(Float.parseFloat(gameModel.getPrice()));

                            userCart.child(gameModel.getKey())
                                    .setValue(cartModel)
                                    .addOnSuccessListener(aVoid -> {
                                        iCartLoadListener.onCartLoadFailed("Add To Cart Success");
                                    })
                                    .addOnFailureListener(e -> iCartLoadListener.onCartLoadFailed(e.getMessage()));
                        }
                        EventBus.getDefault().postSticky(new MyUpdateCartEvent());
                    }

                    @Override
                    public void onCancelled(@NonNull DatabaseError databaseError) {
                        iCartLoadListener.onCartLoadFailed(databaseError.getMessage());
                    }
                });
    }

    @Override
    public int getItemCount() {
        return gameModelList.size();
    }

    public class MyGameViewHolder extends RecyclerView.ViewHolder implements View.OnClickListener {
        @BindView(R.id.imageView)
        ImageView imageView;
        @BindView(R.id.txtName)
        TextView txtName;
        @BindView(R.id.txtPrice)
        TextView txtPrice;

        IRecyclerViewClickListener listener;

        public void setListener(IRecyclerViewClickListener listener) {
            this.listener = listener;
        }

        private Unbinder unbinder;
        public MyGameViewHolder(@NonNull View itemView) {
            super(itemView);
            unbinder= ButterKnife.bind(this,itemView);
            itemView.setOnClickListener(this);
        }

        @Override
        public void onClick(View v) {
            listener.onRecyclerClick(v,getAdapterPosition());
        }
    }
}
