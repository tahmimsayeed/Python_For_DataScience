students = [
    {"name": "Amina", "major": "AMDS"},
    {"name": "Maya", "major": "Economics"},
    {"name": "Disha", "major": "AMDS"},
    {"name": "Nora", "major": "Public Health"},
    {"name": "Lina", "major": "Economics"}
]

groups = {}
for student in students:
    major = student["major"]
    if major not in groups:
        groups[major] = []
    groups[major].append(student["name"])

counts = {}
for major, names in groups.items():
    counts[major] = len(names)

print("Groups:", groups)
print("Counts:", counts)