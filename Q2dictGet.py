inventory = {"pen": 12, "book": 5}

print(inventory.get("pen", 435))
print(inventory.get("ruler", 2))
print(inventory)
inventory["ruler"] = inventory.get("ruler", 0) + 3
print(inventory)