values = [12,-5,0,7,-3,0,18,-1]
for value in values:
    if(value > 0):
        positive = []
        positive = positive.append(value)
    elif(value<0):
        negative = []
        negative.append(value)
    elif(value == 0):
        zero = []
        zero.append(value)

print("Positive: ", positive)
print("Negative: ",negative)
print("Zero: ",zero)