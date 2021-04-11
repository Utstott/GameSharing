from io import BytesIO
import sys

from PIL import Image
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse
from django.utils import timezone

User = get_user_model()


def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class MinResolutionErrorExeption(Exception):
    pass


class MaxResolutionErrorExeption(Exception):
    pass


# class Category(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Имя категории')
#     slug = models.SlugField(unique=True)
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('category_detail', kwargs={'slug': self.slug})
#
#
# class Product(models.Model):
#     MIN_RESOLUTION = (400, 400)
#     MAX_RESOLUTION = (1000, 1000)
#     MAX_IMAGE_SIZE = 3145728
#
#     class Meta:
#         abstract = True
#
#     category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
#     title = models.CharField(max_length=255, verbose_name='Наименование')
#     slug = models.SlugField(unique=True)
#     image = models.ImageField(verbose_name='Изображение')
#     description = models.TextField(verbose_name='Описание', null=True)
#     price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
#
#     def __str__(self):
#         return self.title
#
#     def get_model_name(self):
#         return self.__class__.__name__.lower()
#
#     def save(self, *args, **kwargs):
#         # image=self.image
#         # img = Image.open(image)
#         # min_height, min_width = self.MIN_RESOLUTION
#         # max_height, max_width = self.MAX_RESOLUTION
#         # if img.height < min_height or img.width < min_width:
#         #     raise MinResolutionErrorExeption('Разрешение изображения меньше минимального!')
#         # if img.height > max_height or img.width > max_width:
#         #     raise MaxResolutionErrorExeption('Разрешение изображения больше максимального!')
#
#         image = self.image
#         img = Image.open(image)
#         new_img = img.convert('RGB')
#         resize_new_img = new_img.resize((200, 200), Image.ANTIALIAS)
#         filestream = BytesIO()
#         resize_new_img.save(filestream, 'JPEG', quality=90)
#         filestream.seek(0)
#         name = '{}.{}'.format(*self.image.name.split('.'))
#         self.image = InMemoryUploadedFile(
#             filestream, 'ImageField', name, 'jpeg/image', sys.getsizeof(filestream), None
#         )
#
#         super().save(*args, **kwargs)
#
#

class GameCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game_category_detail', kwargs={'slug': self.slug})


class GameBox(models.Model):
    STATUS_ON_STORAGE = 'on storage'
    STATUS_AVAILABLE = 'available'
    STATUS_RENTED = 'rented'
    STATUS_BOOKED = 'booked'
    STATUS_ON_REVIEW = 'on review'
    STATUS_BOUGHT = 'bought'
    STATUS_SPOILT = 'spoilt'
    STATUS_DONOR = 'donor'

    STATUS_CHOICES = (
        (STATUS_ON_STORAGE, 'Игра на складе'),
        (STATUS_AVAILABLE, 'Игра свободна'),
        (STATUS_RENTED, 'Игра арендована'),
        (STATUS_BOOKED, 'Игра забронирована'),
        (STATUS_ON_REVIEW, 'Игра на проверке'),
        (STATUS_BOUGHT, 'Игра куплена'),
        (STATUS_SPOILT, 'Игра испорчена'),
        (STATUS_DONOR, 'Игра донор')
    )
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=100, verbose_name='Статус экземпляра', choices=STATUS_CHOICES,
                              default=STATUS_ON_STORAGE, blank=True)
    game = models.ForeignKey('Game', verbose_name='Игра', on_delete=models.CASCADE, null=True)
   # bag_room = models.ForeignKey('BagRoom', verbose_name='Камера хранения', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Коробка с {}".format(str(self.slug))


class Game(models.Model):
    game_category = models.ManyToManyField(GameCategory, related_name='related_game_category')
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена/Залог')
    number_players = models.CharField(max_length=255, verbose_name='Количество игроков')
    rent = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Соимость аренды')
    game_time = models.CharField(max_length=255, verbose_name='Время пратии')

    game_boxes = models.ManyToManyField(GameBox, blank=True, related_name='related_game_box', verbose_name='ID Коробок')

    def __str__(self):
        return self.title

    def get_model_name(self):
        return self.__class__.__name__.lower()

    def save(self, *args, **kwargs):
        image = self.image
        img = Image.open(image)
        new_img = img.convert('RGB')
        resize_new_img = new_img.resize((200, 200), Image.ANTIALIAS)
        filestream = BytesIO()
        resize_new_img.save(filestream, 'JPEG', quality=90)
        filestream.seek(0)
        name = '{}.{}'.format(*self.image.name.split('.'))
        self.image = InMemoryUploadedFile(
            filestream, 'ImageField', name, 'jpeg/image', sys.getsizeof(filestream), None
        )
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

