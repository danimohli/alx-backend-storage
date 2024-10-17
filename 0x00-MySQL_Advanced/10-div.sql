-- Task: Create a function SafeDiv that divides the first number by the second and returns 0 if the second number is 0.

-- Drop the function if it already exists
DROP FUNCTION IF EXISTS SafeDiv;

-- Create the SafeDiv function
DELIMITER //

CREATE FUNCTION SafeDiv(
    a INT,
    b INT
)
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    -- Check if the denominator is zero, return 0 in that case
    IF b = 0 THEN
        RETURN 0;
    ELSE
        -- Otherwise, perform the division
        RETURN a / b;
    END IF;
END //

DELIMITER ;
