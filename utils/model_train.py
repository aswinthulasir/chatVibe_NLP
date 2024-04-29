from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer  # Example feature extractor
from sklearn.linear_model import LogisticRegression  # Example classifier
from sklearn.ensemble import GradientBoostingClassifier

import pandas as pd

df = pd.read_csv('data/dataset/text2.csv')
df =df.dropna()
# Load your data (replace with your data loading logic)
X = df['Text_preprocess']
# ["This is a positive sentiment sentence.",
#      "This is a negative sentiment sentence.",
#      "This is a neutral statement."]  # Sample text data
y = df['label']
#[1, 2, 0]  # Sample labels (1: positive, 0: negative)

# Split data into training and testing sets (optional, adjust test_size as needed)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=46)

# Feature extraction (using TF-IDF in this example)
vectorizer = TfidfVectorizer(max_features=1000)  # Hyperparameter: number of features
X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)

# Model training (using Logistic Regression in this example)
# Create the GradientBoostingClassifier model
model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.01, max_depth=3)


# Train the model on the features and labels
model.fit(X_train_features, y_train )

# Model evaluation (using accuracy in this example)
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test_features)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


#model = LogisticRegression(solver='lbfgs')  # Choose appropriate solver
#model.fit(X_train_features, y_train)



# Make predictions on new data (optional)
# new_text = "I am feeling okay."
# new_text_features = vectorizer.transform([new_text])
# prediction = model.predict(new_text_features)
# print("Predicted sentiment:", prediction[0])
 
# for item in df['text']:
#     new_text_features = vectorizer.transform([item])
#     prediction = model.predict(new_text_features)
#     print("Predicted sentiment:", prediction[0])
#     print(item)
#     print('------------------')