SELECT name FROM people WHERE id in
(SELECT DISTINCT person_id FROM directors
JOIN movies ON directors.movie_id = movies.id
JOIN ratings ON movies.id = ratings.movie_id
WHERE rating >= 9.0);