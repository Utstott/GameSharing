from django.shortcuts import render
from django.views.generic import DetailView, View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .mixins import CategoryDetailMixin, CartMixin, ProductDetailMixin
from django.contrib import messages
from .forms import OrderForm, LoginForm, RegistrationForm
from .utils import recalc_cart
from django.db import transaction

from .models import (
    # Category,
    Customer,
    Cart,
    CartGame,
    GameCategory,
    GameBox,
    GameGetProducts,
    Game,
    Order
)


class BaseView(CartMixin, View):

    def get(self, request, *argc, **kwargs):
        categories = GameCategory.objects.all()
        products = GameGetProducts.object.get_products_for_main_page()
        context = {
            'categories': categories,
            'products': products,
            'cart': self.cart
        }
        return render(request, 'base.html', context)


class ProductDetailView(CartMixin, ProductDetailMixin, DetailView):

    def dispatch(self, request, *args, **kwargs):
        # self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.model = Game
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ct_model'] = self.model._meta.model_name
        context['cart'] = self.cart
        context['categories'] = GameCategory.objects.all()
        return context


class GameCategoryDetailView(CartMixin, CategoryDetailMixin, DetailView):
    model = GameCategory
    queryset = GameCategory.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = self.cart
        return context


# class BaseView(CartMixin, View):
#
#     def get(self, request, *argc, **kwargs):
#         categories = Category.objects.get_categories_for_left_sidebar()
#         products = LatestProducts.object.get_products_for_main_page(
#             'notebook', 'smartphone', with_respect_to='notebook'
#         )
#         context = {
#             'categories': categories,
#             'products': products,
#             'cart': self.cart
#         }
#         return render(request, 'base.html', context)


# class ProductDetailView(CartMixin, CategoryDetailMixin, DetailView):
#     print("PRODUCT")
#     CT_MODEL_MODEL_CLASS = {
#         'notebook': Notebook,
#         'smartphone': Smartphone
#     }
#
#     def dispatch(self, request, *args, **kwargs):
#         self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
#         self.queryset = self.model._base_manager.all()
#         return super().dispatch(request, *args, **kwargs)
#
#     context_object_name = 'product'
#     template_name = 'product_detail.html'
#     slug_url_kwarg = 'slug'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['ct_model'] = self.model._meta.model_name
#         context['cart'] = self.cart
#         return context


# class CategoryDetailView(CartMixin, CategoryDetailMixin, DetailView):
#     model = Category
#     queryset = Category.objects.all()
#     context_object_name = 'category'
#     template_name = 'category_detail.html'
#     slug_url_kwarg = 'slug'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['cart'] = self.cart
#         return context


class AddToCartView(CartMixin, View):

    def get(self, request, *argc, **kwargs):
        game_slug = kwargs.get('slug')
        game = Game.objects.get(slug=game_slug)
        print('User {}'.format(self.cart.owner))
        cart_game, created = CartGame.objects.get_or_create(user=self.cart.owner, cart=self.cart, game=game)
        if created:
            self.cart.products.add(cart_game)
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, "Товар успешно добавлен")
        return HttpResponseRedirect('/cart/')


class DeleteCartView(CartMixin, View):

    def get(self, request, *args, **kwargs):
        game_slug = kwargs.get('ct_model'), kwargs.get('slug')
        game = Game.objects.get(slug=game_slug)
        cart_game = CartGame.objects.get(user=self.cart.owner, cart=self.cart, game=game)

        self.cart.products.remove(cart_game)
        cart_game.delete()
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, "Товар успешно удален")
        return HttpResponseRedirect('/cart/')


class ChangeQTYView(CartMixin, View):
    def post(self, request, *args, **kwargs):
        game_slug = kwargs.get('slug')
        game = Game.objects.get(slug=game_slug)
        cart_game = CartGame.objects.get(user=self.cart.owner, cart=self.cart, game=game)
        qty = int(request.POST.get('qty'))
        cart_game.qty = qty
        cart_game.save()
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, "Количество успешно изменено")
        return HttpResponseRedirect('/cart/')


class CartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        categories = GameCategory.objects.all()
        context = {
            'cart': self.cart,
            'categories': categories
        }
        return render(request, 'cart.html', context)


class CheckOutView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        # categories = Category.objects.get_categories_for_left_sidebar()
        categories = GameCategory.objects.all()
        form = OrderForm(request.POST or None)
        context = {
            'cart': self.cart,
            'categories': categories,
            'form': form
        }
        return render(request, 'checkout.html', context)


class MakeOrderView(CartMixin, View):
    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        customer = Customer.objects.get(user=request.user)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = customer
            new_order.first_name = form.cleaned_data['first_name']
            new_order.last_name = form.cleaned_data['last_name']
            new_order.phone = form.cleaned_data['phone']
            new_order.address = form.cleaned_data['address']
            new_order.buying_type = form.cleaned_data['buying_type']
            new_order.order_data = form.cleaned_data['order_date']
            new_order.comment = form.cleaned_data['comment']
            new_order.save()
            self.cart.in_order = True
            self.cart.save()
            new_order.cart = self.cart
            new_order.save()
            customer.orders.add(new_order)
            messages.add_message(request, messages.INFO,
                                 "Спасибо за заказ, вам придет SMS c информацией на номер {}".format(new_order.phone))
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/check_out/')


class LoginView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        categories = GameCategory.objects.all()
        context = {
            'form': form,
            'categories': categories,
            'cart': self.cart
        }
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
        context = {'form': form, 'cart': self.cart}
        return render(request, 'login.html', context)

class RegistrationView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        categories = GameCategory.objects.all()
        context = {
            'form': form,
            'categories': categories,
            'cart': self.cart
        }
        return render(request, 'registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user=form.save(commit=False)
            new_user.username=form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password (form.cleaned_data['password'])
            new_user.save()
            Customer.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone'],
                address = form.cleaned_data['address']
            )
            # user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            user=form.save()
            login(request, user)
            return HttpResponseRedirect('/')
        context = {'form': form, 'cart': self.cart}
        return render(request, 'registration.html', context)

class ProfileView(CartMixin, View):

    def get (self, request, *args, **kwargs):
        customer=Customer.objects.get(user=request.user)
        orders=Order.objects.filter(customer=customer).order_by('-created_at')
        categories=GameCategory.objects.all()
        context={'orders': orders, 'cart':self.cart, 'categories':categories}
        return render(
            request,
            'profile.html',
            context
        )