class CartGame(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    game=models.ForeignKey(Game,verbose_name='Игра', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.game.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.game.price
        super().save(*args, **kwargs)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(CartGame, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена', default=0)
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True)
    orders = models.ManyToManyField('Order', verbose_name='Заказы покупателя', related_name='related_customer')

    def __str__(self):
        return "{} Покупатель: {} {}".format(self.id,self.user.first_name, self.user.last_name)


class Order(models.Model):
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ выолнен')
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DELIVERY, 'Доставка')
    )

    customer = models.ForeignKey(Customer, verbose_name='Покупатель', related_name='related_orders',
                                 on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    address = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)
    status = models.CharField(max_length=100, verbose_name='Статус заказа', choices=STATUS_CHOICES, default=STATUS_NEW)
    buying_type = models.CharField(max_length=100, verbose_name='Тип заказа', choices=BUYING_TYPE_CHOICES,
                                   default=BUYING_TYPE_SELF)
    comment = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    order_date = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)





class GameGetProductsManager:
    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        products = Game.objects.all()
        return products


class GameGetProducts:
    object = GameGetProductsManager()


# ----------------------------------------------------------------------------------------------------------------------
class BagRoom(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    slug = models.SlugField(unique=True)
    rent = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Стоимость аренды')
    cells = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Количество ячеек')
    free_cells = models.DecimalField(max_digits=4, decimal_places=0, verbose_name='Количество свободных ячеек')

    def __str__(self):
        return self.name


class Event(models.Model):
    TYPE_BOOKED = 'booked'
    TYPE_PASS_CHECK = 'passed check'
    TYPE_PASS_CHECK_EMPLOYEE = 'passed check employee'
    TYPE_NO_PASS_CHECK = 'no passed check'
    TYPE_NO_PASS_CHECK_EMPLOYEE = 'no passed check employee'
    TYPE_START_RENT = 'start rent'
    TYPE_FINISH_RENT = 'finish rent'
    TYPE_BUY = 'buy'

    TYPE_CHOICES = (
        (TYPE_BOOKED, 'Игра забронирована'),
        (TYPE_PASS_CHECK, 'Игра прошла проверку клиентом'),
        (TYPE_PASS_CHECK_EMPLOYEE, 'Игра прошла проверку сотрудником'),
        (TYPE_NO_PASS_CHECK, 'Игра НЕ прошла проверку клиентом'),
        (TYPE_NO_PASS_CHECK_EMPLOYEE, 'Игра НЕ прошла проверку сотрудником'),
        (TYPE_START_RENT, 'Начало бронирования'),
        (TYPE_FINISH_RENT, 'Конец бронирования'),
        (TYPE_BUY, 'Купили игру')
    )
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=100, verbose_name='Тип события', choices=TYPE_CHOICES, blank=True)
    game_box = models.ForeignKey('GameBox', verbose_name='Игра', on_delete=models.CASCADE, null=True)
    rent = models.ForeignKey('Rent', verbose_name='Аренда', on_delete=models.CASCADE, null=True)


class Rent(models.Model):
    STATUS_GAME_BOOKED = 'game_booked'
    STATUS_DEPOSIT_PAY = 'deposit_pay'
    STATUS_GAME_RENT = 'game_rent'
    STATUS_RENT_END = 'rent_end'
    STATUS_DEPOSIT_RETURN = 'deposit_return'

    STATUS_CHOICES = (
        (STATUS_GAME_BOOKED, 'Клиент забронировал игры'),
        (STATUS_DEPOSIT_PAY, 'Клиент внес депозит'),
        (STATUS_GAME_RENT, 'Клиент арендовал игры'),
        (STATUS_RENT_END, 'клиент вернул игры'),
        (STATUS_DEPOSIT_RETURN, 'Мы вернули депозит')
    )

    customer = models.ForeignKey(Customer, verbose_name='Покупатель', related_name='related_rent',
                                 on_delete=models.CASCADE)
    status = models.CharField(max_length=100, verbose_name='Статус аренды', choices=STATUS_CHOICES,
                              default=STATUS_GAME_BOOKED)
    booked_time = models.DateTimeField(auto_now=True, verbose_name='Дата/время начала брони')
    rent_time_start = models.DateTimeField(auto_now=True, verbose_name='Дата/время начала аренды')
    rent_time_finish = models.DateTimeField(auto_now=True, verbose_name='Дата/время окончания аренды')

    rent = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая стоимость аренды')
    booked = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая стоимость брони')
    deposit = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая стоимость залога')

    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)
