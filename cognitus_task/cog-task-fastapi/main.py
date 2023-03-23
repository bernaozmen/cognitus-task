from fastapi import FastAPI
from database import SessionLocal, engine
from starlette.responses import RedirectResponse
import crud, models, schemas
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from algorithm import predict_service,train
from typing import List
from tasks import train_task
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import schemas

from cache import RedisCache

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory='templates')

cache = RedisCache("localhost",6379,1)


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")
   # return {'message': 'Welcome'}


"""@app.get('/train')
def train(request: Request):
    context = {'request': request}
    return templates.TemplateResponse('train.html', context)"""

@app.post('/train')
async def train(request: Request):
    train_task.delay()
    res = "train successfully completed"
    context = {'request': request, 'result': res}
    return {"response": res}
    #return templates.TemplateResponse('train.html', context)

"""@app.get('/predict')
def predict(request: Request):
    return templates.TemplateResponse('train.html', context={'request': request})"""

@app.post('/predict')
def predict(request_data: schemas.Predict):  
    result = predict_service(request_data.text)
    context = {'result': result}
    return {"response": context}
    #return templates.TemplateResponse('train.html', context)

"""@app.post('/predict')
def predict(request: Request,text: str = Form(...)):
    cache_res = cache.getDataFromCache(text)
    res = {"x":0,"y":0}

    if None in cache_res:
        result = predict_service(text)
        #res = {"x":result[0][0],"y":result[0][1]}
        cache.addDataToCache(text,result[0][0],result[0][1])
        res["x"]=result[0][0]
        res["y"]=result[0][1]

    else:
        res["x"]=cache_res[0]
        res["y"]=cache_res[1]

    #result = predict_service(text)
    context = {'request': request, 'result': res, 'text': text}
    return templates.TemplateResponse('train.html', context)"""


"""@app.get('/pre')
def predict(request: Request):
    return templates.TemplateResponse('train.html', context={'request': request})

@app.post('/pre')
def predict(request: Request, text:str = Form(...)):
    result = text
    context = {'request': request, 'result': result, 'text': text}
    return templates.TemplateResponse('train.html', context)"""

#@app.post('/train')
#async def train():
#    res = train_task.delay()
#    return "okey"

"""@app.post('/predict')
def predict(text:str):
    result = predict_service(text)
    return {"text":text, "result": result}"""


"""@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user"""

    
#if __name__ == "__main__":
#    uvicorn.run(app, host="0.0.0.0", port=8000)

