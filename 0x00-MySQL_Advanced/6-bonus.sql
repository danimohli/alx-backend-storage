-- Task: Create a stored procedure AddBonus to add a new correction for a student.
-- AddBonus takes 3 inputs: user_id, project_name, and score.

-- Ensure the 'users', 'projects', and 'corrections' tables exist

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

-- Corrections table
CREATE TABLE IF NOT EXISTS corrections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    project_id INT NOT NULL,
    score DECIMAL(5,2) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS AddBonus;

-- Create the stored procedure AddBonus
DELIMITER //

CREATE PROCEDURE AddBonus(
    IN input_user_id INT,
    IN input_project_name VARCHAR(255),
    IN input_score DECIMAL(5,2)
)
BEGIN
    DECLARE project_id INT;

    -- Check if the project already exists
    SELECT id INTO project_id
    FROM projects
    WHERE name = input_project_name;

    -- If project does not exist, create it
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (input_project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the correction into the corrections table
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (input_user_id, project_id, input_score);
END //

DELIMITER ;

