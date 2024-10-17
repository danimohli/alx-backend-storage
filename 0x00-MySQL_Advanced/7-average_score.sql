-- Task: Create a stored procedure ComputeAverageScoreForUser to
-- compute and store the average score for a student.
-- ComputeAverageScoreForUser takes 1 input: user_id (linked to users table).

-- Ensure the 'users' and 'corrections' tables exist

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Corrections table
CREATE TABLE IF NOT EXISTS corrections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    project_id INT NOT NULL,
    score DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Table to store average scores
CREATE TABLE IF NOT EXISTS user_average_scores (
    user_id INT PRIMARY KEY,
    average_score DECIMAL(5,2),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Create the stored procedure ComputeAverageScoreForUser
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN input_user_id INT   -- Input: user_id (linked to users table)
)
BEGIN
    DECLARE avg_score DECIMAL(5,2);

    -- Compute the average score for the user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = input_user_id;

    -- Check if the user already has an average score stored
    IF EXISTS (SELECT 1 FROM user_average_scores WHERE user_id = input_user_id) THEN
        -- Update the existing average score
        UPDATE user_average_scores
        SET average_score = avg_score
        WHERE user_id = input_user_id;
    ELSE
        -- Insert a new record for the user's average score
        INSERT INTO user_average_scores (user_id, average_score)
        VALUES (input_user_id, avg_score);
    END IF;
END //

DELIMITER ;
