import joblib

def ph_model(rgb):
    model_path = 'models/N_model.pkl'
    model = joblib.load(model_path)
    n = model.predict([rgb])
    return n[0]