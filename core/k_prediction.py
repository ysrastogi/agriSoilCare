import joblib

def ph_model(rgb):
    model_path = 'models/K_model.pkl'
    model = joblib.load(model_path)
    k = model.predict([rgb])
    return k[0]