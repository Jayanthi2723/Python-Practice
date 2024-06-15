import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import export_text
from sklearn import preprocessing
import pydotplus
from io import StringIO

# Load the original CSV file
df = pd.read_csv('outdoors.csv')

def map_outlook_to_weather(outlook):
    if outlook == 'Sunny':
        return 'Sunny'
    elif outlook == 'Overcast':
        return 'Cloudy'
    elif outlook == 'Rain':
        return 'Rainy'
    else:
        return 'Unknown'

df['Weather'] = df['Outlook'].apply(map_outlook_to_weather)

# Performing dummy encoding on the "Weather" column
weather_dummies = pd.get_dummies(df['Weather'], prefix='Weather')
df = pd.concat([df, weather_dummies], axis=1)
df.drop('Weather', axis=1, inplace=True)

# Mapping 'yes' to 1 and 'no' to 0 in the "Play" column
df['Play'] = df['Play'].map({'y': 1, 'n': 0})

# Save the corrected data to a new CSV file and print it
df.to_csv('weather_data_corrected.csv', index=False)
print("Data saved to 'weather_data_corrected.csv'")

# Read the corrected data from the CSV file
df = pd.read_csv('weather_data_corrected.csv')

# Separate features and target variable
X = df[['Temperature', 'Humidity', 'Wind', 'Weather_Sunny', 'Weather_Cloudy', 'Weather_Rainy']]
y = df['Play']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Decision Tree classifier
clf = DecisionTreeClassifier()

# Train the classifier on the training data
clf.fit(X_train, y_train)

# Making predictions on the test data
y_pred = clf.predict(X_test)

# Evaluating the accuracy of the model and printing it
accuracy = (y_pred == y_test).mean()
print("Accuracy:", accuracy)

# Get the tree structure as text
tree_text = export_text(clf, feature_names=X.columns.tolist(), show_weights=True, spacing=3, decimals=1)

# Generate the decision tree graph
dot_data = StringIO()
dot_data.write("digraph Tree {\nnode [shape=box] ;\n")
dot_data.write(tree_text)
dot_data.write("}")

# Save the graph as an image
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_jpg('decision_tree.jpg')
