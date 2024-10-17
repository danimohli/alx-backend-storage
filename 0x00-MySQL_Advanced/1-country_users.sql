-- Task: Create a table 'users' with attributes
-- (id, email, name, country) including constraints.
-- The 'country' field is an enumeration (US, CO, TN)
-- with a default value of 'US'.
-- If the table already exists, the script will not fail.

-- Create the 'users' table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
