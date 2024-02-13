-- Display max temperature of each state
-- Ordered by state name ascending
SELECT state, MAX(value)
FROM temperatures
ORDER BY state;

