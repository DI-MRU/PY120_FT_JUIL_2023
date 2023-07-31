CREATE TABLE IF NOT EXISTS class (
	id SERIAL PRIMARY KEY,
	label CHAR(30) NOT NULL,
	code CHAR(10) UNIQUE,
	year DATE DEFAULT NOW()
);

-- DROP TABLE class;

-- INSERT INTO class (label, code) VALUES
-- ('This is a test', 'A'),
-- ('Python Full time July 2023', 'B'),
-- ('Python Full time July 2023', 'C')
-- ;

-- INSERT INTO class (id, label) VALUES
-- (100, 'Vincent');

-- InSeRT into class (label) VALUES
-- ('Onyeka'),
-- ('Deji'),
-- ('Laeticia'),
-- ('Anas'),
-- ('Borel'),
-- ('Himanish')
-- RETURNING label, year;

-- SELECT id, label, code FROM class;

-- SELECT id, label FROM class
-- WHERE label='Laeticia';

-- SELECT * FROM class
-- WHERE code IS NULL;

-- SELECT * FROM class
-- WHERE code IS NOT NULL;


-- SELECT id, label FROM class
-- WHERE label<>'Laeticia';

-- SELECT id, label FROM class
-- WHERE label!='Laeticia';

-- SELECT * FROM class
-- WHERE id>50
-- ORDER BY id DESC;

-- SELECT * FROM class
-- WHERE id>=80 OR label='Himanish'
-- LIMIT 10
-- OFFSET 15;

-- SELECT * FROM class
-- WHERE label LIKE '___s%';

-- SELECT * FROM class
-- WHERE label ILIKE '%J%';

-- SELECT COUNT(*) FROM class;

-- SELECT * FROM class
-- WHERE label = 'Vincent';

-- UPDATE class
-- SET label = 'Vincenzo'
-- WHERE label = 'Vincent';

-- SELECT * FROM class
-- WHERE label = 'Vincent';

-- SELECT * FROM class
-- WHERE label = 'Laeticia';

-- UPDATE class
-- SET code = 'XYZ'
-- WHERE id = 90;

-- SELECT * FROM class
-- WHERE label = 'Laeticia';


-- UPDATE class
-- SET code = 'LOL'
-- WHERE label = 'Laeticia' AND code IS NULL AND id = 42;


-- SELECT * FROM class
-- WHERE label = 'Laeticia';

-- SELECT * FROM class
-- WHERE label = 'Borel';

-- DELETE FROM CLASS
-- WHERE id = 111
-- RETURNING *;

-- SELECT * FROM class
-- WHERE label = 'Borel';

-- ALTER TABLE class
-- ALTER COLUMN label TYPE VARCHAR(100);

-- INSERT inTO claSS
-- (label)
-- VALUES
-- ('kjjhdfjkhgjdshrgoyoesvitueni4tleistmhlesrhtmsvrjlkt');

SELECT 
id,
label AS "Class name",
code,
year
FROM class;
