# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load CSV without headers
df = pd.read_csv("indian_liver_patient.csv", header=None)

# Assign column names manually
df.columns = [
    'Age', 'Gender', 'Total_Bilirubin', 'Direct_Bilirubin',
    'Alkaline_Phosphotase', 'Alamine_Aminotransferase',
    'Aspartate_Aminotransferase', 'Total_Proteins', 'Albumin',
    'Albumin_and_Globulin_Ratio', 'Dataset'
]

# Convert categorical 'Gender' to numeric (optional, not used in prediction here)
df.dropna(inplace=True)
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})

# Convert target: 1 = disease, 2 = no disease
df['Dataset'] = df['Dataset'].map({1: 1, 2: 0})

# Select features and target
X = df[['Total_Bilirubin', 'Direct_Bilirubin', 'Alkaline_Phosphotase',
        'Alamine_Aminotransferase', 'Total_Proteins', 'Albumin', 'Albumin_and_Globulin_Ratio']]
y = df['Dataset']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Save model
joblib.dump(clf, "liver_disease_model.pkl")
print("✅ Model trained and saved as 'liver_disease_model.pkl'")
