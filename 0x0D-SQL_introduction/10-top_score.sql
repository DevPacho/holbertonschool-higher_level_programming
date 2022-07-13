-- List some records ordered in a specific way.
-- Script that lists all records of the table 'second_table', but
-- the records should be ordered by score (top first).

SELECT score, name FROM second_table ORDER BY score DESC;
