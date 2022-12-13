from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    # pass
    class Meta:
        model = Product
        fields = ['title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    # pass
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']#'stock',

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'products', 'positions']

    # настройте сериализатор для склада
    def create(self, validated_data):
        print("create")
        # print(validated_data)
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)
        # заполнение связанной таблицы StockProduct
        self.update_positions(positions,stock)
        return stock

    def update(self, instance, validated_data):
        print("update")
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # заполнение связанной таблицы StockProduct
        self.update_positions(positions, stock)
        return stock
    def update_positions(self, positions, stock):
        for item in positions:
            StockProduct.objects.update_or_create(stock=stock, product=item['product'],
                defaults=dict(
                price=item['price'],
                quantity=item['quantity']
                )
            )