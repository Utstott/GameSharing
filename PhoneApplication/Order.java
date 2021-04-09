package com.example.bip;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class Order extends AppCompatActivity {
    Button Return;
    Button Take;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_order);

        Return = (Button) findViewById(R.id.btn_return);
        Take = (Button) findViewById(R.id.btn_take);

        Return.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent ReturnGameIntent = new Intent(Order.this, selectPlacePop.class);
                startActivity(ReturnGameIntent);
            }
        });
        Take.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent TakeGameIntent = new Intent(Order.this, TakeGame.class);
                startActivity(TakeGameIntent);
            }
        });
    }
}