from celery import Celery
from algorithm import dump_model,test_SVM,tfidf
from sklearn.model_selection import train_test_split
from algorithm import train,predict_service
import importlib
import logging
from celery import Task
from database import SessionLocal
from models import Record
from config import settings

celery = Celery(
 "worker",
 backend=settings.REDIS_URI,
 broker=settings.REDIS_URI,
)


@celery.task(bind=True)
def train_task(self):
   train() 
   return True
