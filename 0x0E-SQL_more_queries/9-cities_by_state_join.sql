-- lists all the cities
SELECT c.id, c.name, s.name
FROM cities AS c
JOIN states AS s
WHERE c.state_id = s.id;

