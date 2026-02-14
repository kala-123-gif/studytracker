def predict_days(difficulty, daily_hours):
    if difficulty == "easy":
        total_hours = 10
    elif difficulty == "medium":
        total_hours = 25
    else:
        total_hours = 40

    return round(total_hours / daily_hours, 1)

print("Study Time Predictor")

difficulty = input("Enter difficulty (easy/medium/hard): ")
daily_hours = float(input("Enter daily study hours: "))

days = predict_days(difficulty, daily_hours)

print("Estimated days needed:", days)
