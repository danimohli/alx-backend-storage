-- Task: List all bands with Glam rock as their main style,
-- ranked by their longevity.
-- Longevity (lifespan) is calculated using the 'formed' and 'split'
-- columns, with a default year of 2022 if the band hasn't split.

-- Select bands with Glam rock as their main style and calculate their lifespan
SELECT band_name,
FROM metal_bands
WHERE style LIKE '%Glam%'
ORDER BY lifespan DESC;
