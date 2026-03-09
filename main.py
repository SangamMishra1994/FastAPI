from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.getAll("/all_detail")
def getAllInfo():
    return {"message": "All the data in the Json format"}
