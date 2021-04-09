package com.example.bip;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;

public class Regret extends AppCompatActivity {
    ImageButton UserLogo;
    Button OtherPlace;
    Button removeGame;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_regret);

        UserLogo = (ImageButton) findViewById(R.id.user7);
        OtherPlace = (Button) findViewById(R.id.OtherPlace);
        removeGame = (Button) findViewById(R.id.RemoveGame);

        UserLogo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent TakeGameIntent = new Intent(Regret.this, Personal_Cabin.class);
                startActivity(TakeGameIntent);

            }
        });

        OtherPlace.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent OtherPlaceIntent = new Intent(Regret.this, ShopActivity.class);
                startActivity(OtherPlaceIntent);
            }
        });

        removeGame.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent RemoveGameIntent = new Intent(Regret.this, Order.class);
                startActivity(RemoveGameIntent);
            }
        });

    }
}