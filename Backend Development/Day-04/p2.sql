-- ============================================================
-- E-COMMERCE DATABASE PRACTICE
-- MYSQL
-- ============================================================

-- Create database
CREATE DATABASE IF NOT EXISTS ecommerce_db;

USE ecommerce_db;


-- ============================================================
-- 1. USERS TABLE
-- ============================================================

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- ============================================================
-- 2. PRODUCTS TABLE
-- ============================================================

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- ============================================================
-- 3. ORDERS TABLE
-- ============================================================

CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(30) DEFAULT 'pending',

    FOREIGN KEY (user_id)
        REFERENCES users(id)
);


-- ============================================================
-- 4. ORDER_ITEMS TABLE
-- ============================================================

CREATE TABLE order_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL,

    FOREIGN KEY (order_id)
        REFERENCES orders(id)
        ON DELETE CASCADE,

    FOREIGN KEY (product_id)
        REFERENCES products(id)
);


-- ============================================================
-- INSERT USERS
-- ============================================================

INSERT INTO users (name, email)
VALUES
('Arslaan Ahmad', 'arslaan@gmail.com'),
('Arshi Khan', 'arshi@gmail.com'),
('Rahul Sharma', 'rahul@gmail.com'),
('Priya Singh', 'priya@gmail.com'),
('Aman Verma', 'aman@gmail.com');


-- ============================================================
-- INSERT PRODUCTS
-- ============================================================

INSERT INTO products
(name, description, price, stock)
VALUES
('Dell Inspiron 15',
 '15-inch laptop for students and professionals',
 54999.00,
 10),

('Logitech K380 Keyboard',
 'Wireless compact keyboard',
 2999.00,
 25),

('HP Wireless Mouse',
 'Wireless optical mouse',
 899.00,
 50),

('Samsung 24 Inch Monitor',
 'Full HD LED monitor',
 12999.00,
 15),

('USB-C Hub',
 'Multi-port USB-C connectivity hub',
 2499.00,
 30),

('College Backpack',
 'Water-resistant laptop backpack',
 1499.00,
 40),

('Desk Lamp',
 'LED adjustable desk lamp',
 1799.00,
 20),

('Mechanical Keyboard',
 'RGB mechanical gaming keyboard',
 4499.00,
 12);


-- ============================================================
-- CREATE ORDERS
-- ============================================================

-- Order for Arslaan
INSERT INTO orders (user_id, status)
VALUES
(1, 'confirmed');


-- Order for Arshi
INSERT INTO orders (user_id, status)
VALUES
(2, 'confirmed');


-- Another order for Arslaan
INSERT INTO orders (user_id, status)
VALUES
(1, 'pending');


-- ============================================================
-- ADD PRODUCTS TO ORDERS
-- ============================================================

-- Order 1
-- Laptop x1
-- Mouse x2
-- Keyboard x1

INSERT INTO order_items
(order_id, product_id, quantity, price)
VALUES
(1, 1, 1, 54999.00),
(1, 3, 2, 899.00),
(1, 2, 1, 2999.00);


-- Order 2
-- Monitor x1
-- USB-C Hub x1
-- Backpack x1

INSERT INTO order_items
(order_id, product_id, quantity, price)
VALUES
(2, 4, 1, 12999.00),
(2, 5, 1, 2499.00),
(2, 6, 1, 1499.00);


-- Order 3
-- Mechanical Keyboard x1
-- Desk Lamp x2

INSERT INTO order_items
(order_id, product_id, quantity, price)
VALUES
(3, 8, 1, 4499.00),
(3, 7, 2, 1799.00);


-- ============================================================
-- VERIFY TABLES
-- ============================================================

SELECT * FROM users;

SELECT * FROM products;

SELECT * FROM orders;

SELECT * FROM order_items;


-- ============================================================
-- TASK 1 — FIND ALL ORDERS FOR A USER
-- ============================================================

-- Find all orders belonging to Arslaan

SELECT
    orders.id AS order_id,
    users.name AS user_name,
    orders.order_date,
    orders.status
FROM orders
JOIN users
    ON orders.user_id = users.id
WHERE users.id = 1;


-- ============================================================
-- TASK 2 — FIND ALL PRODUCTS IN AN ORDER
-- ============================================================

-- Find everything inside Order 1

SELECT
    orders.id AS order_id,
    products.name AS product_name,
    order_items.quantity,
    order_items.price
FROM order_items
JOIN orders
    ON order_items.order_id = orders.id
JOIN products
    ON order_items.product_id = products.id
WHERE orders.id = 1;


-- ============================================================
-- TASK 3 — CALCULATE AN ORDER'S TOTAL
-- ============================================================

-- Calculate total for Order 1

SELECT
    order_id,
    SUM(quantity * price) AS order_total
FROM order_items
WHERE order_id = 1
GROUP BY order_id;


-- ============================================================
-- TASK 4 — CALCULATE TOTAL FOR EVERY ORDER
-- ============================================================

SELECT
    orders.id AS order_id,
    users.name AS customer,
    SUM(order_items.quantity * order_items.price) AS order_total
FROM orders
JOIN users
    ON orders.user_id = users.id
JOIN order_items
    ON orders.id = order_items.order_id
GROUP BY
    orders.id,
    users.name;


-- ============================================================
-- BONUS — COMPLETE ORDER DETAILS
-- ============================================================

SELECT
    orders.id AS order_id,
    users.name AS customer,
    users.email,
    products.name AS product,
    order_items.quantity,
    order_items.price,
    (order_items.quantity * order_items.price) AS item_total,
    orders.status,
    orders.order_date
FROM orders
JOIN users
    ON orders.user_id = users.id
JOIN order_items
    ON orders.id = order_items.order_id
JOIN products
    ON order_items.product_id = products.id
ORDER BY orders.id;


-- ============================================================
-- BONUS — FIND ORDERS WITH TOTAL GREATER THAN ₹10,000
-- ============================================================

SELECT
    orders.id AS order_id,
    users.name AS customer,
    SUM(order_items.quantity * order_items.price) AS order_total
FROM orders
JOIN users
    ON orders.user_id = users.id
JOIN order_items
    ON orders.id = order_items.order_id
GROUP BY
    orders.id,
    users.name
HAVING order_total > 10000;


-- ============================================================
-- BONUS — FIND HOW MANY PRODUCTS ARE IN EACH ORDER
-- ============================================================

SELECT
    orders.id AS order_id,
    COUNT(order_items.product_id) AS number_of_products
FROM orders
JOIN order_items
    ON orders.id = order_items.order_id
GROUP BY orders.id;


-- ============================================================
-- DATABASE RELATIONSHIP
-- ============================================================

-- users
--   |
--   | 1
--   |
--   | many
--   v
-- orders
--   |
--   | 1
--   |
--   | many
--   v
-- order_items
--   |
--   | many
--   |
--   | 1
--   v
-- products


-- ============================================================
-- END OF E-COMMERCE DATABASE PRACTICE
-- ============================================================