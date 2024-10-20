-- Task: Rank the country origins of bands based on the total number of
-- non-unique fans.
-- The result will be ordered by the total number of fans in descending order.

-- Select country origins and the total number of fans
SELECT origin, SUM(fans) as nb_fans FROM metal_bands
GROUP BY origin ORDER BY nb_fans DESC;
