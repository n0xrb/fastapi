from fastapi import FastAPI

app = FastAPI()

@app.get("/") # PATH OPERATOR / DECORATOR
def home(): # PATH OPERATION FUNCTION
    return {"success":True}
