-- lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked
-- If a show doesn’t have a genre, display NULL
SELECT s.title, g.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g
ON g.show_id = s.id
WHERE s.genre_id IS NULL
ORDER BY s.title ASC, g.genre_id ASC;

