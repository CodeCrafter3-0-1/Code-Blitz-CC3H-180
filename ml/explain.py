# FILE: ml/explain.py

def explain_risk(age, bp, sugar, weight, smoking, exercise):

    reasons = []

    if age > 45:
        reasons.append("Age factor may increase health risk.")

    if bp > 140:
        reasons.append("Blood pressure is above healthy range.")

    if sugar > 140:
        reasons.append("Blood sugar appears elevated.")

    if weight > 85:
        reasons.append("Weight is above recommended range.")

    if smoking == 1:
        reasons.append("Smoking habit increases heart and lung risk.")

    if exercise == 0:
        reasons.append("Low physical activity detected.")

    if len(reasons) == 0:
        reasons.append("All major vitals appear within safer range.")

    return reasons