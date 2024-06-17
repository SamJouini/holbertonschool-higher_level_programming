-- List all records from the table second_table with a name value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
