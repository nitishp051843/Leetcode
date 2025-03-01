-- Write your PostgreSQL query statement below
select a1.machine_id, ROUND(avg(a1.timestamp - a2.timestamp)::numeric, 3) as processing_time
-- select *
FROM Activity a1
JOIN Activity a2 ON a1.activity_type != a2.activity_type
AND a1.process_id=a2.process_id
AND a1.machine_id=a2.machine_id
WHERE a1.activity_type != 'start'
GROUP BY a1.machine_id
