from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import generics
from .models import Product, Cart, CartItem, Order
from .serializers import ProductSerializer, CartSerializer, CartItemSerializer,OrderSerializer

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartCreateAPIView(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemCreateAPIView(CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartItemListAPIView(ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer