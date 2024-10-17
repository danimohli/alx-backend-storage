-- Task: Create a stored procedure ComputeAverageScoreForUser to
-- compute and store the average score for a student.
-- ComputeAverageScoreForUser takes 1 input: user_id (linked to users table).

-- Ensure the 'users' and 'corrections' tables exist

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	UPDATE users
	SET
	average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
	WHERE id = user_id;

END $$

DELIMITER ;
