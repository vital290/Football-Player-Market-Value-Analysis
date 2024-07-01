from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load your ML model
with open('rf_tuned1.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/', methods=['GET'])
def home():
    # Render the home page with the form
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form
    try:
        # Retrieve values from form
        age = int(request.form['age'])
        overall = int(request.form['overall'])
        potential = int(request.form['potential'])
        international_reputation = int(request.form['international_reputation'])
        release_clause = float(request.form['release_clause'])
        wage = float(request.form['wage'])

        # Make prediction
        prediction = model.predict([[age, overall, potential, international_reputation, release_clause, wage]])

        # Return result
        return jsonify({'market_value': prediction[0]})
    except Exception as e:
        # Return error message
        return jsonify({'error': str(e)})

# Check if the executed file is the main program and run the app
if __name__ == '__main__':
    app.run(debug=True)
