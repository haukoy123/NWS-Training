-- Exe 42: The Report

-- Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. Ketty doesn't want the NAMES of those students who received a grade lower than 8.
-- The report must be in descending order by grade -- i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them,
-- order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order.
-- If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

SELECT
    CASE
        WHEN G.GRADE < 8
        THEN NULL
        ELSE S.NAME  -- REVIEW: thêm tên bảng. VD: "S.NAME"
    END AS NAME,  -- REVIEW: nên thêm alias. VD: "AS NAME"
    G.GRADE,
    S.MARKS
FROM STUDENTS S, GRADES G
WHERE S.MARKS BETWEEN G.MIN_MARK AND G.MAX_MARK
ORDER BY G.GRADE DESC, S.NAME



-- EXE 43: Top Competitors

-- Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! Write a query to print the respective hacker_id and name of hackers
-- who achieved full scores for more than one challenge. Order your output in descending order by the total number of challenges in which the hacker earned a full score.
-- If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.


SELECT
    HACKER_ID,
    NAME
FROM (
    SELECT
        H.HACKER_ID,
        H.NAME,
        COUNT(H.HACKER_ID) AS DEM
    FROM HACKERS H
        INNER JOIN SUBMISSIONS S ON H.HACKER_ID = S.HACKER_ID
        INNER JOIN CHALLENGES C ON S.CHALLENGE_ID = C.CHALLENGE_ID
        INNER JOIN DIFFICULTY D ON C.DIFFICULTY_LEVEL = D.DIFFICULTY_LEVEL
    WHERE S.SCORE = D.SCORE
    GROUP BY H.HACKER_ID, H.NAME
) AS TEMPORARY_TABLE
WHERE DEM >= 2
ORDER BY DEM DESC, HACKER_ID






-- Exe 44: Ollivander's Inventory

-- Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.

-- Hermione decides the best way to choose is by determining the minimum number of gold galleons needed
-- to buy each non-evil wand of high power and age. Write a query to print the id, age, coins_needed,
-- and power of the wands that Ron's interested in, sorted in order of descending power.
-- If more than one wand has same power, sort the result in order of descending age.

SELECT
    W.ID,
    WP.AGE,
    W.COINS_NEEDED,
    W.POWER
FROM WANDS W
    INNER JOIN WANDS_PROPERTY WP ON W.CODE = WP.CODE
WHERE W.COINS_NEEDED = (SELECT MIN(coins_needed)
                        FROM WANDS AS W1
                            INNER JOIN WANDS_PROPERTY AS WP1 ON W1.code = WP1.code
                        WHERE W1.power = W.power AND WP1.age = WP.age AND WP.IS_EVIL = 0 )
ORDER BY W.POWER DESC, WP.AGE DESC






-- Exe 45: Challenges

-- Julia asked her students to create some coding challenges. Write a query to print the hacker_id, name, and the total number of challenges created by each student.
--  Sort your results by the total number of challenges in descending order. If more than one student created the same number of challenges, then sort the result by hacker_id.
--  If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.


SELECT * FROM (
    SELECT
        H.HACKER_ID,
        H.NAME,
        COUNT(H.HACKER_ID) AS CHALLENGES_CREATED
    FROM HACKERS H
        INNER JOIN CHALLENGES C ON H.HACKER_ID = C.HACKER_ID
    GROUP BY H.HACKER_ID, H.NAME
) AS TEMP_TABLE
WHERE CHALLENGES_CREATED IN (
    SELECT CHALLENGES_CREATED_1 FROM (
        SELECT
            CHALLENGES_CREATED_1,
            COUNT(CHALLENGES_CREATED_1) AS REPEAT_1
        FROM
        (
            SELECT
                H1.HACKER_ID, H1.NAME,
                COUNT(H1.HACKER_ID) AS CHALLENGES_CREATED_1
            FROM HACKERS H1
                INNER JOIN CHALLENGES C1 ON H1.HACKER_ID = C1.HACKER_ID
            GROUP BY H1.HACKER_ID, H1.NAME
        ) AS TEMP_TABLE_1
        GROUP BY CHALLENGES_CREATED_1
        HAVING
            REPEAT_1 = 1
            OR
            CHALLENGES_CREATED_1 = (
                SELECT COUNT(HACKER_ID)
                FROM CHALLENGES
                GROUP BY HACKER_ID
                ORDER BY COUNT(HACKER_ID) DESC
                LIMIT 1
            )
    ) AS TEMP_TABLE_2
)
ORDER BY CHALLENGES_CREATED DESC, HACKER_ID
