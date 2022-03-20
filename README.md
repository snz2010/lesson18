## Домашняя работа по уроку 18

**Варианты обращения к таблице "movies" БД:**

GET:

    * 1. получить все фильмы: http://localhost:10001/movies/

    * 2. получить фильм по ID: http://localhost:10001/movies/1

    * 3. получить все фильмы режиссера: http://localhost:10001/movies?director_id=15

    * 4. получить все фильмы жанра: http://localhost:10001/movies?genre_id=17

    * 5. получить все фильмы за год: http://localhost:10001/movies?year=2010

POST:

    * 6. создать фильм: http://localhost:10001/movies

PUT:

    * 7. изменить информацию о фильме: http://localhost:10001/movies/21

DELETE:

    * 8. удалить фильм: http://localhost:10001/movies/21


**Варианты обращения к таблице "directors" БД:**

GET:

    * 1. http://localhost:10001/directors/ — получить всех режиссеров.

    * 2. http://localhost:10001/directors/18 — получить режиссера по ID


**Варианты обращения к таблице "genres" БД:**

GET:

    * 1. http://localhost:10001/genres/ — получить все жанры.

    * 2. http://localhost:10001/genres/3 — получить жанр по ID.

