def main():
    course_points = input_course_points()
    points_sum = 0
    passes = 0
    distribution = [0] * 6
    
    for points in course_points:
        points_sum += total_points(points)
        if passed(points):
            passes += 1
        distribution[grade(points)] += 1
        
    print("Statistics:")
    print(f"Points average: {(points_sum / len(course_points)):.1f}")
    print(f"Pass percentage: {(passes / len(course_points) * 100):.1f}")
    print("Grade distribution:")
    for i in range(5, -1, -1):
        print(f"  {i}: {'*' * distribution[i]}")

def input_course_points() -> list[list[int]]:
    course_points = []
    while True:
        points = input("Exam points and exercises completed: ")
        if points == "":
            break
        
        course_points.append([int(points) for points in points.split(" ")])
    return course_points

def total_points(points: list[int]) -> int:
    return points[0] + (points[1] // 10)

def passed(points: list[int]) -> bool:
    if points[0] < 10 or total_points(points) < 15:
        return False
    return True

def grade(points: list[int]) -> int:
    if points[0] < 10:
        return 0
    
    total = total_points(points)
    bounds = [14, 17, 20, 23, 27, 30]
    for i in range(6):
        if total <= bounds[i]:
            return i

main()