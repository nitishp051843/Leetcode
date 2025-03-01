-- Write your PostgreSQL query statement below
-- SELECT w2.id
-- FROM Weather w1
-- JOIN Weather w2 ON w1.id=w2.id+1
-- WHERE w1.temperature < w2.temperature;


-- Write your PostgreSQL query statement below
SELECT w1.id
FROM Weather w1
JOIN Weather w2 ON w1.recordDate - w2.recordDate = 1
WHERE w1.temperature > w2.temperature;