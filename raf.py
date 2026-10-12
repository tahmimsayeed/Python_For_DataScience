students = {
    "S01": {"name": "Amina", "scores": [80, 90, 85]},
    "S02": {"name": "Disha", "scores": [70, 75, 80]},
}

for record in students.values():
    scores = record["scores"]
    mean = sum(scores) / len(scores)
    print(f"{record['name']}: {mean:.2f}")