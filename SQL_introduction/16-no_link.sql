-- name value and display the score decending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
