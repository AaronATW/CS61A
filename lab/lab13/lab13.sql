.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE color='blue' AND pet='dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE color='blue' AND pet='dog';


CREATE TABLE matchmaker AS
  SELECT A.pet, A.song, A.color, B.color
    FROM students AS A, students AS B
    WHERE A.pet = B.pet AND A.song = B.song AND A.time < B.time;


CREATE TABLE sevens AS
  SELECT student.seven
    FROM students AS student, numbers AS number
    WHERE student.time = number.time AND student.number = 7 AND number.'7' = 'True';


CREATE TABLE favpets AS
  SELECT pet, COUNT(*) AS count
  FROM students
  GROUP BY pet
  ORDER BY count DESC
  LIMIT 10;


CREATE TABLE dog AS
  SELECT pet, COUNT(*) FROM students WHERE pet = 'dog';


CREATE TABLE bluedog_agg AS
  SELECT song, COUNT(*) AS count
  FROM bluedog_songs
  GROUP BY song
  ORDER BY count DESC;


CREATE TABLE instructor_obedience AS
  SELECT seven, instructor, COUNT(*)
  FROM students
  WHERE seven = '7'
  GROUP BY instructor;

