def older_people(people: list[tuple[str, int]], year: int) -> list[str]:
    old = []
    for person in people:
        if person[1] < year:
            old.append(person[0])
    return old