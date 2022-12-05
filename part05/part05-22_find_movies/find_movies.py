def find_movies(db: list[dict], search: str) -> list[dict]:
    results = []
    for movie in db:
        if search.lower() in movie["name"].lower():
            results.append(movie)
    return results