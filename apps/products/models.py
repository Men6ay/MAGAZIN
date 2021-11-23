from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):

    title = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Название'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='product_user'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена: '
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='Колличество: '
        )
    is_stock = models.BooleanField(
        default=True,
        db_index=True
        )
    
    class Meta:

        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('-id',)

    def __str__(self):
        return self.title

class ProductImage(models.Model):

    image = models.ImageField(
        upload_to = 'product',
        verbose_name='Картинка',
        blank = True,
        null=True,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_image',
    )

    def __str__(self):
        return self.product.title

