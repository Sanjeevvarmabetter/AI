# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import dtreeviz

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

species_names = ['setosa', 'versicolor', 'virginica']
y_labels = [species_names[label] for label in y]

print("___________________________________________")

# Display the class labels
print("Class Labels (Species):")
print(y_labels)

print("___________________________________________")
# Create a DataFrame from the dataset
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = y_labels  # Add the species labels as a new column
print(df.head())


print("___________________________________________")
# Display specific fields for 'setosa' (class 0)
setosa_data = df[df['target'] == 'setosa']
print("Data for 'Setosa' (Class 0):")
print(setosa_data.head(3))
print("___________________________________________")
# Display specific fields for 'versicolor' (class 1)
versicolor_data = df[df['target'] == 'versicolor']
print("\nData for 'Versicolor' (Class 1):")
print(versicolor_data.head(3))
print("___________________________________________")
# Display specific fields for 'virginica' (class 2)
virginica_data = df[df['target'] == 'virginica']
print("\nData for 'Virginica' (Class 2):")
print(virginica_data.head(3))
print("___________________________________________")
# We'll focus on binary classification, e.g., classifying 'setosa' (class 0) vs. 'versicolor' (class 1)
#y_binary = (y <= 1).astype(int)  # 1 if 'setosa' or 'versicolor', 0 if 'virginica'


# Prepare Data for Binary Classification: Classify between 'setosa' (class 1) and 'virginica' (class 0)
#y_binary = (y == 0).astype(int)  # 1 if 'setosa', 0 if 'virginica'

# Prepare Data for Binary Classification: Classify between 'virginica' (class 1) and 'versicolor' (class 0)
y_binary = (y == 2).astype(int)  # 1 if 'virginica', 0 if 'versicolor'


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.3, random_state=42)

# Create a decision tree classifier
clf = DecisionTreeClassifier()

# Train (fit) the classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("___________________________________________")
# Visualize the decision tree using 'dtreeviz' SETOSA VS VERSICOLOR
#m = dtreeviz.model(clf, X_train, y_train, target_name='target', feature_names=data.feature_names, class_names=['setosa', 'versicolor'])

# Visualize the decision tree using 'dtreeviz' SETOSA VS VIRGINIA
#m = dtreeviz.model(clf, X_train, y_train, target_name='target', feature_names=data.feature_names, class_names=['setosa', 'virginica'])

# Visualize the decision tree using 'dtreeviz' VIRGINIA VS VERSICOLOR
m = dtreeviz.model(clf, X_train, y_train, target_name='target', feature_names=data.feature_names, class_names=['virginica', 'versicolor'])

m.view()
