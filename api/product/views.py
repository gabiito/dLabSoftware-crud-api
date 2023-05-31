from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from .models import Product   

from .serializers import ProductSerializer

@extend_schema_view(
    list    = extend_schema(summary = 'List all products'),
    retrieve= extend_schema(summary = 'Retrieve a product'),
    create  = extend_schema(summary = 'Create a product'),
    update  = extend_schema(summary = 'Update a product'),
    partial_update  = extend_schema(summary = 'Partially update a product'),
    destroy = extend_schema(summary = 'Delete a product'),
)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
