def add_student(students: dict, name: str) -> None:
    students[name] = []

def print_student(students: dict, name: str) -> None:
    if name in students:
        print(f"{name}:\n no completed courses")
    else:
        print(f"{name}: no such person in the database")

students = {}
add_student(students, "Peter")
add_student(students, "Eliza")
print_student(students, "Peter")
print_student(students, "Eliza")
print_student(students, "Jack")