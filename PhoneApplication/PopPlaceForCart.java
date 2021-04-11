package com.example.bip;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.annotation.Nullable;

public class PopPlaceForCart extends Activity {
    TextView text;
    TextView text2;
    TextView text3;
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_select_place_pop);

        text = (TextView) findViewById(R.id.textView7);
        text2 = (TextView) findViewById(R.id.textView8);
        text3 = (TextView) findViewById(R.id.textView9);

        text.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent RetGameIntent = new Intent(PopPlaceForCart.this, CartActivity.class);
                startActivity(RetGameIntent);
            }
        });
        text2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent RetGameIntent = new Intent(PopPlaceForCart.this, CartActivity.class);
                startActivity(RetGameIntent);
            }
        });
        text3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent RetGameIntent = new Intent(PopPlaceForCart.this, CartActivity.class);
                startActivity(RetGameIntent);
            }
        });


        DisplayMetrics dm = new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(dm);

        int width = dm.widthPixels;
        int height = dm.heightPixels;

        getWindow().setLayout((int)(width*.6), (int)(height*.2));



    }
}
