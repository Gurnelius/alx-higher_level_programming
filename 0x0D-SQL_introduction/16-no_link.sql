-- List all records with name value
SELECT score, name
IFROM second_table
WHERE name IS NOT NULL;
ORDER BY score DESC;

