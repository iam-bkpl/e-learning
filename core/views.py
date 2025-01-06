# External imports
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from rest_framework import filters

# Custom imports
from .models import Batch, Product, Warehouse
from .serializers import (
    BatchSerializer,
    CreateBatchSerializer,
    UpdateBatchSerializer,
    ProductSerializer,
    WarehouseSerializer,
)


class BatchViewSet(ModelViewSet):
    queryset = Batch.objects.select_related("product", "warehouse").all()
    http_method_names = ["get", "post", "patch"]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["product__name", "warehouse__name", "batch_name"]
    ordering_fields = ["quantity", "created_at"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateBatchSerializer
        if self.request.method == "PATCH":
            return UpdateBatchSerializer
        return BatchSerializer
