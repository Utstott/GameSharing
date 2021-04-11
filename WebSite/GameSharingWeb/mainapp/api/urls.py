from django.urls import path

from .api_views import (
    GameCategoryListAPIView,
    GameListAPIView,
    CustomerListAPIView,
    CartListAPIView,
    CartGameListAPIView,
    OrderListAPIView,
    GameBoxListAPIView,
    BagRoomListAPIView,
    EventListAPIView
)
from .api_views import (
    GameCategoryDetailListAPIView,
    GameDetailListAPIView,
    GameBoxDetailListAPIView,
    CustomerDetailListAPIView,
    CartDetailListAPIView,
    CartGameDetailListAPIView,
    OrderDetailListAPIView,
    BagRoomDetailListAPIView,
    EventDetailListAPIView
)

urlpatterns = [
    path('gamecategories/', GameCategoryListAPIView.as_view(), name='gamecategories'),
    path('gamecategories/<str:id>/', GameCategoryDetailListAPIView.as_view(), name='gamecategories_detail'),
    path('games/', GameListAPIView.as_view(), name='games'),
    path('games/<str:id>/', GameDetailListAPIView.as_view(), name='games_detail'),
    path('customer/', CustomerListAPIView.as_view(), name='customer'),
    path('customer/<str:id>/', CustomerDetailListAPIView.as_view(), name='customer'),
    path('cart/', CartListAPIView.as_view(), name='cart'),
    path('cart/<str:id>/', CartDetailListAPIView.as_view(), name='cart'),
    path('cartproduct/', CartGameListAPIView.as_view(), name='cartproduct'),
    path('cartproduct/<str:id>/', CartGameDetailListAPIView.as_view(), name='cartproduct'),
    path('order/', OrderListAPIView.as_view(), name='order'),
    path('order/<str:id>/', OrderDetailListAPIView.as_view(), name='order'),
    path('gamebox/', GameBoxListAPIView.as_view(), name='gamebox'),
    path('gamebox/<str:id>/', GameBoxDetailListAPIView.as_view(), name='gamebox_detail'),
    path('bagroom/', BagRoomListAPIView.as_view(), name='bagroom'),
    path('bagroom/<str:id>/', BagRoomDetailListAPIView.as_view(), name='bagroom'),
    path('event/', EventListAPIView.as_view(), name='event'),
    path('event/<str:id>/', EventDetailListAPIView.as_view(), name='event')

]