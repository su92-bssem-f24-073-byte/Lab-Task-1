def check_student(score, documents_complete, attendance, age):
    if score < 70:
        return "Hold"
    if not documents_complete:
        return "Hold"
    if attendance < 75:
        return "Hold"
    if age < 18:
        return "Hold"
    return "Review"
tests = [
    (80, True, 80, 18),
    (80, True, 60, 18),
    (80, True, 80, 16),
    (70, True, 75, 18)
]
for test in tests:
    result = check_student(*test)
    print("Input:", test, "| Result:", result)