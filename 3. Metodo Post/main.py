from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    name: str
    lastname: str
    skills: List[str] = []

@app.post("/students")
def saveStudent(student: Student):
    return f"Habilidades de {student.name}: {student.skills}"