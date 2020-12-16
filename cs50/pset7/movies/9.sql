SELECT name FROM people
WHERE id in
(SELECT person_id FROM stars
JOIN movies ON stars.movie_id = movies.id
WHERE year = 2004) ORDER BY birth;