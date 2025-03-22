from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {"data":"Auth_Service"}
