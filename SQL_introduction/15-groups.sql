-- list records with the same score en orden decendiente
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
