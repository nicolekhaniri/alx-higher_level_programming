-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

SELECT show.title, genre.genre_id
FROM tv_shows AS shows
INNER JOIN tv_show_genres as genres
ON shows.id = genre.show_id
ORDER BY show.title, genre.genre_id;
