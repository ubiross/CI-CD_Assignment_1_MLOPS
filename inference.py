import requests

# Define the URL of your Flask API
url = 'http://localhost:5000/predict'  # Update the URL if needed

# Prepare the data to be sent as a JSON payload
data = {
    'pclass': 1,  # Passenger class
    'age': 30,     # Age
    'fare': 100   # Fare
}

# Send a POST request to the Flask API
response = requests.post(url, json=data)

# Print the response from the API
print(response.json())
