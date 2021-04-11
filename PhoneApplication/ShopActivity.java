package com.example.bip;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.media.Image;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.bumptech.glide.Glide;
import com.google.android.material.snackbar.Snackbar;

import org.w3c.dom.Text;

public class ShopActivity extends AppCompatActivity {
    Button mButtonTakeGame;
    Button mButtonOrder;
    ImageButton UserLogo;
    ImageView Image;
    TextView Description;
    TextView GameName;
    ImageView catalog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_shop);

        Image = (ImageView) findViewById(R.id.imageView2);
        Description = (TextView) findViewById(R.id.GameDescription);
        GameName = (TextView) findViewById(R.id.GameName);
        catalog = (ImageView) findViewById(R.id.cartButton);

        if (getIntent().hasExtra("name")) {
            Intent intent = new Intent();
            Glide.with(this)
                    //.load(intent.getExtras().getString("image"))
                    .load(getIntent().getStringExtra("image"))
                    .into(Image);

//            Glide.with(this)
//                    //.load(intent.getExtras().getString("image"))
//                    .load(getIntent().getStringExtra("descr"))
//                    .into(Description);
            Description.setText(new StringBuilder().append(getIntent().getStringExtra("descr")));
            GameName.setText(new StringBuilder().append(getIntent().getStringExtra("name")));

            //Toast.makeText(ShopActivity.this,"YEAP",Toast.LENGTH_SHORT).show();
        }
        else
        {
            Toast.makeText(ShopActivity.this,"NOPE",Toast.LENGTH_SHORT).show();
        }

        mButtonTakeGame = (Button) findViewById(R.id.TakeGameButton);
        mButtonOrder = (Button) findViewById(R.id.Order);
        UserLogo = (ImageButton) findViewById(R.id.user7);

        Button btn = (Button) findViewById(R.id.FindGameButton);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                EditText GameName = (EditText) findViewById(R.id.FindGameTextBox);
                String GameNameString = GameName.getText().toString();

                TextView textView = (TextView) findViewById(R.id.GameName);
                textView.setText(GameNameString);
            }
        });

        mButtonTakeGame.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                    Intent TakeGameIntent = new Intent(ShopActivity.this,PopPlaceForCart.class);
                    startActivity(TakeGameIntent);

            }
        });
        mButtonOrder.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent TakeGameIntent = new Intent(ShopActivity.this,Order.class);
                startActivity(TakeGameIntent);
            }
        });
        UserLogo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent TakeGameIntent = new Intent(ShopActivity.this, Personal_Cabin.class);
                startActivity(TakeGameIntent);

            }
        });
        catalog.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(ShopActivity.this, OrderCart.class));
            }
        });


    }
}
