from django.shortcuts import render 
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product
from .serializers import ProductSerializer
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from .pagination import CustomPagination
from rest_framework.pagination import PageNumberPagination



class ProductPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100

def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 5)  # Show 5 products per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'product_list.html', {'page_obj': page_obj})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by()  # Ordering by 'id', you can change this as needed
    # queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPagination
    pagination_class = ProductPagination  # Optional: Pagination can be disabled at the view level

    @action(detail=False, methods=['get'])
    def recent_products(self, request):
        recent_products = Product.objects.order_by('-created_at')[:5]
        serializer = self.get_serializer(recent_products, many=True)
        return Response(serializer.data)


class HomeView(TemplateView):
    template_name = 'home.html'


def temper(request):
    return render(request, "temp.html")