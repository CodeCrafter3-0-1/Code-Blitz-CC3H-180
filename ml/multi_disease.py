# FILE NAME:
# ml/multi_disease.py

def calculate_multi_disease(age, bp, sugar, weight, smoking, exercise):

    # ==================================
    # BMI CALCULATION
    # assuming avg height = 1.70 meter
    # ==================================
    bmi = round(weight / (1.70 * 1.70), 1)

    # ==================================
    # HEART RISK
    # ==================================
    heart_score = 0

    if age > 45:
        heart_score += 20

    if bp > 140:
        heart_score += 35

    if smoking == 1:
        heart_score += 25

    if exercise == 0:
        heart_score += 15

    if bmi > 28:
        heart_score += 10

    if heart_score > 100:
        heart_score = 100


    # ==================================
    # DIABETES RISK
    # ==================================
    diabetes_score = 0

    if sugar > 140:
        diabetes_score += 45

    if weight > 85:
        diabetes_score += 20

    if age > 40:
        diabetes_score += 15

    if exercise == 0:
        diabetes_score += 10

    if smoking == 1:
        diabetes_score += 10

    if diabetes_score > 100:
        diabetes_score = 100


    # ==================================
    # RESPIRATORY RISK
    # ==================================
    respiratory_score = 0

    if smoking == 1:
        respiratory_score += 50

    if age > 50:
        respiratory_score += 20

    if exercise == 0:
        respiratory_score += 15

    if weight > 90:
        respiratory_score += 15

    if respiratory_score > 100:
        respiratory_score = 100


    # ==================================
    # OBESITY RISK
    # ==================================
    obesity_score = 0

    if bmi >= 30:
        obesity_score = 90

    elif bmi >= 27:
        obesity_score = 75

    elif bmi >= 25:
        obesity_score = 60

    elif bmi >= 23:
        obesity_score = 35

    else:
        obesity_score = 15


    # ==================================
    # OVERALL SCORE
    # ==================================
    overall = round(
        (heart_score + diabetes_score +
         respiratory_score + obesity_score) / 4
    )


    # ==================================
    # RETURN DATA
    # ==================================
    return {
        "bmi": bmi,
        "heart_score": heart_score,
        "diabetes_score": diabetes_score,
        "respiratory_score": respiratory_score,
        "obesity_score": obesity_score,
        "overall_score": overall
    }