Marks = [50,-100,-90,200,70,99,89,80]

for n in Marks: 
    if n >= 97:
        print(f"for {n}: A+")
    elif n >= 90:
        print(f"for {n}:A")
    elif n >= 83:
        print(f"for {n}:A-")
    elif n >= 80:
        print(f"for {n}:B+")
    elif n >= 73:
        print(f"for {n}:B")
    elif n >= 70:
        print(f"for {n}:B-")
    elif n >= 60:
        print(f"for {n}:C")
    else:
        print(f"for {n}:F")
        continue   