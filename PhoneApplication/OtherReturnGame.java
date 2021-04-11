package com.example.bip;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.Manifest;
import android.content.ContentValues;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.provider.MediaStore;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.Toast;

public class OtherReturnGame extends AppCompatActivity {
    private static final int PERMISSION_CODE = 1000;
    private static final int IMAGE_CAPTURE_CODE = 1001;
    ImageButton UserLogo;
    Button btnCamera;
    ImageView photo;
    Uri imageUri;
    Button otherPlace;
    Button remove;
    ImageView catalog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_other_return_game);

        UserLogo = (ImageButton) findViewById(R.id.user7);
        btnCamera = (Button) findViewById(R.id.Camera2);
        photo = (ImageView) findViewById(R.id.photo2);
        otherPlace = (Button) findViewById(R.id.btn2);
        remove = (Button) findViewById(R.id.btn3);
        catalog = (ImageView) findViewById(R.id.cartButton);

        UserLogo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent TakeGameIntent = new Intent(OtherReturnGame.this, Personal_Cabin.class);
                startActivity(TakeGameIntent);

            }
        });
        otherPlace.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent searchPlace = new Intent(OtherReturnGame.this, ShopActivity.class);
                startActivity(searchPlace);
            }
        });
        remove.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent remFromOrder = new Intent(OtherReturnGame.this, Order.class);
                startActivity(remFromOrder);
            }
        });
        catalog.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(OtherReturnGame.this, OrderCart.class));
            }
        });
        btnCamera.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M){
                    if(checkSelfPermission(Manifest.permission.CAMERA)==
                            PackageManager.PERMISSION_DENIED ||
                            checkSelfPermission(Manifest.permission.WRITE_EXTERNAL_STORAGE)==
                                    PackageManager.PERMISSION_DENIED){
                        String[] permission = {Manifest.permission.CAMERA, Manifest.permission.WRITE_EXTERNAL_STORAGE};
                        requestPermissions(permission, PERMISSION_CODE);
                    }
                    else{
                        //you already have permissions
                        openCamera();
                    }

                }
                else{
                    //old version
                    openCamera();
                }
//                try {
//                    Intent intent = new Intent();
//                    intent.setAction(MediaStore.ACTION_IMAGE_CAPTURE);
//                    startActivity(intent);
//
//                } catch (Exception e) {
//                    e.printStackTrace();
//                }

            }
        });

    }

    private void openCamera() {
        ContentValues values = new ContentValues();
        values.put(MediaStore.Images.Media.TITLE, "New Picture");
        values.put(MediaStore.Images.Media.DESCRIPTION, "From the Camera");
        imageUri = getContentResolver().insert(MediaStore.Images.Media.EXTERNAL_CONTENT_URI, values);
        Intent cameraIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        cameraIntent.putExtra(MediaStore.EXTRA_OUTPUT, imageUri);
        startActivityForResult(cameraIntent, IMAGE_CAPTURE_CODE);
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        switch (requestCode){
            case PERMISSION_CODE:{
                if(grantResults.length > 0 && grantResults[0]==
                        PackageManager.PERMISSION_GRANTED){
                    openCamera();
                }
                else {
                    Toast.makeText(this, "Permission denied", Toast.LENGTH_SHORT).show();
                }
            }
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (resultCode == RESULT_OK) {
            photo.setImageURI(imageUri);
        }

    }
}