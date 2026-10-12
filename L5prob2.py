prices = {"pen":15,"book":120,"bag":850}
requested_items = ['book','ruler','pen']
for product in requested_items:
    price = prices.get(product,"not found")
    print(f"{product}: Tk {price}")

