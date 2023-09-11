-- Database: PostgreSQL 15.3

-- Create the actors table
CREATE TABLE actors (
  actor_id SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  age DATE NOT NULL,
  number_oscars INT NOT NULL DEFAULT 0
);

-- Populate the actors table
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Matt', 'Damon', '1970-08-09', 5),
       ('George', 'Clooney', '1961-06-04', 2),
       ('Angelina', 'Jolie', '1975-06-03', 1),
       ('Jennifer', 'Aniston', '1969-02-10', 0);
