import joblib

# Load model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

print("=== Spam Detection Chatbot ===")

while True:
    user_input = input("\nEnter a message: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    transformed = vectorizer.transform([user_input])
    prediction = model.predict(transformed)[0]

    if prediction == 1:
        print("⚠ Spam Message Detected")
    else:
        print("✅ Normal Message")