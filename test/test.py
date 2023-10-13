import joblib
import pytest

# Load the pre-trained model
model = joblib.load('model/titanic_model.pkl')  # Replace with the correct path to your model

@pytest.fixture
def sample_input_data():
    # Define sample input data for testing
    return {
        'pclass': 1,  # Passenger class
        'age': 30,     # Age
        'fare': 100   # Fare
    }

def test_model_prediction(sample_input_data):
    # Make predictions using the model
    prediction = model.predict([[sample_input_data['pclass'], sample_input_data['age'], sample_input_data['fare']]])

    # Perform assertions on the prediction
    assert len(prediction) == 1
    assert prediction[0] in [0, 1]  # Assuming your model predicts binary outcomes
