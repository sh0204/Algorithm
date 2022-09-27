SELECT HOUR(DATETIME) AS 'HOUR', COUNT(DATETIME) AS 'COUNT'
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME)<= 19
GROUP BY HOUR
ORDER BY HOUR