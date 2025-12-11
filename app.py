from logic import load_movies, save_movies, add_movie, mark_watched, find_by_year

DATA_FILE = "movies.json"

def main():
    movies = load_movies(DATA_FILE)

    while True:
        print("\nКаталог фильмов")
        print("1. Показать все фильмы")
        print("2. Добавить фильм")
        print("3. Отметить фильм как просмотренный")
        print("4. Найти фильмы по году")
        print("0. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            if movies:
                for movie in movies:
                    watched_status = "Просмотрено" if movie['watched'] else "Не просмотрено"
                    print(f"{movie['id']}. {movie['title']} ({movie['year']}): {watched_status}")
            else:
                print("Список фильмов пуст.")

        elif choice == "2":
            title = input("Введите название фильма: ")
            year = input("Введите год выхода фильма: ")
            if year.isdigit():
                year = int(year)
                movies = add_movie(movies, title, year)
                save_movies('movies.json', movies)
                print("Фильм добавлен.")
            else:
                print("Ошибка: год должен быть числом.")

        elif choice == "3":
            for movie in movies:
                watched_status = "Просмотрено" if movie['watched'] else "Не просмотрено"
                print(f"{movie['id']}. {movie['title']} ({movie['year']}): {watched_status}")
            movie_id = input("Введите ID фильма для отметки как просмотренного: ")
            if movie_id.isdigit():
                movie_id = int(movie_id)
                movies = mark_watched(movies, movie_id)
                save_movies('movies.json', movies)
                print("Фильм отмечен как просмотренный.")
            else:
                print("Ошибка: ID должен быть числом.")

        elif choice == "4":
            for movie in movies:
                print(f"{movie['id']}. {movie['title']} ({movie['year']})")
            year = input("Введите год для поиска фильмов: ")
            if year.isdigit():
                year = int(year)
                found_movies = find_by_year(movies, year)
                if found_movies:
                    for movie in found_movies:
                        print(f"{movie['id']}. {movie['title']} ({movie['year']})")
                else:
                    print("Фильмов не найдено.")
            else:
                print("Ошибка: год должен быть числом.")

        elif choice == "0":
            save_movies(DATA_FILE, movies)
            print("До свидания!")
            break

        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    main()