-- Script that converts hbtn_0c_0 database to UTF8(utf8mb4, collate utf8mb4_unicode_ci)
-- Convert Database hbtn_0c_0, Table first_table and field name in first_table to UTF8
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;