-- Display average temperatures by city
-- ordered by temperature descending
SELECT city, AVG(value) AS avg_temp
`FROM temperatures
GROUP BY avg_temp
ORDER BY avg_temp DESC;

