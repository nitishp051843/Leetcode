-- Write your PostgreSQL query statement below
select name, bonus
from Employee E
LEFT JOIN Bonus b ON b.empId=E.empId
WHERE b.bonus < 1000 or b.bonus is null