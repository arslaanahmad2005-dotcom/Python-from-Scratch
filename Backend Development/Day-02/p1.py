# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from typing import Optional

app = FastAPI(title="Day 2 Practice API")


# =========================
# USERS
# =========================

users = [
    {"id": 1, "name": "Arslaan", "email": "arslaan@example.com"},
    {"id": 2, "name": "Rahul", "email": "rahul@example.com"},
    {"id": 3, "name": "Aman", "email": "aman@example.com"},
    {"id": 4, "name": "Priya", "email": "priya@example.com"},
    {"id": 5, "name": "Neha", "email": "neha@example.com"}
]


# =========================
# PRODUCTS
# =========================

products = [
    {"id": 1, "name": "HP Pavilion", "price": 65000, "category": "laptop"},
    {"id": 2, "name": "Dell Inspiron", "price": 58000, "category": "laptop"},
    {"id": 3, "name": "Samsung Galaxy S24", "price": 72000, "category": "phone"},
    {"id": 4, "name": "iPhone 15", "price": 65000, "category": "phone"},
    {"id": 5, "name": "Lenovo IdeaPad", "price": 52000, "category": "laptop"},
    {"id": 6, "name": "OnePlus 13", "price": 70000, "category": "phone"},
    {"id": 7, "name": "ASUS VivoBook", "price": 60000, "category": "laptop"},
    {"id": 8, "name": "Google Pixel 9", "price": 75000, "category": "phone"},
    {"id": 9, "name": "Acer Aspire", "price": 48000, "category": "laptop"},
    {"id": 10, "name": "Nothing Phone", "price": 35000, "category": "phone"}
]


# =========================
# STUDENTS
# =========================

students = [
    {"id": 1, "name": "Arslaan", "email": "arslaan@example.com", "course": "CSE", "year": 3},
    {"id": 2, "name": "Rahul", "email": "rahul@example.com", "course": "ECE", "year": 2},
    {"id": 3, "name": "Priya", "email": "priya@example.com", "course": "CSE", "year": 3},
    {"id": 4, "name": "Aman", "email": "aman@example.com", "course": "ME", "year": 1},
    {"id": 5, "name": "Neha", "email": "neha@example.com", "course": "CSE", "year": 2},
    {"id": 6, "name": "Riya", "email": "riya@example.com", "course": "ECE", "year": 3},
    {"id": 7, "name": "Karan", "email": "karan@example.com", "course": "CSE", "year": 4},
    {"id": 8, "name": "Simran", "email": "simran@example.com", "course": "IT", "year": 3}
]


# =========================
# TASK 1 — BASIC API
# =========================

@app.get("/")
def home():
    return {"message": "API is running"}


@app.get("/about")
def about():
    return {
        "message": "Information about your API",
        "name": "Day 2 Practice API",
        "technology": "FastAPI"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


# =========================
# TASK 2 — USER API
# =========================

@app.get("/users")
def get_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    return {"message": "User not found"}


# =========================
# TASK 3, 4 & 5 — PRODUCTS
# =========================

@app.get("/products")
def get_products(
    category: Optional[str] = None,
    limit: Optional[int] = None,
    offset: int = 0
):
    result = products

    if category is not None:
        result = [
            product for product in result
            if product["category"].lower() == category.lower()
        ]

    result = result[offset:]

    if limit is not None:
        result = result[:limit]

    return result


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {"message": "Product not found"}


# =========================
# TASK 6 — USER ORDERS
# =========================

@app.get("/users/{user_id}/orders")
def get_user_orders(user_id: int, limit: int = 5):
    return {
        "user_id": user_id,
        "limit": limit,
        "orders": []
    }


# =========================
# MINI CHALLENGE — STUDENTS
# =========================

@app.get("/students")
def get_students(
    course: Optional[str] = None,
    year: Optional[int] = None,
    limit: Optional[int] = None
):
    result = students

    if course is not None:
        result = [
            student for student in result
            if student["course"].lower() == course.lower()
        ]

    if year is not None:
        result = [
            student for student in result
            if student["year"] == year
        ]

    if limit is not None:
        result = result[:limit]

    return result


@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}