import seaborn as sns

# Load the Titanic dataset
titanic = sns.load_dataset('titanic')

# Save the dataset to a CSV file
titanic.to_csv('dataset/titanic.csv', index=False)
