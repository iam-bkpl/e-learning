from rest_framework import serializers
from .models import Batch, Product, Warehouse

from .utils import get_unique_batch_number


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class BatchSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    warehouse = WarehouseSerializer()

    class Meta:
        model = Batch
        fields = [
            "id",
            "batch_number",
            "batch_name",
            "product",
            "quantity",
            "purchase_price",
            "sales_price",
            "warehouse",
            "created_at",
            "updated_at",
        ]


class CreateBatchSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source="product.name")
    warehouse = serializers.CharField(source="warehouse.name")

    class Meta:
        model = Batch
        fields = [
            "batch_name",
            "product",
            "quantity",
            "purchase_price",
            "sales_price",
            "warehouse",
        ]

    def create(self, validated_data):
        product_name = validated_data.pop("product")["name"]
        warehouse_name = validated_data.pop("warehouse")["name"]

        batch_number = get_unique_batch_number()

        product, _ = Product.objects.get_or_create(name=product_name)
        warehouse, _ = Warehouse.objects.get_or_create(name=warehouse_name)

        return Batch.objects.create(
            batch_number=batch_number,
            product=product,
            warehouse=warehouse,
            **validated_data,
        )


class UpdateBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ["batch_number", "quantity"]
