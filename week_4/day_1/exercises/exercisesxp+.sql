-- CREATE TABLE student (Id SERIAL PRIMARY KEY,
-- last_name VARCHAR (50), first_name VARCHAR (20),
-- birth_date DATE
-- )

-- INSERT INTO Student (first_name, last_name,birth_date )
-- VALUES ('Marc','Benichou','1998/11/02'),
--        ('Yoan','Cohen','2010/12/03'),
--        ('Lea','Benichou','1987/07/27'),
--        ('Amelia', 'Dux','1996/04/07'),
--        ('David','Grez','2003/06/14'),
--        ('Omer','Simpson','1980/10/03');

-- Fetch all of the data from the table.
SELECT * FROM student;

-- Fetch all of the students first_names and last_names.
SELECT first_name, last_name FROM student;

-- Fetch the student which id is equal to 2.
SELECT first_name, last_name FROM student WHERE id = 2;

-- Fetch the student whose last_name is Benichou AND first_name is Marc.
SELECT first_name, last_name FROM student WHERE last_name = 'Benichou' AND first_name = 'Marc';

-- Fetch the students whose last_names are Benichou OR first_names are Marc.
SELECT first_name, last_name FROM student WHERE last_name = 'Benichou' OR first_name = 'Marc';

-- Fetch the students whose first_names contain the letter a.
SELECT first_name, last_name FROM student WHERE first_name ILIKE '%a%';

-- Fetch the students whose first_names start with the letter a.
SELECT first_name, last_name FROM student WHERE first_name ILIKE 'a%';

-- Fetch the students whose first_names end with the letter a.
SELECT first_name, last_name FROM student WHERE first_name ILIKE '%a';

-- Fetch the students whose second to last letter of their first_names are a (Example: Leah).
SELECT first_name, last_name FROM student WHERE first_name ILIKE '%a_';
SELECT first_name, last_name FROM student WHERE SUBSTRING(first_name, LENGTH(first_name) - 1, 1) = 'a'; --Also works

-- Fetch the students whose id’s are equal to 1 AND 3 .
SELECT * FROM student WHERE Id  IN (1 , 3);

-- Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
SELECT * FROM Student WHERE birth_date  >= '2000/01/01';