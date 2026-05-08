def calculate_bmi(weight, height):
    return weight / (height ** 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def health_advice(category):
    if category == "Underweight":
        return "You may need to increase calorie intake and focus on strength training."
    elif category == "Normal":
        return "Great! Maintain a balanced diet and regular exercise."
    elif category == "Overweight":
        return "Consider cardio workouts and reducing sugar intake."
    else:
        return "High risk. Consult a healthcare professional and adopt a structured fitness plan."


def main():
    print("=== BMI Calculator ===")

    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Invalid input. Values must be greater than zero.")
            return

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        advice = health_advice(category)

        print("\n--- Results ---")
        print(f"BMI Value: {round(bmi, 2)}")
        print(f"Category: {category}")
        print(f"Advice: {advice}")

    except ValueError:
        print("Please enter valid numeric inputs.")


if __name__ == "__main__":
    main()