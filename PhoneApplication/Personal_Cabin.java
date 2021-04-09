package com.example.bip;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class Personal_Cabin extends AppCompatActivity {

    DatabaseHelper db;
    EditText mTextUsername;
    EditText mTextEmail;
    EditText mTextPhone;
    Button mButtonChange;
    Button mButtonExit;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_personal__cabin);

        db = new DatabaseHelper(this);
        mTextUsername = (EditText)findViewById(R.id.edittext_username_l);
        mTextEmail = (EditText)findViewById(R.id.edittext_email_l);
        mTextPhone= (EditText)findViewById(R.id.edittext_phone_l);
        mButtonChange = (Button)findViewById(R.id.button_accept_change);
        mButtonExit = (Button)findViewById(R.id.button_exit);
        mButtonChange.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String user = mTextUsername.getText().toString().trim();
                String email = mTextEmail.getText().toString().trim();
                String phone = mTextPhone.getText().toString().trim();
                Boolean res = db.checkChange(user,email,phone);
                if(res == true)
                {
                    Toast.makeText(Personal_Cabin.this,"Changes Saves",Toast.LENGTH_SHORT).show();
                }
                else
                {
                    Toast.makeText(Personal_Cabin.this,"Change Error",Toast.LENGTH_SHORT).show();
                }
            }
        });
        mButtonExit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent ExitIntent = new Intent(Personal_Cabin.this,MainActivity.class);
                startActivity(ExitIntent);
            }
        });
    }
}