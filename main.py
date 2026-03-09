from fastapi import FastAPI, Body

app = FastAPI()

TODOS = [
    {"title": "Task 1", "description": "My Task 1", "is_completed": False},
    {"title": "Task 2", "description": "My Task 2", "is_completed": True},
    {"title": "Task 3", "description": "My Task 3", "is_completed": True},
    {"title": "Task 4", "description": "My Task 4", "is_completed": False},
]

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.getAll("/todos/all")
def get_all_todo():
    return TODOS


@app.post("/todos/add")
def create_todo(new_todo=Body()):
    TODOS.append(new_todo)
    return {"message":"Success"}


@app.delete("/todos/{title}")
def delete_todo_by_title(title):
    for index in range(len(TODOS)):
        if TODOS[index][title].lower() == title.lower():
            TODOS.pop(index)
            return {"message":"Delete Successfully"}


@app.put("/todos/update")
def update_todo(existing_todo=Body()):
    TODOS[0] = existing_todo
    return {"message": "Updated Successfully"}
    
         
