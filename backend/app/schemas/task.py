from pydantic import BaseModel

class TaskSchema(BaseModel):
    name: str
    description: str
    is_completed: bool | None = None
