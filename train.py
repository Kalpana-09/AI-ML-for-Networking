# train.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
from feature_extraction import load_and_clean_dataset

# Load and combine both datasets
path1 = r"C:\Network security\dataset\large_sample_network_data.csv"
path2 = r"C:\Network security\dataset\training_dataset_full.csv"

df1 = load_and_clean_dataset(path1)
df2 = load_and_clean_dataset(path2)

# Merge both into a single DataFrame
df = pd.concat([df1, df2], ignore_index=True)
print(f" Combined dataset shape: {df.shape}")

# Split features and label
X = df.drop(columns=['Label'])
y = df['Label'].astype(str)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("\n Classification Report:")
print(classification_report(y_test, y_pred))
print(" Accuracy:", accuracy_score(y_test, y_pred))

# Save model
joblib.dump(model, "rf_model.pkl")
print(" Model saved as rf_model.pkl")
