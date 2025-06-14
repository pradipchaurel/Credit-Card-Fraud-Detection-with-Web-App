from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)
model = joblib.load('fraud_model.pkl')

@app.route('/')
def home():
    return render_template('index_csv.html')

@app.route('/predict_csv', methods=['POST'])
def predict_csv():
    file = request.files['file']
    if not file:
        return render_template('index_csv.html', prediction_text="No file uploaded.")

    try:
        df = pd.read_csv(file)
    except Exception as e:
        return render_template('index_csv.html', prediction_text=f"Error reading CSV: {str(e)}")

    if df.shape[1] != 30:
        return render_template('index_csv.html', prediction_text=f"Expected 30 features, got {df.shape[1]}")

    try:
        predictions = model.predict(df)
        df['Prediction'] = predictions
        fraud_count = np.count_nonzero(predictions)
        total = len(predictions)
        result_summary = f"🚨 Detected {fraud_count} fraud transactions out of {total}."

        # Get preview of first 5 predictions
        prediction_table = df.head().to_html(classes='table', index=False)
        return render_template('index_csv.html', prediction_text=result_summary, prediction_table=prediction_table)
    except Exception as e:
        return render_template('index_csv.html', prediction_text=f"Prediction error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
