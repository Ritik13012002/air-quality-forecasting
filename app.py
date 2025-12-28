from flask import Flask, request, render_template_string
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained next-day AQI model
model = pickle.load(open("models/aqi_next_day_model.pkl", "rb"))

def aqi_category(aqi):
    if aqi <= 50:
        return "Good 😊"
    elif aqi <= 100:
        return "Satisfactory 🙂"
    elif aqi <= 200:
        return "Moderate 😐"
    elif aqi <= 300:
        return "Poor 😷"
    elif aqi <= 400:
        return "Very Poor 🤒"
    else:
        return "Severe ☠️"

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None
    category = None

    if request.method == "POST":
        data = {
            'PM2.5': float(request.form['PM2.5']),
            'PM10': float(request.form['PM10']),
            'NO': float(request.form['NO']),
            'NO2': float(request.form['NO2']),
            'NOx': float(request.form['NOx']),
            'NH3': float(request.form['NH3']),
            'CO': float(request.form['CO']),
            'SO2': float(request.form['SO2']),
            'O3': float(request.form['O3']),
            'Benzene': float(request.form['Benzene']),
            'Toluene': float(request.form['Toluene']),
            'Xylene': float(request.form['Xylene']),
            'month': int(request.form['month']),
            'day': int(request.form['day']),
            'AQI_lag_1': float(request.form['AQI_lag_1']),
            'AQI_roll_7': float(request.form['AQI_roll_7'])
        }

        df = pd.DataFrame([data])
        prediction = round(model.predict(df)[0], 2)
        category = aqi_category(prediction)

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Next-Day AQI Forecast</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f8;
            }
            .container {
                width: 420px;
                margin: 40px auto;
                background: white;
                padding: 25px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }
            h2 {
                text-align: center;
                margin-bottom: 20px;
            }
            label {
                font-weight: bold;
            }
            input {
                width: 100%;
                padding: 6px;
                margin-bottom: 10px;
            }
            button {
                width: 100%;
                padding: 10px;
                background: #007bff;
                color: white;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
            }
            button:hover {
                background: #0056b3;
            }
            .result {
                margin-top: 20px;
                text-align: center;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h2>Next-Day AQI Forecast</h2>

            <form method="post">
                <label>PM2.5</label>
                <input name="PM2.5" value="80">

                <label>PM10</label>
                <input name="PM10" value="120">

                <label>NO</label>
                <input name="NO" value="30">

                <label>NO2</label>
                <input name="NO2" value="40">

                <label>NOx</label>
                <input name="NOx" value="50">

                <label>NH3</label>
                <input name="NH3" value="20">

                <label>CO</label>
                <input name="CO" value="1.2">

                <label>SO2</label>
                <input name="SO2" value="15">

                <label>O3</label>
                <input name="O3" value="25">

                <label>Benzene</label>
                <input name="Benzene" value="5">

                <label>Toluene</label>
                <input name="Toluene" value="8">

                <label>Xylene</label>
                <input name="Xylene" value="6">

                <label>Month</label>
                <input name="month" value="6">

                <label>Day</label>
                <input name="day" value="15">

                <label>Yesterday AQI</label>
                <input name="AQI_lag_1" value="150">

                <label>Last 7 Days Avg AQI</label>
                <input name="AQI_roll_7" value="160">

                <button type="submit">Predict Tomorrow AQI</button>
            </form>

            {% if prediction %}
            <div class="result">
                <h3>Predicted AQI: {{ prediction }}</h3>
                <h4>Category: {{ category }}</h4>
            </div>
            {% endif %}
        </div>
    </body>
    </html>
    """, prediction=prediction, category=category)

if __name__ == "__main__":
   
  import os

  if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

