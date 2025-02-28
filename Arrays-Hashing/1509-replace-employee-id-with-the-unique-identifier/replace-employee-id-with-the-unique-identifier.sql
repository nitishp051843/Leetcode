-- Write your PostgreSQL query statement below
select EU.unique_id, E.name from Employees E
LEFT JOIN EmployeeUNI EU ON E.id=EU.id;