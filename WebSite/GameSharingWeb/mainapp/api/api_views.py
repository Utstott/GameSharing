from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import GameCategorySerializer, GameSerializer, CustomerSerializer, CartSerializer
from .serializers import CartProductSerializer, OrderSerializer, GameBoxSerializer, BagRoomSerializer
from .serializers import EventSerializer
from ..models import GameCategory, Game, Customer, Cart, CartGame, Order, GameBox, BagRoom, Event
from rest_framework.filters import SearchFilter


class GameCategoryListAPIView(ListAPIView):
    serializer_class = GameCategorySerializer
    queryset = GameCategory.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['slug']


class GameCategoryDetailListAPIView(RetrieveAPIView):
    serializer_class = GameCategorySerializer
    queryset = GameCategory.objects.all()
    lookup_field = 'id'


class GameListAPIView(ListAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['slug', 'price', 'game_time', 'number_players']


class GameDetailListAPIView(RetrieveAPIView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    lookup_field = 'id'


class GameBoxListAPIView(ListAPIView):
    serializer_class = GameBoxSerializer
    queryset = GameBox.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['slug', 'status', 'game', 'bag_room']


class GameBoxDetailListAPIView(RetrieveAPIView):
    serializer_class = GameBoxSerializer
    queryset = GameBox.objects.all()
    lookup_field = 'id'


class CustomerListAPIView(ListAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['address', 'phone']


class CustomerDetailListAPIView(RetrieveAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'id'


class CartListAPIView(ListAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['final_price', 'total_products']


class CartDetailListAPIView(RetrieveAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    lookup_field = 'id'


class CartGameListAPIView(ListAPIView):
    serializer_class = CartProductSerializer
    queryset = CartGame.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['final_price']


class CartGameDetailListAPIView(RetrieveAPIView):
    serializer_class = CartProductSerializer
    queryset = CartGame.objects.all()
    lookup_field = 'id'


class OrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['']


class OrderDetailListAPIView(RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'id'


class BagRoomListAPIView(ListAPIView):
    serializer_class = BagRoomSerializer
    queryset = BagRoom.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['']


class BagRoomDetailListAPIView(RetrieveAPIView):
    serializer_class = BagRoomSerializer
    queryset = BagRoom.objects.all()
    lookup_field = 'id'


class EventListAPIView(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['']


class EventDetailListAPIView(RetrieveAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    lookup_field = 'id'

