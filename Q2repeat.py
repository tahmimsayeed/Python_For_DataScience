colours = ["blue", "red", "blue", "green", "red",
"blue"]
frequency = {}
for colour in colours:
    frequency[colour] = frequency.get(colour,0)+1
print(frequency)