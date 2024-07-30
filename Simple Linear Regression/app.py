from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get CGPA from form data
        cgpa = float(request.form['cgpa'])
        
        # Make prediction
        prediction = model.predict([[cgpa]])
        
        # Format prediction to two decimal places
        formatted_prediction = f'{prediction[0][0]:.2f}'
        
        # Return result as JSON
        return jsonify({'result': f'Your package will be: {formatted_prediction}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
