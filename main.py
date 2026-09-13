from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return "Welcome to FastAPI series"
@app.get("/contact")
def contact():
    return "contact us at: example@gmail.com"