words = ["model", "data", "python", "data",
"model", "analysis", "data"]
frequency = {}
counts = []
for word in words:
    frequency[word] = frequency.get(word,0)+1
    if frequency[word] >1:
        counts.append(word)
print(f"Frequency: {frequency}")
print(f"Repeated words: {counts}")