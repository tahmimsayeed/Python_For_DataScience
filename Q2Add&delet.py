fruits = ['Apple','banana','mango']
fruits.extend(["Kiwi",'mulberry'])
fruits.append("Apple")
fruits.insert(0,"Guava")
print(fruits)
fruits.pop(1)
del fruits[-1]
fruits.remove("Kiwi")
print(fruits)
