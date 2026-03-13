from rest_framework.generics import  CreateAPIView ,ListAPIView
from .models import Product, Cart, CartItem
from .serializers import ProductSerializer, CartSerializer, CartItemSerializer

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
