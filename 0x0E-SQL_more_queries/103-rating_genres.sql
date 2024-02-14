-- 
SELECT name, SUM(tsr.rate) rating
FROM tv_genres AS tg
INNER JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id
INNER JOIN tv_show_ratings AS tsr
ON tsg.show_id = tsr.show_id
GROUP BY name
ORDER BY rating DESC;

