-- Get the state_id for 'California'
SELECT id FROM states WHERE name = 'California';

-- List all cities for the state with the retrieved id
SELECT cities.id, cities.name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id ASC;
