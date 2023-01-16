def find_movies(db: list[dict[str, str|int]], search: str) -> list[dict[str, str|int]]:
    results = []
    for movie in db:
        if search.lower() in movie["name"].lower():
            results.append(movie)
    return results