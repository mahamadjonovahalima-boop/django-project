from django.urls import path
from .views import ProductListAPIView, CartItemCreateAPIView, CartItemListAPIView
from .views import CartCreateAPIView, OrderCreateView

urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('cart/create/', CartCreateAPIView.as_view()),
    path('cart/items/', CartItemListAPIView.as_view()),
    path('cart/add-product/', CartItemCreateAPIView.as_view()),
    path('order/', OrderCreateView.as_view()),
]