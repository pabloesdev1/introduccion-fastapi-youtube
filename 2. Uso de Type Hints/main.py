from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def mensaje():
    return "Hola mundo"

@app.get("/login")
def mensaje():
    return "Ingrese sus datos"

@app.get("/users/{user_id}")
def mensaje(user_id: str):
    return f"El id del usuario es: {user_id}"