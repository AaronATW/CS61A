CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size
  FROM dogs, sizes
  WHERE height > min AND height <= max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child
  FROM parents, dogs
  WHERE parent = name
  ORDER BY height DESC;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT old.child AS first, young.child AS second, first_size_table.size AS sibling_size
  FROM parents AS old, parents AS young, size_of_dogs AS first_size_table, size_of_dogs AS second_size_table
  WHERE old.parent = young.parent AND first < second AND first = first_size_table.name AND second = second_size_table.name AND sibling_size = second_size_table.size
  ORDER BY first;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT first || ' and ' || second || ' are ' || sibling_size || ' siblings'
  FROM siblings;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height, n);
-- Add your INSERT INTOs here
INSERT INTO stacks_helper SELECT name, height, height, 1 FROM dogs;
INSERT INTO stacks_helper SELECT dogs || ', ' || name, stack_height + height, height, 2 FROM stacks_helper, dogs WHERE height > last_height AND n = 1; 
INSERT INTO stacks_helper SELECT dogs || ', ' || name, stack_height + height, height, 3 FROM stacks_helper, dogs WHERE height > last_height AND n = 2; 
INSERT INTO stacks_helper SELECT dogs || ', ' || name, stack_height + height, height, 4 FROM stacks_helper, dogs WHERE height > last_height AND n = 3; 

CREATE TABLE stacks AS
  SELECT dogs, stack_height FROM stacks_helper WHERE n = 4 AND stack_height >= 170 ORDER BY stack_height;

