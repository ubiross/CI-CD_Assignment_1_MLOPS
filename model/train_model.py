import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load the Titanic dataset
data = pd.read_csv('dataset/titanic.csv')

# Select features and target variable
X = data[['pclass', 'age', 'fare']]
y = data['survived']

# Handle missing values
X['age'].fillna(X['age'].mean(), inplace=True)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the trained model to a file
import joblib
joblib.dump(model, 'model/titanic_model.pkl')
