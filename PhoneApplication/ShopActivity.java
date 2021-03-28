package com.example.loginscreen;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class ShopActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_shop);

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
    }
}
