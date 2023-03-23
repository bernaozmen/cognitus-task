import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
import psycopg2
from sklearn.svm import SVC
from sklearn.metrics import precision_score, accuracy_score, recall_score
from sklearn.model_selection import train_test_split
from crud import get_users
from database import SessionLocal
from config import rc

from cache import RedisCache
import redis


def create_data():
    conn = SessionLocal()
    users = get_users(conn)
    texts=[]
    labels=[]
    for i in users:
        texts.append(i.text)
        labels.append(i.label)
    df = pd.DataFrame(list(zip(texts, labels)), columns=['text', 'label'])
    return df['text'].tolist(), df['label'].tolist()

#feature extraction - creating a tf-idf matrix
def tfidf(data, ma = 0.6, mi = 0.0001):
    tfidf_vectorize = TfidfVectorizer()
    tfidf_data = tfidf_vectorize.fit_transform(data)
    return tfidf_data, tfidf_vectorize


#SVM classifier
def test_SVM(x_train, x_test, y_train, y_test):
    SVM = SVC(kernel = 'linear', probability=True)
    SVMClassifier = SVM.fit(x_train, y_train)
    predictions = SVMClassifier.predict(x_test)
    a = accuracy_score(y_test, predictions)
    p = precision_score(y_test, predictions, average = 'weighted')
    r = recall_score(y_test, predictions, average = 'weighted')
    return SVMClassifier, a, p, r


def dump_model(key, model, file_output):
    dmp = pickle.dumps(model)
    rc.set(key,dmp)


def load_model(key,file_input):
    res = rc.get(key)
   
    if res:
        result = pickle.loads(res)
    else:
        result = pickle.load(open(file_input, 'rb'))
    
    return result
        

# TRAIN
def train():
    text, label = create_data()
    training, vectorizer = tfidf(text)
    x_train, x_test, y_train, y_test = train_test_split(training, label, test_size = 0.25, random_state = 0)
    model, accuracy, precision, recall = test_SVM(x_train, x_test, y_train, y_test)
    # cache2.setFromCache("model",dump_model(model, 'model.pickle'))
    # cache2.setFromCache("vectorizer",dump_model(vectorizer, 'vectorizer.pickle'))
    dump_model("model",model,'model.pickle')
    dump_model("vectorizer",vectorizer,'vectorizer.pickle')
    return True

# PREDICTION
def predict_service(user_text):
   
    model = load_model("model",'model.pickle')
    vectorizer = load_model("vectorizer",'vectorizer.pickle')
    tfidf = vectorizer.transform([user_text])
    result = model.predict_proba(tfidf)
    print(result)
    return result

