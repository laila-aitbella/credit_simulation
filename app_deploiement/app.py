from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the saved model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    Credit_History = request.form['Credit_History']
    Married = request.form['Married']
    ApplicantIncome = request.form['ApplicantIncome']

    # Ensure the input is in the correct format
    try:
        Credit_History = int(Credit_History)
        Married = int(Married)
        ApplicantIncome = float(ApplicantIncome)
    except ValueError:
        return render_template('index.html', prediction_text="Invalid input. Please enter valid numbers.")

    # Create the feature vector for prediction
    features = [[Credit_History, Married, ApplicantIncome]]
    prediction = model.predict(features)[0]

    # Interpret the prediction result
    if prediction == 1:
        result = "Your credit is approved."
    else:
        result = "Your credit is denied."

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
