# 3main3.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer


# CATEGORY

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"


# PRODUCT

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"


# REVIEW

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "id"from django.urls import path
from .views import *

urlpatterns = [

    path('api/v1/categories/', CategoryListCreateView.as_view()),
    path('api/v1/categories/<int:id>/', CategoryRetrieveUpdateDeleteView.as_view()),

    path('api/v1/products/', ProductListCreateView.as_view()),
    path('api/v1/products/<int:id>/', ProductRetrieveUpdateDeleteView.as_view()),

    path('api/v1/reviews/', ReviewListCreateView.as_view()),
    path('api/v1/reviews/<int:id>/', ReviewRetrieveUpdateDeleteView.as_view()),

]
