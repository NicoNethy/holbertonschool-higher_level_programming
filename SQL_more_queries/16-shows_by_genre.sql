-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name

SELECT tv_shows.title, tv_genres.name
FROM tv_genres
RIGHT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
RIGHT JOIN  tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_genres.name ASC