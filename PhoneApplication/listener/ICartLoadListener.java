package com.example.bip.listener;

import com.example.bip.model.CartModel;
import com.example.bip.model.GameModel;

import java.util.List;

public interface ICartLoadListener {
    void onCartLoadSuccess(List<CartModel> cartModelList);
    void onCartLoadFailed(String message);
}
