from django.db import models

from core.utils import get_unique_batch_number


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "Product"

    def __str__(self):
        return self.name


class Warehouse(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "Warehouse"

    def __str__(self):
        return self.name


class Batch(BaseModel):
    batch_number = models.CharField(max_length=50, default=get_unique_batch_number())
    batch_name = models.CharField(max_length=255)

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="batches"
    )
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2)
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, related_name="batches"
    )

    class Meta:
        db_table = "Batch"

    def __str__(self):
        return self.batch_name
