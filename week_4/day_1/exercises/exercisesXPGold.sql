-- Fetch the first four students. You have to order the four students alphabetically by last_name.
SELECT * FROM student 
ORDER BY last_name
LIMIT 4;


-- Fetch the details of the youngest student.
SELECT * FROM student
ORDER BY birth_date DESC
LIMIT 1;

-- Fetch three students skipping the first two students.
SELECT * FROM student 
ORDER BY id
OFFSET 2
LIMIT 3;