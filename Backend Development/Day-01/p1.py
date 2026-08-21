

users = [
    {
        "id": 1,
        "name": "Arslaan",
        "email": "arslaan@example.com",
        "age": 20
    },
    {
        "id": 2,
        "name": "Rahul",
        "email": "rahul@example.com",
        "age": 21
    },
    {
        "id": 3,
        "name": "Aman",
        "email": "aman@example.com",
        "age": 22
    },
    {
        "id": 4,
        "name": "Priya",
        "email": "priya@example.com",
        "age": 20
    },
    {
        "id": 5,
        "name": "Ananya",
        "email": "ananya@example.com",
        "age": 21
    }
]



def get_users():
    return users




def get_user_by_id(user_id):

    for user in users:

        if user["id"] == user_id:
            return user

    return None



def create_user(name, email, age):

    # Generate new ID
    if len(users) == 0:
        new_id = 1
    else:
        new_id = max(user["id"] for user in users) + 1

    # Create new user
    new_user = {
        "id": new_id,
        "name": name,
        "email": email,
        "age": age
    }

    # Add user to list
    users.append(new_user)

    # Return created user
    return new_user




def update_user(user_id, name, email, age):

    user = get_user_by_id(user_id)

    if user is None:
        return None

    user["name"] = name
    user["email"] = email
    user["age"] = age

    return user




def delete_user(user_id):

    user = get_user_by_id(user_id)

    if user is None:
        return None

    users.remove(user)

    return user



def handle_request(method, user_id=None, data=None):

    method = method.upper()

    # ---------------- GET ----------------

    if method == "GET":

        if user_id is None:
            return get_users()

        return get_user_by_id(user_id)


    # ---------------- POST ----------------

    elif method == "POST":

        if data is None:
            return None

        return create_user(
            data["name"],
            data["email"],
            data["age"]
        )


    # ---------------- PUT ----------------

    elif method == "PUT":

        if user_id is None or data is None:
            return None

        return update_user(
            user_id,
            data["name"],
            data["email"],
            data["age"]
        )


    # ---------------- DELETE ----------------

    elif method == "DELETE":

        if user_id is None:
            return None

        return delete_user(user_id)


    # ---------------- INVALID METHOD ----------------

    else:
        return {
            "error": "Invalid HTTP method"
        }



print("\n========== ALL USERS ==========")

print(get_users())


print("\n========== FIND USER ==========")

print("User 1:")
print(get_user_by_id(1))

print("User 3:")
print(get_user_by_id(3))

print("User 999:")
print(get_user_by_id(999))


print("\n========== CREATE USER ==========")

new_user = create_user(
    "Kabir",
    "kabir@example.com",
    23
)

print("Created User:")
print(new_user)


print("\n========== UPDATE USER ==========")

updated_user = update_user(
    1,
    "Arslaan Ahmad",
    "arslaan.ahmad@example.com",
    21
)

print("Updated User:")
print(updated_user)


print("\n========== DELETE USER ==========")

deleted_user = delete_user(2)

print("Deleted User:")
print(deleted_user)

print("Trying to delete non-existing user:")
print(delete_user(999))


print("\n========== MINI API ==========")

print("\nGET /users")
print(handle_request("GET"))


print("\nGET /users/3")
print(handle_request("GET", 3))


print("\nPOST /users")

print(
    handle_request(
        "POST",
        data={
            "name": "Zoya",
            "email": "zoya@example.com",
            "age": 22
        }
    )
)


print("\nPUT /users/3")

print(
    handle_request(
        "PUT",
        3,
        {
            "name": "Aman Updated",
            "email": "aman.updated@example.com",
            "age": 23
        }
    )
)


print("\nDELETE /users/3")

print(
    handle_request(
        "DELETE",
        3
    )
)