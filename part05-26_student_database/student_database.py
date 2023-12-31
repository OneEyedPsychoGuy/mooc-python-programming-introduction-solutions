def add_student(students: dict[str, list[tuple[str, int]]], name: str) -> None:
    students[name] = []

def add_course(students: dict[str, list[tuple[str, int]]], name: str, course_to_add: tuple[str, int]) -> None:
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

def print_student(students: dict[str, list[tuple[str, int]]], name: str) -> None:
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

def summary(students: dict[str, list[tuple[str, int]]]):
    most_courses = ""
    best_average = 0
    best_average_name = ""
    for name in students:
        if len(students[name]) > len(students.get(most_courses, [])):
            most_courses = name
        
        sum = 0
        for course in students[name]:
            sum += course[1]
        
        average = sum / len(students[name])
        if average > best_average:
            best_average = average
            best_average_name = name
        
    print(f"students {len(students)}")
    print(f"most courses completed {len(students[most_courses])} {most_courses}")
    print(f"best average grade {best_average} {best_average_name}")