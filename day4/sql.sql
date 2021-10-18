-- Exe 46: Contest Leaderboard

-- The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score.
-- If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. Exclude all hackers with a total score of 0 from your result.

SELECT
    HACKER_ID,
    NAME,
    SUM(SCORE)
FROM (
    SELECT
        H.HACKER_ID
        H.NAME
        S.CHALLENGE_ID
        MAX(S.SCORE) AS SCORE
    FROM HACKERS H
        INNER JOIN SUBMISSIONS S ON H.HACKER_ID = S.HACKER_ID
    WHERE S.SCORE > 0
    GROUP BY H.HACKER_ID, S.CHALLENGE_ID, H.NAME
) AS TEMP_TABLE
GROUP BY HACKER_ID, NAME
ORDER BY SUM(SCORE) DESC, HACKER_ID




-- Exe 47: Placements

-- Write a query to output the names of those students whose best friends got offered a higher salary than them. Names must be ordered by the salary amount offered to the best friends.
-- It is guaranteed that no two students got same salary offer.


SELECT
    S.NAME
FROM STUDENTS S
    INNER JOIN PACKAGES P ON S.ID = P.ID
    INNER JOIN FRIENDS F ON S.ID = F.ID
    INNER JOIN PACKAGES P1 ON F.FRIEND_ID = P1.ID
WHERE P.SALARY < P1.SALARY
ORDER BY P1.SALARY



-- Exe 48:Symmetric Pairs

-- Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.
-- Write a query to output all such symmetric pairs in ascending order by the value of X. List the rows such that X1 ≤ Y1.

SELECT F1.X, F1.Y
FROM FUNCTIONS F1
    JOIN FUNCTIONS F2 ON F1.X=F2.Y AND F1.Y=F2.X
GROUP BY F1.X, F1.Y
HAVING F1.X < F1.Y OR COUNT(F1.X) > 1
ORDER BY F1.X


-- e đếm nhầm 2 lần câu 22, 23