from flask import Flask, request, render_template
import pandas as pd
import numpy as np

from src.pipeline.prediction_pipeline import PredictPipeline
from src.pipeline.prediction_pipeline import CustomData

application = Flask(__name__)
app = application

@app.route("/")
def index():
    return render_template('index.html')  # Ensure this file exists in the "templates" folder

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_data():
    if request.method == 'GET':
        return render_template('home.html')  # Ensure this file exists in the "templates" folder
    else:
        try:
            # Initialize the custom data object
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )

            # Get DataFrame from the custom data
            pred_df = data.get_as_dataframe()
            print("Input DataFrame:", pred_df)

            # Predict using the pipeline
            predict_pipeline = PredictPipeline()
            results = np.round(predict_pipeline.predict(pred_df),2)
            print("Prediction Results:", results)

            return render_template('home.html', results=results[0])

        except Exception as e:
            print("Error occurred:", str(e))
            return render_template('home.html', results="An error occurred during prediction.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
