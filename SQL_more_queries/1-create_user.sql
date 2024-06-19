-- -- Creates the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant privileges to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';