def add_student(students: dict, name: str) -> None:
    students[name] = []

def add_course(students: dict, name: str, course_to_add: tuple[str, int]) -> None:
    if course_to_add[1] == 0:
        return
    
    for course in students[name]:
        if course[0] == course_to_add[0]:
            if course[1] > course_to_add[1]:
                return
            else:
                students[name].remove(course)
                break
    students[name].append(course_to_add)

def print_student(students: dict, name: str) -> None:
    if name in students:
        text = f"{name}:\n "
        courses = students[name]
        if len(courses) == 0:
            text += "no completed courses"
        else:
            text += f"{len(courses)} completed courses:\n"
            sum = 0
            for course in courses:
                text += f"  {course[0]} {course[1]}\n"
                sum += course[1]
            text += f" average grade {sum / len(courses)}"
        print(text)
    else:
        print(f"{name}: no such person in the database")

students = {}
add_student(students, "Peter")
add_course(students, "Peter", ("Introduction to Programming", 3))
add_course(students, "Peter", ("Advanced Course in Programming", 2))
add_course(students, "Peter", ("Data Structures and Algorithms", 0))
add_course(students, "Peter", ("Introduction to Programming", 2))
print_student(students, "Peter")