-- Display max temperature of each state
-- Ordered by state name ascending
SELECT state, MAX(value) as max_temp
FROM temperatures
ORDER BY state;

