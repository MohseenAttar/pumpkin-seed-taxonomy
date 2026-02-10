from flask import Blueprint, render_template, flash, request
import numpy as np
import joblib
import os

routes = Blueprint('routes', __name__, template_folder='../templates')

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'static', 'model', 'RandomForestClassifier_model')
SCALER_PATH = os.path.join(os.path.dirname(__file__), '..', 'static', 'model', 'scaler')

FEATURES = [
    'Area', 'Perimeter', 'Major_Axis_Length', 'Minor_Axis_Length',
    'Convex_Area', 'Equiv_Diameter', 'Eccentricity', 'Solidity',
    'Extent', 'Roundness', 'Aspect_Ration', 'Compactness'
]

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# ===== Landing Page =====
@routes.route('/', methods=['GET'])
def home():
    return render_template('index.html')   # ← Landing Page

# ===== Prediction Form Page =====
@routes.route('/form', methods=['GET'])
def form_page():
    return render_template('predict.html')   # ← Prediction Form Page

# ===== Prediction Logic =====
@routes.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = []

        for feature in FEATURES:
            value = float(request.form.get(feature))
            input_data.append(value)

        input_array = np.array([input_data])
        scaled_input = scaler.transform(input_array)

        prediction = int(model.predict(scaled_input)[0])

        probabilities = model.predict_proba(scaled_input)[0]
        cercevelik_prob = round(probabilities[0] * 100, 2)
        urgup_prob = round(probabilities[1] * 100, 2)

        input_summary = {feature: value for feature, value in zip(FEATURES, input_data)}

        return render_template(
            'result.html',
            prediction=prediction,
            input_summary=input_summary,
            cercevelik_prob=cercevelik_prob,
            urgup_prob=urgup_prob
        )

    except:
        flash("Please enter valid numeric values!", "error")
        return render_template('predict.html')
