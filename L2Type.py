#take input. check int/take again. check grade. 
while True:
    try:
        n = int(input("Give a grade: "))
    except ValueError:
        print("Invalid input, enter a number.")
        continue

    if n >= 97:
        print("A+")
    elif n >= 90:
        print("A")
    elif n >= 83:
        print("A-")
    elif n >= 80:
        print("B+")
    elif n >= 73:
        print("B")
    elif n >= 70:
        print("B-")
    elif n >= 60:
        print("C")
    else:
        print("F")
        break   