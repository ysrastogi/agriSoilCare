import joblib

def ph_model(rgb):
    model_path = 'models/pH_model.pkl'
    model = joblib.load(model_path)
    ph = model.predict([rgb])
    return ph[0]