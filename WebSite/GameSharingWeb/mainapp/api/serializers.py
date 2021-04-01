from rest_framework import serializers
from ..models import GameCategory
from ..models import Game, GameBox, Cart, CartProduct
from ..models import Customer, Order, BagRoom, Event
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class GameCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = GameCategory
        fields = [
            'id', 'name', 'slug'
        ]


class GameSerializer(serializers.ModelSerializer):
    game_category = serializers.PrimaryKeyRelatedField(queryset=GameCategory.objects.all(), many=True)
    title = serializers.CharField(required=True)
    slug = serializers.SlugField()
    image = serializers.ImageField(required=True)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=9, decimal_places=2, required=True)
    number_players = serializers.CharField(required=True)
    rent = serializers.DecimalField(max_digits=9, decimal_places=2, required=True)
    game_time = serializers.CharField(required=True)
    game_boxes = serializers.PrimaryKeyRelatedField(queryset=GameBox.objects.all(), many=True)

    class Meta:
        model = Game
        fields = [
            'id', 'game_category', 'title', 'slug', 'image', 'description', 'price', 'number_players', 'rent', 'game_time', 'game_boxes'
        ]


class GameBoxSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=True)
    status = serializers.CharField(required=True)
    game = serializers.PrimaryKeyRelatedField(queryset=Game.objects.all(), required=False)
    bag_room = serializers.PrimaryKeyRelatedField(queryset=BagRoom.objects.all(), required=False)

    class Meta:
        model = GameBox
        fields = [
            'id', 'slug', 'status', 'game', 'bag_room'
        ]


class CustomerSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model())
    phone = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    orders = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all(), many=True)
    #

    class Meta:
        model = Customer
        fields = [
            'id', 'user', 'phone', 'address', 'orders'
        ]


class CartSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), required=False)
    products = serializers.PrimaryKeyRelatedField(queryset=CartProduct.objects.all(), many=True)
    total_products = serializers.IntegerField(default=0)
    final_price = serializers.DecimalField(max_digits=9, decimal_places=2, default=0)
    in_order = serializers.BooleanField(default=False)
    for_anonymous_user = serializers.BooleanField(default=False)

    class Meta:
        model = Cart
        fields = [
            'id', 'owner', 'products', 'total_products', 'final_price', 'in_order', 'for_anonymous_user'
        ]


class CartProductObjectRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, Game):
            serializer = GameSerializer(value)
        elif isinstance(value, Customer):
            serializer = CustomerSerializer(value)
        else:
            raise Exception('Unexpected type of tagged object')

        return serializer.data


class CartProductSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())
    content_type = serializers.PrimaryKeyRelatedField(queryset=ContentType)
    object_id = serializers.IntegerField(required=True)
    content_object = CartProductObjectRelatedField(many=False, queryset=CartProduct.objects.all())
    #content_object = GenericForeignKey('content_type', 'object_id')
    qty = serializers.IntegerField(default=1)
    final_price = serializers.DecimalField(max_digits=9, decimal_places=2, required=True)

    class Meta:
        model = CartProduct
        fields = [
            'id', 'user', 'cart', 'content_type', 'object_id', 'content_object', 'qty', 'final_price'
        ]


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    address = serializers.CharField(required=False)
    status = serializers.CharField(required=True)
    buying_type = serializers.CharField(required=True)
    comment = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=True)
    order_date = serializers.DateField(required=True)
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all(), required=False)

    class Meta:
        model = Order
        fields = [
            'id', 'customer', 'first_name', 'last_name', 'phone', 'address', 'status', 'buying_type', 'comment', 'created_at', 'order_date', 'cart'
        ]


class BagRoomSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    rent = serializers.DecimalField(max_digits=9, decimal_places=2, required=True)
    cells = serializers.DecimalField(max_digits=4, decimal_places=0, required=True)
    free_cells = serializers.DecimalField(max_digits=4, decimal_places=0, required=True)

    class Meta:
        model = BagRoom
        fields = [
            'id', 'name', 'address', 'slug', 'rent', 'cells', 'free_cells'
        ]


class EventSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=True)
    status = serializers.CharField(required=True)
    game_box = serializers.PrimaryKeyRelatedField(queryset=GameBox.objects.all(), required=False)

    class Meta:
        model = Event
        fields = [
            'id', 'slug', 'status', 'game_box'
        ]

