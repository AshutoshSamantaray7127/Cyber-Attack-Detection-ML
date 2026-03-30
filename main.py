print("Step 1: Starting")

from src.preprocessing import load_and_preprocess
print("Step 2: Imported preprocessing")

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

print("Step 3: Loading data")
X_train, X_test, y_train, y_test = load_and_preprocess()

print("Step 4: Data Loaded")
print("Feature count:", X_train.shape[1])
model = RandomForestClassifier()

print("Step 5: Training started")
model.fit(X_train, y_train)

print("Step 6: Training done")

y_pred = model.predict(X_test)

print("Step 7: Prediction done")

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

joblib.dump(model, "models/best_model.pkl")

print("Step 8: Model saved")