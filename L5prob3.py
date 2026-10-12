stock = {"pen": 12, "book": 3, "bag": 2, "ruler": 9, "calculator": 1}
count = 0
low_stock = {name:price
             for name,price in stock.items()
             if price< 5}
for key,value in stock.items():
    count += value
print(f"Total units: {count}")
print(f"Low Stock: {low_stock}")