-- Exe 36: Weather Observation Station 18

-- Consider P1(a,b) and P2(c,d) to be two points on a 2D plane.
-- a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
-- b happens to equal the minimum value in Western Longitude (LONG_W in STATION).
-- c happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
-- d happens to equal the maximum value in Western Longitude (LONG_W in STATION).
-- Query the Manhattan Distance between points P1 and P2 and round it to a scale of 4 decimal places.

select round(abs(max(lat_n) - min(lat_n)) + abs(max(long_w) - min(long_w)), 4)
from station



-- Exe 37: Weather Observation Station 19

-- Consider P1(a,c) and P2(b,d) to be two points on a 2D plane where (a,b) are the respective minimum and maximum values of Northern Latitude (LAT_N) and (c,d) are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.
-- Query the Euclidean Distance between points  and  and format your answer to display  decimal digits.

select round(sqrt(power(max(long_w) - min(long_w), 2) + power(max(lat_n) -min(lat_n), 2)), 4)
from station;


-- Exe 38: Weather Observation Station 20
-- A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to 4 decimal places.


with temporary_table_1 as (
    select round(lat_n, 4) as dec_lat_n, ROW_NUMBER() over(ORDER BY lat_n) as rank_number
    from station
    order by lat_n asc
)
, temporary_table_2  as (
    select((count( * ) / 2) + 0.5) as total from station
)

select dec_lat_n from temporary_table_1
where rank_number = (select total from temporary_table_2)


-- Exe 39: Population Census
-- Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

select sum(ci.population)
from country co inner join city ci
    on co.code = ci.countrycode
where CONTINENT = 'Asia'



-- Exe 40: African Cities
-- Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.

select ci.name
from country co inner join city ci
    on co.code = ci.countrycode
where CONTINENT = 'Africa'


-- Exe 41: Average Population of Each Continent
-- Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.

select co.continent, floor(avg(ci.population))
from country co inner join city ci
    on co.code = ci.countrycode
group by co.continent;
