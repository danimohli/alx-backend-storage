-- Task: Create a trigger that resets the 'valid_email' attribute only when the 'email' has been changed.

-- Create the trigger
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
