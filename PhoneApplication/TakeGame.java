package com.example.bip;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Bitmap;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;

import java.lang.String;
import java.math.BigInteger;
import java.util.Random;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.MultiFormatWriter;
import com.google.zxing.common.BitMatrix;
import com.journeyapps.barcodescanner.BarcodeEncoder;

public class TakeGame extends AppCompatActivity {

    ImageButton UserLogo;
    ImageView QR;
    Button Bad;
    Button Good;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_take_game);

        UserLogo = (ImageButton) findViewById(R.id.user7);
        QR = (ImageView) findViewById(R.id.QR);
        Bad = (Button) findViewById(R.id.NotOk);
        Good = (Button) findViewById(R.id.Ok);

        MultiFormatWriter multiFormatWriter = new MultiFormatWriter();

        try {
            //BigInteger randomNum = ThreadLocalRandom.current().nextLong(2^255, 2^256 + 1);
            //BigInteger bigInteger = new BigInteger(ThreadLocalRandom.current().nextLong(2^255, 2^256 + 1));
            BigInteger maxLimit = new BigInteger("115792089237316195423570985008687907853269984665640564039457584007913129639936");
            BigInteger minLimit = new BigInteger("57896044618658097711785492504343953926634992332820282019728792003956564819968");
            BigInteger bigInteger = maxLimit.subtract(minLimit);
            Random randNum = new Random();
            int len = maxLimit.bitLength();
            BigInteger res = new BigInteger(len, randNum);
            if (res.compareTo(minLimit) < 0)
                res = res.add(minLimit);
            if (res.compareTo(bigInteger) >= 0)
                res = res.mod(bigInteger).add(minLimit);

            BitMatrix bitMatrix = multiFormatWriter.encode(String.valueOf(res), BarcodeFormat.QR_CODE, 500, 500);
            BarcodeEncoder barcodeEncoder = new BarcodeEncoder();
            Bitmap bitmap = barcodeEncoder.createBitmap(bitMatrix);
            QR.setImageBitmap(bitmap);


        }catch (Exception e){
            e.printStackTrace();
        }

        UserLogo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent TakeGameIntent = new Intent(TakeGame.this, Personal_Cabin.class);
                startActivity(TakeGameIntent);

            }
        });
        Good.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent OkIntent = new Intent(TakeGame.this, Order.class);
                startActivity(OkIntent);
            }
        });
        Bad.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(TakeGame.this, Pop.class));
            }
        });

    }


}