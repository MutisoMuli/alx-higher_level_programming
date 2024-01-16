-- Script that lists the number of records with the same score in second_table
-- Results should display the score and number of records with the label number
-- List should be in descending order
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;