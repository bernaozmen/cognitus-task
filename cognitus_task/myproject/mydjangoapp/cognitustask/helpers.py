import os

class Settings(object):
    TRAIN_HOST = os.getenv("TRAIN_HOST", "127.0.0.1")
    TRAIN_PORT = os.getenv("TRAIN_PORT", "")
   
    TRAIN_URI = "http://{}:{}/train".format(
    TRAIN_HOST, TRAIN_PORT)

    PREDICT_URI = "http://{}:{}/predict".format(
    TRAIN_HOST, TRAIN_PORT)

