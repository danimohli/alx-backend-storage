-- Task: Create a stored procedure ComputeAverageWeightedScoreForUsers that computes and stores the average weighted score for all students.

-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- Create the procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;  -- Declare a flag for the loop
    DECLARE user_id INT;         -- Variable to store user ID during iteration
    DECLARE weighted_average DECIMAL(10, 2);  -- Variable to store the weighted average score
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;  -- Cursor to iterate through all users
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;  -- Handler to exit the loop when no more rows are found

    -- Open the cursor to go through each user
    OPEN user_cursor;

    read_loop: LOOP
        -- Fetch the next user ID from the cursor
        FETCH user_cursor INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Compute the weighted average score for the current user
        SELECT 
            SUM(score * weight) / SUM(weight) INTO weighted_average
        FROM 
            scores
        WHERE 
            scores.user_id = user_id;

        -- Store the weighted average in the users table (assuming users table has an avg_weighted_score column)
        UPDATE users
        SET avg_weighted_score = IFNULL(weighted_average, 0)  -- If the weighted average is NULL, store 0
        WHERE id = user_id;
        
    END LOOP;

    -- Close the cursor after the loop ends
    CLOSE user_cursor;

END //

DELIMITER ;
