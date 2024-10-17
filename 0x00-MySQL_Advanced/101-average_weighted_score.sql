-- Task: Create a stored procedure ComputeAverageWeightedScoreForUsers that computes and stores the average weighted score for all students.

DELIMITER $$
-- The procedure if not alrea exists
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE total_score DECIMAL(10, 2);
    DECLARE total_weight DECIMAL(10, 2);
    DECLARE average_weighted_score DECIMAL(10, 2);

    -- Iterate over all users
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;

    -- Declare a cursor for all users
    DECLARE cur CURSOR FOR
        SELECT id FROM users;

    -- Declare a handler to set 'done' when the cursor is finished
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    -- Open the cursor
    OPEN cur;

    -- Iterate through each user
    read_loop: LOOP
        -- Fetch the next user ID
        FETCH cur INTO user_id;

        -- If no more rows, exit the loop
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Initialize the total score and weight
        SET total_score = 0;
        SET total_weight = 0;

        -- Calculate the total score and weight for each project for this user
        SELECT SUM(score * weight), SUM(weight)
        INTO total_score, total_weight
        FROM corrections
        INNER JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = user_id;

        -- Calculate the average weighted score for this user
        IF total_weight > 0 THEN
            SET average_weighted_score = total_score / total_weight;
        ELSE
            SET average_weighted_score = 0;
        END IF;

        -- Update the average weighted score for the user
        UPDATE users
        SET average_weighted_score = average_weighted_score
        WHERE id = user_id;

    END LOOP;

    -- Close the cursor
    CLOSE cur;
END $$

DELIMITER ;
