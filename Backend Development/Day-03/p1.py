from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, Literal


app = FastAPI(title="Day 3 CRUD API")


# =========================================================
# PRODUCT MODEL
# =========================================================

class Product(BaseModel):
    name: str = Field(min_length=2)
    description: str
    price: float = Field(gt=0)
    category: str
    stock: int = Field(ge=0)


# =========================================================
# USER MODEL
# =========================================================

class User(BaseModel):
    name: str = Field(min_length=2)
    email: str
    age: int = Field(gt=0)


# =========================================================
# TASK MODEL
# =========================================================

class Task(BaseModel):
    title: str = Field(min_length=1)
    description: str
    completed: bool = False
    priority: Literal["low", "medium", "high"]


# =========================================================
# IN-MEMORY DATABASE
# =========================================================

products = [
    {
        "id": 1,
        "name": "Keyboard",
        "description": "Mechanical keyboard",
        "price": 2500,
        "category": "Electronics",
        "stock": 20
    }
]

users = []

tasks = []


# =========================================================
# PRODUCT CRUD
# =========================================================

# CREATE PRODUCT
@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: Product):

    # Duplicate name check
    for existing_product in products:
        if existing_product["name"].lower() == product.name.lower():
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A product with this name already exists"
            )

    # Generate new ID
    new_id = len(products) + 1

    new_product = {
        "id": new_id,
        **product.model_dump()
    }

    products.append(new_product)

    return new_product


# GET ALL PRODUCTS
@app.get("/products")
def get_products():
    return products


# GET ONE PRODUCT
@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )


# UPDATE PRODUCT
@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):

    # Find product
    for index, product in enumerate(products):

        if product["id"] == product_id:

            # Check duplicate name
            for other_product in products:
                if (
                    other_product["id"] != product_id
                    and other_product["name"].lower()
                    == updated_product.name.lower()
                ):
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail="Another product with this name already exists"
                    )

            products[index] = {
                "id": product_id,
                **updated_product.model_dump()
            }

            return products[index]

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )


# DELETE PRODUCT
@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    for index, product in enumerate(products):

        if product["id"] == product_id:
            deleted_product = products.pop(index)

            return {
                "message": "Product deleted successfully",
                "product": deleted_product
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )


# =========================================================
# USER CRUD
# =========================================================

# CREATE USER
@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):

    new_id = len(users) + 1

    new_user = {
        "id": new_id,
        **user.model_dump()
    }

    users.append(new_user)

    return new_user


# GET ALL USERS
@app.get("/users")
def get_users():
    return users


# GET ONE USER
@app.get("/users/{user_id}")
def get_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )


# UPDATE USER
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):

    for index, user in enumerate(users):

        if user["id"] == user_id:

            users[index] = {
                "id": user_id,
                **updated_user.model_dump()
            }

            return users[index]

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )


# DELETE USER
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    for index, user in enumerate(users):

        if user["id"] == user_id:

            deleted_user = users.pop(index)

            return {
                "message": "User deleted successfully",
                "user": deleted_user
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )


# =========================================================
# TASK MANAGER API
# =========================================================

# CREATE TASK
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):

    new_id = len(tasks) + 1

    new_task = {
        "id": new_id,
        **task.model_dump()
    }

    tasks.append(new_task)

    return new_task


# GET TASKS WITH FILTERING
@app.get("/tasks")
def get_tasks(
    completed: Optional[bool] = None,
    priority: Optional[Literal["low", "medium", "high"]] = None
):

    result = tasks

    # Filter by completed status
    if completed is not None:
        result = [
            task
            for task in result
            if task["completed"] == completed
        ]

    # Filter by priority
    if priority is not None:
        result = [
            task
            for task in result
            if task["priority"] == priority
        ]

    return result


# GET ONE TASK
@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:

        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )


# UPDATE TASK
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: Task):

    for index, task in enumerate(tasks):

        if task["id"] == task_id:

            tasks[index] = {
                "id": task_id,
                **updated_task.model_dump()
            }

            return tasks[index]

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )


# DELETE TASK
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    for index, task in enumerate(tasks):

        if task["id"] == task_id:

            deleted_task = tasks.pop(index)

            return {
                "message": "Task deleted successfully",
                "task": deleted_task
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )