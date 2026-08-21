# ============================================================
# STUDENT MANAGEMENT BACKEND SIMULATION
# ============================================================


students = [
    {
        "id": 1,
        "name": "Arslaan",
        "email": "arslaan@example.com",
        "course": "CSE",
        "year": 3
    },
    {
        "id": 2,
        "name": "Rahul",
        "email": "rahul@example.com",
        "course": "ECE",
        "year": 2
    },
    {
        "id": 3,
        "name": "Ananya",
        "email": "ananya@example.com",
        "course": "CSE",
        "year": 3
    },
    {
        "id": 4,
        "name": "Aman",
        "email": "aman@example.com",
        "course": "ME",
        "year": 4
    },
    {
        "id": 5,
        "name": "Priya",
        "email": "priya@example.com",
        "course": "CSE",
        "year": 2
    }
]


# ============================================================
# CREATE STUDENT
# ============================================================

def create_student(name, email, course, year):

    if len(students) == 0:
        new_id = 1
    else:
        new_id = max(student["id"] for student in students) + 1

    new_student = {
        "id": new_id,
        "name": name,
        "email": email,
        "course": course,
        "year": year
    }

    students.append(new_student)

    return new_student


# ============================================================
# GET ALL STUDENTS
# ============================================================

def get_students():

    return students


# ============================================================
# GET STUDENT BY ID
# ============================================================

def get_student_by_id(student_id):

    for student in students:

        if student["id"] == student_id:
            return student

    return None


# ============================================================
# UPDATE STUDENT
# ============================================================

def update_student(student_id, name, email, course, year):

    student = get_student_by_id(student_id)

    if student is None:
        return None

    student["name"] = name
    student["email"] = email
    student["course"] = course
    student["year"] = year

    return student


# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student(student_id):

    student = get_student_by_id(student_id)

    if student is None:
        return None

    students.remove(student)

    return student


# ============================================================
# SEARCH STUDENTS BY COURSE
# ============================================================

def search_students(course):

    result = []

    for student in students:

        if student["course"].lower() == course.lower():
            result.append(student)

    return result


# ============================================================
# STUDENT API ROUTER
# ============================================================

def handle_student_request(
    method,
    student_id=None,
    data=None,
    course=None
):

    method = method.upper()


    # ========================================================
    # GET
    # ========================================================

    if method == "GET":

        # GET /students?course=CSE
        if course is not None:
            return search_students(course)

        # GET /students
        if student_id is None:
            return get_students()

        # GET /students/{id}
        return get_student_by_id(student_id)


    # ========================================================
    # POST
    # ========================================================

    elif method == "POST":

        if data is None:
            return None

        return create_student(
            data["name"],
            data["email"],
            data["course"],
            data["year"]
        )


    # ========================================================
    # PUT
    # ========================================================

    elif method == "PUT":

        if student_id is None or data is None:
            return None

        return update_student(
            student_id,
            data["name"],
            data["email"],
            data["course"],
            data["year"]
        )


    # ========================================================
    # DELETE
    # ========================================================

    elif method == "DELETE":

        if student_id is None:
            return None

        return delete_student(student_id)


    # ========================================================
    # INVALID METHOD
    # ========================================================

    else:

        return {
            "error": "Invalid HTTP method"
        }


# ============================================================
# TEST STUDENT BACKEND
# ============================================================


print("\n====================================")
print("GET ALL STUDENTS")
print("====================================")

print(
    handle_student_request("GET")
)


print("\n====================================")
print("GET STUDENT BY ID")
print("====================================")

print(
    handle_student_request(
        "GET",
        student_id=3
    )
)


print("\n====================================")
print("SEARCH CSE STUDENTS")
print("====================================")

print(
    handle_student_request(
        "GET",
        course="CSE"
    )
)


print("\n====================================")
print("CREATE STUDENT")
print("====================================")

print(
    handle_student_request(
        "POST",
        data={
            "name": "Kabir",
            "email": "kabir@example.com",
            "course": "CSE",
            "year": 3
        }
    )
)


print("\n====================================")
print("UPDATE STUDENT")
print("====================================")

print(
    handle_student_request(
        "PUT",
        student_id=1,
        data={
            "name": "Arslaan Ahmad",
            "email": "arslaan.ahmad@example.com",
            "course": "CSE",
            "year": 4
        }
    )
)


print("\n====================================")
print("DELETE STUDENT")
print("====================================")

print(
    handle_student_request(
        "DELETE",
        student_id=2
    )
)


print("\n====================================")
print("FINAL STUDENT LIST")
print("====================================")

print(
    handle_student_request("GET")
)