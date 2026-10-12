delivery_1 = {"pen": 12, "book": 5, "bag": 2}
delivery_2 = {"book": 4, "ruler": 10, "pen": 3}
grand_totl = 0
new_dictionary = delivery_1.copy()
for key,value in delivery_2.items():
    new_dictionary[key] = new_dictionary.get(key,0)+value
for key,value in new_dictionary.items():
    grand_totl += value
print(f"combined delivery: {new_dictionary}")
print(f"Grand total: {grand_totl}")
