-- Script that lists all records of second_table
-- Don't list rows without name value
-- Results should display the score and the name
-- Records should be in descending order
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC