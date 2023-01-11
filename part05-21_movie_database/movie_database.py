def add_movie(db: list[dict], name: str, director: str, year: int, runtime: int) -> None:
    db.append({
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    })