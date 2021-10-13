-- Exe 20: The PADS

-- + Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a
--   parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
-- + Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the
--   following format:
-- 		There are a total of [occupation_count] [occupation]s.


	select concat(name,'(', left(occupation,1),')') from occupations order by name;

	select concat("There are a total of ", count(occupation), " ", LOWER(occupation), "s.") from occupations group by occupation order
	by count(occupation), occupation asc;


-- Exe 21: Occupations

-- Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation.
-- The output column headers should be Doctor, Professor, Singer, and Actor, respectively.


	select min(Doctor), min(Professor), min(Singer), min(Actor) from(
		select
			case when Occupation = 'Doctor' then Name end as Doctor,
			case when Occupation = 'Actor' then Name  end as Actor,
			case when Occupation = 'Singer' then Name  end as Singer,
			case when Occupation = 'Professor' then Name end as Professor,
			ROW_NUMBER() OVER( PARTITION by Occupation order by name) as TT
		from OCCUPATIONS
	) as TB
	group by TT




-- Exe 22: Binary Tree Nodes

-- You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.
-- Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:
	-- Root: If node is root node.
	-- Leaf: If node is leaf node.
	-- Inner: If node is neither root nor leaf node.

	select 
	case
		when p is null then concat(n, ' Root')
		when n in (select distinct p from BST) then concat(n, ' Inner')
		else concat(n, ' Leaf')
	end
	from BST
	order by n asc


-- Exe 23: New Companies


	select c.company_code, c.founder, count(distinct lm.lead_manager_code), 
	count(distinct sm.senior_manager_code), count(distinct m.manager_code), 
	count(distinct e.employee_code)

	from Company c, Lead_Manager lm, Senior_Manager sm, Manager m, Employee e
	where c.company_code = lm.company_code
		and lm.lead_manager_code = sm.lead_manager_code
		and sm.senior_manager_code = m.senior_manager_code
		and m.manager_code = e.manager_code
	group by c.company_code, c.founder
	order by c.company_code



-- Exe 22: Revising Aggregations - The Count Function

-- Query a count of the number of cities in CITY having a Population larger than .

	select count(id) from city
	where population > 100000;


-- Exe 23: Revising Aggregations - The Sum Function

-- Query the total population of all cities in CITY where District is California.

	select sum(population) from city
	where District = 'California';


-- Exe 24: Revising Aggregations - Averages

-- Query the average population of all cities in CITY where District is California.

	select avg(population) from city 
	where district = 'California';


-- Exe 25: Average Population
-- Query the average population for all cities in CITY, rounded down to the nearest integer.

	select round(avg(population)) from city;


-- Exe 26: Japan Population
-- Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.

	select sum(population) from city
	where COUNTRYCODE = 'JPN';


-- Exe 27: Population Density Difference
-- Query the difference between the maximum and minimum populations in CITY.

	select max(population)-min(population) from CITY;

-- Exe 28: The Blunder

-- Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's  
-- key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.
-- Write a query calculating the amount of error (i.e.: actual - miscalculated  average monthly salaries), and round it up to the next integer.
	
	select ceil(avg(Salary) - avg(replace(Salary,'0',''))) from employees;


-- Exe 29: Top Earners

-- We define an employee's total earnings to be their monthly salary x months worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. 
-- Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as  space-separated integers.

	select (salary * months) as earnings, count(employee_id) 
	from employee 
	group by earnings 
	order by earnings desc 
	limit 1;

-- Exe 30: Weather Observation Station 2

-- Query the following two values from the STATION table:
-- 1. The sum of all values in LAT_N rounded to a scale of 2 decimal places.
-- 2. The sum of all values in LONG_W rounded to a scale of 2 decimal places.

	select round(sum(lat_n),2), round(sum(long_w),2) from station;

-- Exe 31: Weather Observation Station 13
-- Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7880 and less than 137,2345 . Truncate your answer to 4 decimal places.

	select round(sum(lat_n),4) from station
	where lat_n between 38.7880 and 137.2345

-- Exe 32: Weather Observation Station 14
-- Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137,2345. Truncate your answer to 4 decimal places.

	select round(max(lat_n),4) from station
	where lat_n < 137.2345;


-- Exe 33: Weather Observation Station 15
-- Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137,2345. Round your answer to 4 decimal places.

	select round(long_w,4) from station
	where lat_n < 137.2345
	order by lat_n desc
	limit 1;


-- Exe 34: Weather Observation Station 16
-- Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7780. Round your answer to  decimal places.


	select round(lat_n,4) from station
	where lat_n > 38.7780
	order by lat_n asc
	limit 1;
-- Exe 35: Weather Observation Station 17
-- Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than 38.7780. Round your answer to 4 decimal places.

	select round(LONG_W,4) from station
    where lat_n > 38.7780
    order by lat_n asc
    limit 1;