-- ============================================================
-- DAY 5 - MYSQL DATABASE PRACTICE
-- Backend Development Practice
-- Project: IdleSpace
-- ============================================================


-- ============================================================
-- TASK 1 — CREATE DATABASE
-- ============================================================

CREATE DATABASE IF NOT EXISTS backend_practice;

USE backend_practice;


-- ============================================================
-- TASK 2 — CREATE USERS TABLE
-- ============================================================

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- ============================================================
-- TASK 3 — INSERT 10 USERS
-- ============================================================

INSERT INTO users (name, email, age) VALUES
('Arslaan Ahmad', 'arslaan@gmail.com', 21),
('Arshi', 'arshi@gmail.com', 20),
('Adarsh Raj', 'adarsh@gmail.com', 20),
('Rahul Sharma', 'rahul@gmail.com', 23),
('Priya Singh', 'priya@gmail.com', 19),
('Mohammad Sahil', 'sahil@gmail.com', 22),
('Aman Verma', 'aman@gmail.com', 24),
('Neha Gupta', 'neha@gmail.com', 21),
('Rohan Mehta', 'rohan@gmail.com', 26),
('Sneha Kapoor', 'sneha@gmail.com', 18);


-- Verify users
SELECT * FROM users;


-- ============================================================
-- TASK 4 — SELECT PRACTICE
-- ============================================================

-- 1. Get all users
SELECT * FROM users;


-- 2. Get only name and email
SELECT name, email
FROM users;


-- 3. Get users older than 20
SELECT *
FROM users
WHERE age > 20;


-- 4. Get users whose name starts with A
SELECT *
FROM users
WHERE name LIKE 'A%';


-- 5. Get users between ages 18 and 25
SELECT *
FROM users
WHERE age BETWEEN 18 AND 25;


-- ============================================================
-- TASK 5 — UPDATE PRACTICE
-- ============================================================

-- Change one user's name
UPDATE users
SET name = 'Arslaan Ahmad Khan'
WHERE id = 1;


-- Change another user's age
UPDATE users
SET age = 25
WHERE id = 4;


-- Verify changes
SELECT * FROM users;


-- ============================================================
-- TASK 6 — DELETE PRACTICE
-- ============================================================

-- Delete one user
DELETE FROM users
WHERE id = 10;


-- Verify that the user is deleted
SELECT * FROM users;


-- ============================================================
-- TASK 7 — CREATE PRODUCTS TABLE
-- ============================================================

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10,2),
    category VARCHAR(50),
    stock INT
);


-- Insert 10 realistic products
INSERT INTO products
(name, description, price, category, stock)
VALUES
('Dell Inspiron 15',
 '15-inch laptop for everyday computing',
 54999.00,
 'Electronics',
 12),

('Logitech K380 Keyboard',
 'Wireless compact keyboard',
 2999.00,
 'Electronics',
 25),

('Samsung 24 Inch Monitor',
 'Full HD LED monitor',
 12999.00,
 'Electronics',
 8),

('HP Wireless Mouse',
 'Wireless optical mouse',
 899.00,
 'Electronics',
 40),

('College Backpack',
 'Water-resistant laptop backpack',
 1499.00,
 'Accessories',
 30),

('Office Chair',
 'Ergonomic office chair',
 8999.00,
 'Furniture',
 15),

('Study Table',
 'Wooden study and computer table',
 6999.00,
 'Furniture',
 7),

('USB-C Hub',
 'Multi-port USB-C connectivity hub',
 2499.00,
 'Electronics',
 18),

('Notebook Set',
 'Set of five ruled notebooks',
 499.00,
 'Stationery',
 50),

('Desk Lamp',
 'LED adjustable desk lamp',
 1799.00,
 'Electronics',
 22);


-- Verify products
SELECT * FROM products;


-- ============================================================
-- TASK 8 — PRODUCT QUERIES
-- ============================================================

-- 1. Products cheaper than 50,000
SELECT *
FROM products
WHERE price < 50000;


