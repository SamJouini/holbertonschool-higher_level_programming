-- Switch to the MySQL database
USE mysql;

-- List privileges for user_0d_1
SELECT Host, User, Db, Table_name, Table_priv, Column_priv
FROM mysql.tables_priv
WHERE User = 'user_0d_1';

-- List privileges for user_0d_2
SELECT Host, User, Db, Table_name, Table_priv, Column_priv
FROM mysql.tables_priv
WHERE User = 'user_0d_2';