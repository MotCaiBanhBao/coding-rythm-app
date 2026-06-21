from sqlmodel import Field, SQLModel

class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    is_completed: bool | None
