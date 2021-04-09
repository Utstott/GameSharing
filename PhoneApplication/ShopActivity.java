package com.example.bip;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

public class ShopActivity extends AppCompatActivity {
    //Button mButtonTakeGame;
    Button mButtonOrder;
    ImageButton UserLogo;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_shop);

//        mButtonTakeGame = (Button) findViewById(R.id.TempTakeGame);
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

//        mButtonTakeGame.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                    Intent TakeGameIntent = new Intent(ShopActivity.this,TakeGame.class);
//                    startActivity(TakeGameIntent);
//
//            }
//        });
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


    }
}
