"""Модуль для отработки учебного кода"""
# temp.py


class Product:
    """Продукт"""
    def __init__(self, name, retail_price, purchase_price):
        self.name = name
        self.retail_price = retail_price
        self.purchase_price = purchase_price

    @property
    def profit(self):
        """Свойство продукта: разница между закупочной и розничной ценой"""
        return self.purchase_price - self.retail_price

    @staticmethod
    def average_price(price_list):
        """Статистический метод: возвращает средне значение цен из списка"""
        return ((sum(price for price in price_list)) /
                len(price_list) if price_list else 0)

    @property
    def information(self):
        """Информация о товаре"""
        return (f'Товар: {str.capitalize(self.name)}, '
                f'розничная цена: {self.retail_price}, '
                f'закупочная цена: {self.purchase_price}')


# Данные для проверки, не изменяйте их.
product_1 = Product('Картошка', 100, 90)
product_2 = Product('Перчатки', 150, 120)
product_3 = Product('Велосипед', 170, 150)

assortment_prices = [
    product_1.purchase_price,
    product_2.purchase_price,
    product_3.purchase_price
]

print(f'Средняя стоимость: {Product.average_price(assortment_prices)}')
print(f'Прибыль магазина с товара {product_1.name}: {product_1.profit}')
print(f'Информация о товаре {product_1.name}: {product_1.information}')
