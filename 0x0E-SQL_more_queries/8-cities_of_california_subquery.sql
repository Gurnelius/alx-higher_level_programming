-- lists all the cities of California
SELECT c.id, c.name
FROM cities AS c
JOIN states AS s
WHERE c.state_id = s.id;

