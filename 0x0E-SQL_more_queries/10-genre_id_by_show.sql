-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

SELECT show.title, genres.genre_id
FROM tv_shows AS shows
INNER JOIN tv_show_genres as genres
ON shows.id = genres.show_id
ORDER BY shows.title, genres.genre_id;
