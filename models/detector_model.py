import pickle

model = pickle.load(open('models/detect_model.sav', 'rb'))

def predict(data):
    x = data[['Ia','Ib','Ic','Va','Vb','Vc']]
    return model.predict(x)[0]