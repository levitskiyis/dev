
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
#1.Общая выручка
def total_revenue (purchases):
    total_revenue=0
    for idx,i in enumerate(purchases):
        total_revenue+=i['price']*i['quantity']
        #print (total_revenue)
    return total_revenue
#2.Список товаров по категориям
def items_by_category(purchases):
    frequency={}
    for idx,i in enumerate(purchases):
       if i['category'] not in frequency:
        frequency[i['category']]=[i['item']]
       else:
           frequency[i['category']].append(i['item'])
    return frequency
#3.Список покупок, где цена превышает заданное значение
def expensive_purchases(purchases, min_price=1):
    product_list = []
    for idx, i in enumerate(purchases):
        if i['price']> min_price :
            product_list.append(i)
    return product_list
#4.Средняя цена товаров по категориям
def average_price_by_category(purchases):
    frequency = {}
    for idx, i in enumerate(purchases):
        if i['category'] not in frequency:
            frequency[i['category']] = (i['price'])
        else:
            frequency[i['category']] = (frequency[i['category']]+ (i['price']))/2
    return frequency
#5.Категория с наибольшим числом проданных товаров
def most_frequent_category(purchases):
    frequency = {}
    for idx, i in enumerate(purchases):
        if i['category'] not in frequency:
            frequency[i['category']] = (i['quantity'])
        else:
            frequency[i['category']] = (frequency[i['category']] + (i['quantity']))
    for idx, i in enumerate(frequency):
       if frequency[i] == max(frequency.values()):
           return i
# Агрегация функций в общий вывод
print (f"Общая выручка: {total_revenue (purchases)}\n"
       f"Товары по категориям: {items_by_category(purchases)}\n"
       f"Покупки дороже 1.0: {expensive_purchases(purchases, min_price=1)}\n"
       f"Средняя цена по категориям: {average_price_by_category(purchases)}\n"
       f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}\n")