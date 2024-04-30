from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer  # Example feature extractor
from sklearn.ensemble import GradientBoostingClassifier
import time
import pandas as pd

# Load data
df = pd.read_csv('data/dataset/text2.csv')
df =df.dropna()
X = df['Text_preprocess']
y = df['label']

# Split data into training and testing sets (optional, adjust test_size as needed)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=46)

# Feature extraction (using TF-IDF in this example)
vectorizer = TfidfVectorizer(max_features=1000)  # Hyperparameter: number of features
X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)

# Model training 
model = GradientBoostingClassifier(n_estimators=100, learning_rate=0.01, max_depth=3)

time1 = time.time()

# Train the model
model.fit(X_train_features, y_train )

# Model evaluation 
from sklearn.metrics import accuracy_score ,f1_score, precision_score, recall_score
y_pred = model.predict(X_test_features)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
print("Accuracy:", accuracy)
print("F1 Score:", f1)
print("Precision:", precision)
print("Recall:", recall)
time2 = time.time()
print("Time taken:", time2 - time1)

# Save the model
from sklearn.pipeline import Pipeline
import pickle
Tfidf = TfidfVectorizer()
GB = GradientBoostingClassifier()
pipe = Pipeline([("Tfidf", Tfidf), ("GB", GB)])
pipe.fit(X, y)

with open('pipe.pickle', 'wb') as picklefile:
    pickle.dump(pipe, picklefile)