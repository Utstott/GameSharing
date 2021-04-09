package com.example.bip;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.view.View;
import android.widget.Button;

import androidx.annotation.Nullable;

public class Pop extends Activity {
    Button Damaged;
    Button EmptyBox;
    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pop);

        Damaged = (Button)findViewById(R.id.BoxDamaged);
        EmptyBox = (Button) findViewById(R.id.EmptyBox);

        Damaged.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent TakeGameIntent = new Intent(Pop.this, OtherReturnGame.class);
                startActivity(TakeGameIntent);
            }
        });
        EmptyBox.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //finish();
                Intent Regret = new Intent(Pop.this, Regret.class);
                startActivity(Regret);
            }
        });

        DisplayMetrics dm = new DisplayMetrics();
        getWindowManager().getDefaultDisplay().getMetrics(dm);

        int width = dm.widthPixels;
        int height = dm.heightPixels;

        getWindow().setLayout((int)(width*.9), (int)(height*.12));



    }
}
