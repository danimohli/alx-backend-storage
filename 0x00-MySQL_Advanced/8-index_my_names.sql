-- Task: Create an index idx_name_first on the first letter of the 'name' column in the 'names' table.

-- Ensure the 'names' table exists (this would be based on the imported dump from names.sql.zip)

CREATE TABLE IF NOT EXISTS names (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create an index on the first letter of the 'name' column
CREATE INDEX idx_name_first ON names (SUBSTRING(name, 1, 1));
