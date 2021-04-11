package com.example.bip;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.os.Bundle;
import android.widget.FrameLayout;
import android.widget.ImageButton;
import android.widget.RelativeLayout;

import com.example.bip.adapter.MyGameAdapter;
import com.example.bip.eventbus.MyUpdateCartEvent;
import com.example.bip.listener.ICartLoadListener;
import com.example.bip.listener.IGameLoadListener;
import com.example.bip.model.CartModel;
import com.example.bip.model.GameModel;
import com.example.bip.utils.SpaceItemDecoration;
import com.google.android.material.snackbar.Snackbar;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.nex3z.notificationbadge.NotificationBadge;

import org.greenrobot.eventbus.EventBus;
import org.greenrobot.eventbus.Subscribe;
import org.greenrobot.eventbus.ThreadMode;

import java.util.ArrayList;
import java.util.List;

import butterknife.BindView;
import butterknife.ButterKnife;

public class OrderCart extends AppCompatActivity implements IGameLoadListener, ICartLoadListener {
    @BindView(R.id.recycler_drink)
    RecyclerView recyclerDrink;
    @BindView(R.id.ordercart)
    RelativeLayout ordercart;
    @BindView(R.id.badge)
    NotificationBadge badge;
    @BindView(R.id.btnCart)
    FrameLayout btnCart;
    @BindView(R.id.user7)
    ImageButton userLogo;

    IGameLoadListener gameLoadListener;
    ICartLoadListener cartLoadListener;

    @Override
    protected void onStart() {
        super.onStart();
        EventBus.getDefault().register(this);
    }

    @Override
    protected void onStop() {
        if(EventBus.getDefault().hasSubscriberForEvent(MyUpdateCartEvent.class))
            EventBus.getDefault().removeStickyEvent(MyUpdateCartEvent.class);
        EventBus.getDefault().unregister(this);
        super.onStop();
    }

    @Subscribe(threadMode = ThreadMode.MAIN,sticky = true)
    public void onUpdateCart(MyUpdateCartEvent event)
    {
        countCartItem();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_order_cart);

        init();
        loadGameFromFirebase();
        countCartItem();
    }

    private void loadGameFromFirebase() {
        List<GameModel> gameModels = new ArrayList<>();
        FirebaseDatabase.getInstance()
                .getReference("Drink")
                .addListenerForSingleValueEvent(new ValueEventListener() {
                    @Override
                    public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                        if(dataSnapshot.exists())
                        {
                            for(DataSnapshot gameSnapshot:dataSnapshot.getChildren())
                            {
                                GameModel gameModel=gameSnapshot.getValue(GameModel.class);
                                gameModel.setKey(gameSnapshot.getKey());
                                gameModels.add(gameModel);
                            }
                            gameLoadListener.onGameLoadSuccess(gameModels);
                        }
                        else
                        {
                            gameLoadListener.onGameLoadFailed("Can't find Game");
                        }
                    }

                    @Override
                    public void onCancelled(@NonNull DatabaseError databaseError) {
                        gameLoadListener.onGameLoadFailed(databaseError.getMessage());
                    }
                });
    }

    private void init() {
        ButterKnife.bind(this);

        gameLoadListener=this;
        cartLoadListener=this;

        GridLayoutManager gridLayoutManager=new GridLayoutManager(this,2);
        recyclerDrink.setLayoutManager(gridLayoutManager);
        recyclerDrink.addItemDecoration(new SpaceItemDecoration());
        userLogo.setOnClickListener(v->startActivity(new Intent(this,Personal_Cabin.class)));
        btnCart.setOnClickListener(v->startActivity(new Intent(this,CartActivity.class)));
        //recyclerDrink.setOnClickListener(v->startActivity(new Intent(this,ShopActivity.class)));
    }

    @Override
    public void onGameLoadSuccess(List<GameModel> gameModelList) {
        MyGameAdapter adapter = new MyGameAdapter(this,gameModelList,cartLoadListener);
        recyclerDrink.setAdapter(adapter);
    }

    @Override
    public void onGameLoadFailed(String message) {
        Snackbar.make(ordercart,message,Snackbar.LENGTH_LONG).show();
    }

    @Override
    public void onCartLoadSuccess(List<CartModel> cartModelList) {
        int cartSum=0;
        for(CartModel cartModel:cartModelList)
        {
            cartSum+=cartModel.getQuantity();
        }
        badge.setNumber(cartSum);
    }

    @Override
    public void onCartLoadFailed(String message) {
        Snackbar.make(ordercart,message,Snackbar.LENGTH_LONG).show();
    }

    @Override
    protected void onResume() {
        super.onResume();
        countCartItem();
    }

    private void countCartItem() {
        List<CartModel> cartModels=new ArrayList<>();
        FirebaseDatabase
                .getInstance().getReference("Cart")
                .child("UNIQUE_USER_ID")
                .addListenerForSingleValueEvent(new ValueEventListener() {
                    @Override
                    public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                        for(DataSnapshot cartSnapshot:dataSnapshot.getChildren())
                        {
                            CartModel cartModel=cartSnapshot.getValue(CartModel.class);
                            cartModel.setKey(cartSnapshot.getKey());
                            cartModels.add(cartModel);
                        }
                        cartLoadListener.onCartLoadSuccess(cartModels);
                    }

                    @Override
                    public void onCancelled(@NonNull DatabaseError databaseError) {
                        cartLoadListener.onCartLoadFailed(databaseError.getMessage());
                    }
                });
    }
}