-- Write your PostgreSQL query statement below
SELECT name FROM Employee
WHERE id IN (
    SELECT managerId FROM Employee
    GROUP BY managerId
    HAVING COUNT(id) >= 5
);


-- SELECT managerId FROM Employee
-- GROUP BY managerId
-- HAVING COUNT(id) >= 5