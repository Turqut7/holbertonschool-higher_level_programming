-- lists records with non-null and non-empty names ordered by score desc
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
