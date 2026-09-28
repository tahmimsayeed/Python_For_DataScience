n = int(input("Enter a number: "))
print("Fibonacci numbers are: ")

a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b