-- List number of records with same score
SELECT score, COUNT(score) as number
GROUP BY score
ORDER BY number DESC;

