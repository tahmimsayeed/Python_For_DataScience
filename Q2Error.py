student = {"name":"Disha","Age":23,"CG":3.33}
print(student.get('score'))
try:
    print(student["Ug year"])
except KeyError as error:
    print(type(error).__name__)
    print(error)
