from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained Titanic model
model = joblib.load('model/titanic_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        pclass = data['pclass']
        age = data['age']
        fare = data['fare']
        
        # Handle missing values for age
        if age is None:
            age = X['age'].mean()
        
        prediction = model.predict([[pclass, age, fare]])[0]
        return jsonify({'prediction': int(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
