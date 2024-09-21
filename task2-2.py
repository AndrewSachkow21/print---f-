product_name = input("Введіть назву товару: ")
quantity = int(input("Введіть кількість: "))
price = float(input("Введіть ціну за одиницю: "))

total_cost = quantity * price

print(f"Продукт: {product_name}, Кількість: {quantity}, Вартість: {total_cost},Усього вилучено{total_cost}")