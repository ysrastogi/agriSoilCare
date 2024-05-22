import joblib

def ph_model(rgb):
    model_path = 'models/P_model.pkl'
    model = joblib.load(model_path)
    p = model.predict([rgb])
    return p[0]