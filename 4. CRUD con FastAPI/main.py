from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI()

students = []

class Student(BaseModel):
    id: str
    name: str
    lastname: str
    skills: List[str] = []

@app.get("/students")
def get_students():
    return students

@app.get("/students/{id}")
def get_student(id: str):
    for student in students:
        if student["id"] == id:
            return student
    return "No existe el estudiante"

@app.post("/students")
def save_student(student: Student):
    student.id = str(uuid4())
    students.append(student.dict())
    return "Estudiante registrado"

@app.put("/students/{id}")
def update_student(updated_updated: Student, id:str):
    for student in students:
        if student["id"] == id:
            student["name"] = updated_updated.name
            student["lastname"] = updated_updated.lastname
            student["skills"] = updated_updated.skills
            return "Estudiante modificado"
    return "No existe el estudiante"

@app.delete("/students/{id}")
def delete_student(id: str):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return "Estudiante eliminado"
    return "No existe el estudiante"