-- Task: Create an index idx_name_first_score on the first letter of 'name' and 'score' in the 'names' table.

-- Ensure the 'names' table exists (based on the imported dump from names.sql.zi
CREATE TABLE IF NOT EXISTS names (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    score INT NOT NULL
);

-- Create an index on the first letter of 'name' and 'score'
CREATE INDEX idx_name_first_score ON names(name(1), score);
