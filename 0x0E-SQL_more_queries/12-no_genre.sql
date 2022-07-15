-- Lists values with some requeriments.

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.show_id = NULL AND tv_shows.id = NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
