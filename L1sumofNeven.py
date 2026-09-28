n = int(input("Enter a number: "))
sum = 0
if(n % 2 == 0):
    i = 2
    while(i <= n):
        sum += i
        i += 2
else:
    i = 2
    while(i <= n-1):
        sum += i
        i += 2
print("The sum of first ",n,"even integers is:", sum)