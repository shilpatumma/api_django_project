from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product
from .serializers import ProductSerializer
from django.views.generic import TemplateView



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by()  # Ordering by 'id', you can change this as needed
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # pagination_class = None  # Optional: Pagination can be disabled at the view level

    @action(detail=False, methods=['get'])
    def recent_products(self, request):
        recent_products = Product.objects.order_by('-created_at')[:5]
        serializer = self.get_serializer(recent_products, many=True)
        return Response(serializer.data)
    

class HomeView(TemplateView):
    template_name = 'home.html'