from keras.models import Sequential
from keras.layers import Dense, LSTM , Embedding,Bidirectional
from sklearn.model_selection import train_test_split


#import csv file
import pandas as pd
csv_file = r"C:\Users\NANDHANA ESBEE\Desktop\CHATViBE\chatvibe\data\dataset\text.csv"
df = pd.read_csv(csv_file)
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Initialize models
model = Sequential()

#add layers
model.add(Embedding(input_dim=100, output_dim=64))
model.add(LSTM(64, return_sequences=True))  
model.add(LSTM(64))
#model.add(Bidirectional(LSTM(64)))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

#evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {test_acc:.4f}")

#predict the model
predict = model.predict()
print(predict)

# Print the model summary
print(model.summary())
# Save the model
#model.save('model1.keras')
