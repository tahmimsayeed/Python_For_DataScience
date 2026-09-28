list = ["banana","apple","mango","guava","kiwi"]
n = input("Enter a fruit name: ").lower()
if n in list: 
   print("Item in list")
else:
   print("Item not in list")
   list.append(n)   
print(list)

        