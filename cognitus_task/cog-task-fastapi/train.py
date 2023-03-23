from algorithm import dump_model,test_SVM,tfidf
from sklearn.model_selection import train_test_split

def train():
    training, vectorizer = tfidf(text)
    x_train, x_test, y_train, y_test = train_test_split(training, label, test_size = 0.25, random_state = 0)
    model, accuracy, precision, recall = test_SVM(x_train, x_test, y_train, y_test)
    dump_model(model, 'model.pickle')
    dump_model(vectorizer, 'vectorizer.pickle')
    return 1