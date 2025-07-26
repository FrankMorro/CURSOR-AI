from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Simple",
    description="API de ejemplo creada con FastAPI",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "¡Hola, FastAPI!"}

@app.get("/test")
def test():
    return {"status": "OK"} 