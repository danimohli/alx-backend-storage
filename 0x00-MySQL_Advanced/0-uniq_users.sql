-- Task: Create a table 'users' with specific attributes
-- (id, email, name) with certain constraints.
-- If the table already exists, the script will not fail.

-- Create the 'users' table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
