from django.db import models


class Product(models.Model):
    """Модель продукта"""
    
    STATUS_CHOICES = [
        ('available', 'В наличии'),
        ('limited', 'Ограниченное предложение'),
        ('new', 'Новинка'),
    ]
    
    name = models.CharField(max_length=200, verbose_name='Название продукта')
    description = models.TextField(verbose_name='Описание')
    category = models.CharField(max_length=100, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='available',
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['id']
    
    def __str__(self):
        return self.name
    
    def get_status_class(self):
        """Возвращает CSS класс для статуса"""
        status_map = {
            'available': 'status-available',
            'limited': 'status-limited',
            'new': 'status-new',
        }
        return status_map.get(self.status, 'status-available')
    
    def get_formatted_price(self):
        """Возвращает отформатированную цену"""
        return f"{self.price:,.0f} ₽".replace(',', ' ')
