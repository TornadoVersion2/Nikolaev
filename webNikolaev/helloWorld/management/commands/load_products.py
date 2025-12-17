from django.core.management.base import BaseCommand
from helloWorld.models import Product


class Command(BaseCommand):
    help = 'Загружает начальные данные продуктов в базу данных'

    def handle(self, *args, **options):
        products_data = [
            {
                'name': 'Базовый пакет',
                'description': 'Стандартный набор функций для малого бизнеса',
                'category': 'Пакеты услуг',
                'price': 15000.00,
                'status': 'available'
            },
            {
                'name': 'Профессиональный пакет',
                'description': 'Расширенный функционал для среднего бизнеса',
                'category': 'Пакеты услуг',
                'price': 35000.00,
                'status': 'available'
            },
            {
                'name': 'Корпоративный пакет',
                'description': 'Полный набор инструментов для крупных компаний',
                'category': 'Пакеты услуг',
                'price': 75000.00,
                'status': 'limited'
            },
            {
                'name': 'Веб-сайт "Старт"',
                'description': 'Готовый сайт-визитка с базовым функционалом',
                'category': 'Веб-разработка',
                'price': 25000.00,
                'status': 'available'
            },
            {
                'name': 'Веб-сайт "Бизнес"',
                'description': 'Корпоративный сайт с CMS и админ-панелью',
                'category': 'Веб-разработка',
                'price': 55000.00,
                'status': 'available'
            },
            {
                'name': 'Интернет-магазин',
                'description': 'Полнофункциональный интернет-магазин с интеграцией платежей',
                'category': 'Веб-разработка',
                'price': 120000.00,
                'status': 'available'
            },
            {
                'name': 'Мобильное приложение',
                'description': 'Кроссплатформенное мобильное приложение для iOS и Android',
                'category': 'Мобильная разработка',
                'price': 200000.00,
                'status': 'limited'
            },
            {
                'name': 'Консультация "Эксперт"',
                'description': 'Индивидуальная консультация с экспертом по вашему проекту',
                'category': 'Консалтинг',
                'price': 5000.00,
                'status': 'available'
            },
            {
                'name': 'Дизайн-пакет "Премиум"',
                'description': 'Полный брендинг: логотип, фирменный стиль, дизайн сайта',
                'category': 'Дизайн',
                'price': 45000.00,
                'status': 'new'
            },
            {
                'name': 'Техническая поддержка',
                'description': 'Годовая техническая поддержка и обслуживание',
                'category': 'Поддержка',
                'price': 30000.00,
                'status': 'available'
            },
        ]

        # Очищаем существующие данные (опционально)
        Product.objects.all().delete()
        
        # Создаем продукты
        created_count = 0
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                created_count += 1
            else:
                # Обновляем существующий продукт
                for key, value in product_data.items():
                    setattr(product, key, value)
                product.save()

        total_count = Product.objects.count()
        message = f'Successfully loaded {created_count} products. Total products in database: {total_count}'
        self.stdout.write(self.style.SUCCESS(message))

