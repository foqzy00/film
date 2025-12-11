import json
import os


def load_movies(path: str) -> list[dict]:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            movies = json.load(file)
        if isinstance(movies, list):
            return movies
        else:
            raise ValueError("Файл не содержит список")

    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла {path}: {e}")
        return []


def save_movies(path: str, movies: list[dict]) -> None:
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(movies, file, ensure_ascii=False, indent=4)

def add_movie(movies: list[dict], title: str, year: int) -> list[dict]:
        if movies:
            max_id = max(movie['id'] for movie in movies)
            new_id = max_id + 1
        else:
            new_id = 1
        new_movie = {
            "id": new_id,
            "title": title,
            "year": year,
            "watched": False
        }
        return movies + [new_movie]


def mark_watched(movies: list[dict], movie_id: int) -> list[dict]:
    updated_movies = []
    for movie in movies:
        if movie['id'] == movie_id:
            movie['watched'] = True
        updated_movies.append(movie)
    return updated_movies


def find_by_year(movies: list[dict], year: int) -> list[dict]:
    found_movies = [movie for movie in movies if movie['year'] == year]
    return found_movies