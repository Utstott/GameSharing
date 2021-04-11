package com.example.bip.listener;

import com.example.bip.model.GameModel;

import java.util.List;

public interface IGameLoadListener {
    void onGameLoadSuccess(List<GameModel> gameModelList);
    void onGameLoadFailed(String message);
}
