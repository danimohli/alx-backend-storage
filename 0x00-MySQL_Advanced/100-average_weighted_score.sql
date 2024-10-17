-- Task: Create a stored procedure ComputeAverageWeightedScoreForUser that computes and stores the average weighted score for a student.

-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- Create the procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
BEGIN
    DECLARE weighted_average DECIMAL(10, 2);
    -- Compute the weighted average score for the given user
    SELECT 
        SUM(score * weight) / SUM(weight) INTO weighted_average
    FROM 
        scores
    WHERE 
        scores.user_id = user_id;

    -- Store the weighted average in the users table
    -- (assuming users table has an avg_weighted_score column)
    UPDATE users
    SET avg_weighted_score = weighted_average
    WHERE id = user_id;

END //

DELIMITER ;
