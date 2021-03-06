-- REVIEW chung:
-- Tương tự bên javascript
-- Mỗi mệnh đề em cứ xuống dòng cho dễ nhìn. VD: SELECT 1 dòng, FROM 1 dòng, WHERE 1 dòng

-- Exe 1: Revising the Select Query I
-- Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.

-- REVIEW: cần thêm 1 dấu cách vào 2 đầu mỗi toán tử
-- VD: population > 100000, countrycode = 'USA'
-- Sửa tương tự cho bên dưới
select * from city
where population > 100000 and countrycode = 'USA';


-- Exe 2: Revising the Select Query II
-- Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is 	USA.

select t.name from city t
where t.population > 120000 and t.CountryCode = 'USA';

-- Exe 3: Select By ID
-- Query all columns for a city in CITY with the ID 1661.

select * from city
where id =1661;


-- Exe 4: Japanese Cities' Attributes
-- Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.

select * from city
where COUNTRYCODE = 'JPN';

-- Exe 5: Japanese Cities' Names
-- Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.

select name from city
where COUNTRYCODE = 'JPN';


-- Exe 6: Weather Observation Station 1
-- Query a list of CITY and STATE from the STATION table.
select CITY, STATE from STATION;


-- Exe 7: Weather Observation Station 3
-- Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude
-- duplicates from the answer.

SELECT DISTINCT CITY FROM STATION
WHERE ID % 2 = 0;


-- Exe 8: Weather Observation Station 4
-- Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.

-- REVIEW: câu này nên tách dòng cho dễ đọc
select count(city) - ( select count(DISTINCT city) from station) from station

-- Exe 9: Weather Observation Station 5
-- Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of 		characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered
-- alphabetically.

-- REVIEW: nên dùng "LIMIT 1" thay cho "SELECT TOP 1"
-- Dùng hàm CHAR_LENGTH() thay cho LEN()
select top 1 city, len(city) from station
order by  len(city) , city asc;

select top 1 city, len(city) from station
order by  len(city) desc , city asc;

-- Exe 10: Weather Observation Station 6
-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

select city from station
where city like 'a%' or city like 'e%' or city like 'u%' or city like 'i%' or city like 'o%';

-- Exe 11: Weather Observation Station 7
-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

select distinct city from station
where city like '%a' or city like '%e' or city like '%u' or city like '%i' or city like '%o';

-- Exe 12: Weather Observation Station 8
-- Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your
-- result cannot contain duplicates.

select distinct city from station
where city like '[a,e,i,o,a,u]%[a,e,i,o,a,u]'

-- Exe 13: Weather Observation Station 9
-- Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

select distinct city from station
where left(city, 1) not in ('a', 'e', 'i', 'o', 'u');

-- Exe 14: Weather Observation Station 10
-- Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.

select distinct city from station
where right(city, 1) not in ('a', 'e', 'i', 'o', 'u');


-- Exe 15: Weather Observation Station 11
-- Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot
-- contain duplicates.

select distinct city from station
where left(city, 1) not in ('a', 'e', 'i', 'o', 'u') or right(city, 1) not in ('a', 'e', 'i', 'o', 'u');

-- Exe 16: Weather Observation Station 12
-- Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain
-- duplicates.

select distinct city from station
where left(city,1) not in ('a','e','i','o','u') and  right(city,1) not in ('a','e','i','o','u');


-- Exe 17: Higher Than 75 Marks
-- Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each
-- name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort
-- them by ascending ID.

select name from students where marks > 75 order by right( name , 3 ) asc, id asc;



-- Exe 18 : Employee Salaries.
-- Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater
-- than $2000 per month who have been employees for less than 10 months. Sort your result by ascending employee_id.

select name from employee
where salary > 2000 and months < 10 order by employee_id asc;


-- Exe 19 :Type of Triangle:
-- Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following
-- statements for each record in the table:
-- Equilateral: It's a triangle with 3 sides of equal length.
-- Isosceles: It's a triangle with 2 sides of equal length.
-- Scalene: It's a triangle with 3 sides of differing lengths.
-- Not A Triangle: The given values of A, B, and C don't form a triangle.

select
	case
	when a >= ( b + c ) or b >= ( a + c ) or c >= ( a + b ) then 'Not A Triangle'
	when a = b and a = c then 'Equilateral'
	when a = b or b = c or a = c then 'Isosceles'
	else 'Scalene'
	end
from triangles;
