from pydantic import BaseModel

class Record(BaseModel):
    text:str
    #label:str

    #class Config:
     #   orm_mode = True

class Train(BaseModel):
    detail:str

class Prediction(BaseModel):
    task_id:str
    detail:str
    x:float
    y:float

class User(Record):
    id: int
    text: str
    label: str
    
    class Config:
        orm_mode = True

class Predict(BaseModel):
    text:str