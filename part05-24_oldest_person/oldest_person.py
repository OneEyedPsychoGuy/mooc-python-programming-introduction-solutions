def oldest_person(people: list[tuple[str, int]]) -> str:
    oldest = people[0]
    for person in people:
        if person[1] < oldest[1]:
            oldest = person
    return oldest[0]