-- 2. Products with stock greater than 10
SELECT *
FROM products
WHERE stock > 10;


-- 3. Electronics only
SELECT *
FROM products
WHERE category = 'Electronics';


-- 4. Cheapest products first
SELECT *
FROM products
ORDER BY price ASC;


-- 5. Get top 5 cheapest products
SELECT *
FROM products
ORDER BY price ASC
LIMIT 5;


-- ============================================================
-- TASK 9 — IDLESPACE DATABASE DESIGN
-- ============================================================

-- USERS table already exists from Task 2.


-- Create SPACES table
CREATE TABLE spaces (
    id INT PRIMARY KEY AUTO_INCREMENT,
    owner_id INT NOT NULL,
    name VARCHAR(150) NOT NULL,
    location VARCHAR(255) NOT NULL,
    price_per_hour DECIMAL(10,2) NOT NULL,
    capacity INT NOT NULL,

    FOREIGN KEY (owner_id)
    REFERENCES users(id)
);


-- Create BOOKINGS table
CREATE TABLE bookings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    space_id INT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    status VARCHAR(30) DEFAULT 'pending',

    FOREIGN KEY (user_id)
    REFERENCES users(id),

    FOREIGN KEY (space_id)
    REFERENCES spaces(id)
);


-- ============================================================
-- INSERT SAMPLE SPACES
-- ============================================================

INSERT INTO spaces
(owner_id, name, location, price_per_hour, capacity)
VALUES
(1, 'Premium Meeting Room',
 'Gomti Nagar, Lucknow',
 800.00,
 10),

(2, 'Creative Workspace',
 'Hazratganj, Lucknow',
 500.00,
 6),

(3, 'Conference Hall',
 'Indira Nagar, Lucknow',
 1500.00,
 30),

(4, 'Photography Studio',
 'Aliganj, Lucknow',
 1000.00,
 8),

(5, 'Small Office Space',
 'Vibhuti Khand, Lucknow',
 700.00,
 5);


-- ============================================================
-- INSERT SAMPLE BOOKINGS
-- ============================================================

INSERT INTO bookings
(user_id, space_id, start_time, end_time, status)
VALUES
(6, 1,
 '2026-08-25 10:00:00',
 '2026-08-25 12:00:00',
 'confirmed'),

(7, 2,
 '2026-08-25 14:00:00',
 '2026-08-25 16:00:00',
 'confirmed'),

(8, 3,
 '2026-08-26 11:00:00',
 '2026-08-26 14:00:00',
 'pending'),

(9, 4,
 '2026-08-27 15:00:00',
 '2026-08-27 17:00:00',
 'confirmed'),

(1, 5,
 '2026-08-28 09:00:00',
 '2026-08-28 11:00:00',
 'cancelled');


-- ============================================================
-- VERIFY IDLESPACE TABLES
-- ============================================================

SELECT * FROM users;

SELECT * FROM spaces;

SELECT * FROM bookings;


-- ============================================================
-- TASK 10 — JOIN PRACTICE
-- ============================================================

-- Get booking ID, user name and space name

SELECT
    bookings.id AS booking_id,
    users.name AS user_name,
    spaces.name AS space_name
FROM bookings
JOIN users
    ON bookings.user_id = users.id
JOIN spaces
    ON bookings.space_id = spaces.id;


-- ============================================================
-- BONUS — COMPLETE BOOKING INFORMATION
-- ============================================================

SELECT
    bookings.id AS booking_id,
    users.name AS user_name,
    users.email AS user_email,
    spaces.name AS space_name,
    spaces.location,
    spaces.price_per_hour,
    spaces.capacity,
    bookings.start_time,
    bookings.end_time,
    bookings.status
FROM bookings
JOIN users
    ON bookings.user_id = users.id
JOIN spaces
    ON bookings.space_id = spaces.id;


-- ============================================================
-- END OF DAY 5
-- ============================================================