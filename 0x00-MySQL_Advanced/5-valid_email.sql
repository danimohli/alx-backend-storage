-- Task: Create a trigger that resets the 'valid_email' attribute when the 'email' has been changed.
-- This ensures that email validation will need to be redone after an email update.

-- Ensure that the 'users' table has the necessary fields
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    valid_email TINYINT(1) DEFAULT 0,
    name VARCHAR(255)
);

-- Create the trigger to reset 'valid_email' when 'email' changes
DELIMITER $$ ;
CREATE TRIGGER resets_valid_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END;
DELIMITER ;
