# Study Notes for SQL (MySQL)

## Types of DBMS

1. RDBMS(Relational DBMS)
-- MySQL  
-- Oracle
-- PostgreSQL
-- SQL Server
2. NRDBMS
-- MogoDB
-- Redis
-- DynamoDB

## Create and Delete a Database  

```sql
-- create
CREATE DATABASE name;
CREATE DATABASE `name`;  -- use `` to avoid the conflict of keywords

-- show and choose databases
SHOW DATABASES;

-- delete
DROP DATABASE <name>;
```

## Types of the Data

```sql
INT
FLOAT
DOUBLE
DECIMAL(m, n)
VARCHAR(n)  
BLOB  -- Binary Large Object
DATE  -- 'YYYY-MM-DD'
TIMESTAMP  -- 'YYYY-MM-DD HH:MM:SS'
```

## Operate Table

### Create & Delete

```sql
USE `name`;

-- create table
-- way 1
CREATE TABLE `student`(
    `student_id` INT PRIMARY KEY,
    `name` VARCHAR(20),
    `major` VARCHAR(20)
);

-- way 2
CREATE TABLE `student`(
    `student_id` INT,
    PRIMARY KEY(`student_id`)
);

-- delete 
DESCRIBE `student`;
DROP TABLE `student`;
```

### Create with Constrains

All Constrains may used are listed below.

```sql
AUTO_INCREMENT
NOT NULL
UNIQUE
PRIMARY KEY
DEFAULT
CHECK
```

```sql
CREATE TABLE `student`(
    `student_id` INT AUTO_INCREMENT,
    `name` VARCHAR(20) NOT NULL,
    `major` VARCHAR(20) UNIQUE,
    PRIMARY KEY(`student_id`)
);
```

### Alter Table

```sql
-- change column
ALTER TABLE `student` ADD `gpa` DECIMAL(3, 2);
ALTER TABLE `student` DROP `gpa`;
ALTER TABLE `student` MODIFY 'student_id' INT AUTO_INCREMENT;

ALTER TABLE `student`
ADD FOREIGN KEY(`teacher_id`) 
REFERENCES `teacher`(`teacher_id`)
ON DELETE SET NULL;
```

## Operate Data

### Insert into

```sql
INSERT INTO `student` VALUES(1, 'Jack', 'History', NULL);
INSERT INTO `student` (`name`, `major`, `student_id`) 
VALUES('jack', 'history', 1);
```

### Update  

```sql
UPDATE `student` 
SET `major` = 'English', `gpa` = 3.99
WHERE `student_id` = 3 OR `student_id` = 1;
```

### Delete  

```sql
DELETE FROM `student`
WHERE `student_id` = 3;
```

### Query  

```sql
SELECT * FROM `student`;

SELECT `name`, `major` 
FROM `student` 
WHERE `major` = 'English' OR `score` <> 70  -- <> means not equal
ORDER BY `gpa` ASC  -- ASC:ascend DESC: descend
LIMIT 5;

SELECT * FROM `student`
WHERE `major` IN('English', 'History'); 
```
