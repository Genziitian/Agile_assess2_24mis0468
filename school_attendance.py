print("attendance system by 24mis")
def calculate_percentage(days_present, total_days):
    return (days_present / total_days) * 100


def get_status(percentage):
    if percentage >= 95:
        return "Excellent"
    if percentage >= 85:
        return "Good"
    if percentage >= 75:
        return "Average"
    return "Poor"


def process_attendance_data(students_data):
    processed_students = []

    for student in students_data:
        name = student["name"]
        pct = calculate_percentage(student["days_present"], student["total_days"])
        status = get_status(pct)

        processed_students.append(
            {"name": name, "percentage": pct, "status": status}
        )

    # 1. Print highest attendance 
    # Sorts by percentage descending and takes the first item
    processed_students.sort(key=lambda x: x["percentage"], reverse=True)
    highest = processed_students[0]

    print("--- STUDENT ATTENDANCE REPORT ---")
    print(f"Highest Attendance: {highest['name']} ({highest['percentage']:.1f}%)")

    # 2. Print poor attendance (<75%)
    print("\nStudents with Poor Attendance (<75%):")
    has_poor = False
    for s in processed_students:
        if s["status"] == "Poor":
            print(f" - {s['name']}: {s['percentage']:.1f}%")
            has_poor = True
    if not has_poor:
        print(" - None")

    # 3. Print all students 
    print("\nAll Students Sorted by Attendance:")
    for s in processed_students:
        print(f" - {s['name']}: {s['percentage']:.1f}% | Status: {s['status']}")


# Data output 
sample_students = [
    {"name": "John Doe", "total_days": 20, "days_present": 19},
    {"name": "Jane Olson", "total_days": 20, "days_present": 17},
    {"name": "Sam Wilson", "total_days": 20, "days_present": 16},
    {"name": "Alex Mercer", "total_days": 20, "days_present": 13},
]

process_attendance_data(sample_students)
print("set 3 attendance tracker done by 24mis0468")
