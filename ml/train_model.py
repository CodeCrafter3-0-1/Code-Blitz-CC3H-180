import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

np.random.seed(42)

rows = 1000

data = []

for i in range(rows):

    age = np.random.randint(18, 80)
    bp = np.random.randint(100, 190)
    sugar = np.random.randint(70, 250)
    weight = np.random.randint(45, 120)
    smoking = np.random.randint(0, 2)
    exercise = np.random.randint(0, 2)

    risk = 0

    if age > 45:
        risk += 1

    if bp > 145:
        risk += 1

    if sugar > 145:
        risk += 1

    if weight > 90:
        risk += 1

    if smoking == 1:
        risk += 1

    if exercise == 0:
        risk += 1

    if risk <= 1:
        label = 0     # Low

    elif risk <= 3:
        label = 1     # Medium

    else:
        label = 2     # High

    data.append([
        age, bp, sugar, weight, smoking, exercise, label
    ])

df = pd.DataFrame(data, columns=[
    "age", "bp", "sugar", "weight",
    "smoking", "exercise", "risk"
])

X = df.drop("risk", axis=1)
y = df["risk"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

acc = accuracy_score(y_test, pred)

joblib.dump(model, "ml/model.pkl")

print("Model Trained Successfully")
print("Accuracy:", round(acc * 100, 2), "%")