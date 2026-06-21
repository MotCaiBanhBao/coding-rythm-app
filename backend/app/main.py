from fastapi import FastAPI

from app.schemas.task import TaskSchema

app = FastAPI()

@app.get("/{task_id}")
def read_root(task_id: str):
    test_model = TaskSchema(name="1", description="2")
    return {"Hello": f"Task ID: {task_id}", "Test Model": test_model}
