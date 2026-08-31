from typing import TypedDict

names: list[str] = ["Alice", "Bob", "Charlie"]
scores: list[int] = [90, 85, 95]

# Student = TypedDict("Student", {
#     "name": str,
#     "score": int
# })

class Student(TypedDict):
    name: str
    score: int

students: dict[int, Student] = {}

for i, (name, score) in enumerate(zip(names, scores)):
    students[i] = {"name":name, "score":score}

print(students)