-- lists all genres from hbtn_0d_tvshows
-- and displays the number of shows linked to each.
SELECT g.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS g
JOIN tv_show_genres AS tsg
ON g.id = tsg.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;

