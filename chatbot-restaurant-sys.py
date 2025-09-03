import re
import dateparser
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

menu = {
    "Starters": ["Spring Rolls", "Garlic Bread", "Chicken Wings"],
    "Main Course": ["Grilled Chicken", "Beef Steak", "Paneer Tikka Masala"],
    "Desserts": ["Brownie", "Ice Cream", "Cheesecake"],
    "Drinks": ["Coke", "Orange Juice", "Mint Margarita"]
}

training_sentences = [
    "hello", "hi there", "good morning",
    "book a table", "i want to reserve a table", "make a booking for dinner",
    "bye", "see you later", "goodbye",
    "show me the menu", "what do you have", "list the dishes", "i want to see the food menu"
]

training_labels = [
    "greeting", "greeting", "greeting",
    "booking", "booking", "booking",
    "goodbye", "goodbye", "goodbye",
    "menu", "menu", "menu", "menu"
]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(training_sentences)
model = MultinomialNB()
model.fit(X, training_labels)

def predict_intent(user_input):
    X_test = vectorizer.transform([user_input])
    prediction = model.predict(X_test)
    return prediction[0]

def extract_booking_details(text):
    text = text.lower()

    people_match = re.search(r'\bfor (\d+)|(\d+)\s+people\b', text)
    people = None
    if people_match:
        people = people_match.group(1) or people_match.group(2)

    time_match = re.search(r'\b(at\s*)?(\d{1,2}(:\d{2})?\s*(am|pm))\b', text)
    time = None
    if time_match:
        time = time_match.group(2)

    parsed_date = dateparser.parse(text)
    formatted_date = parsed_date.strftime('%Y-%m-%d') if parsed_date else None

    return {
"people": people,
        "time": time,
        "date": formatted_date
    }

def run_chatbot():
    print("ChatBot: Hello! I’m your restaurant assistant. How can I help you today?")
    booking_context = {"people": None, "date": None, "time": None}

    while True:
        user_input = input("You: ").lower()
        intent = predict_intent(user_input)

        new_details = extract_booking_details(user_input)
        found_booking_info = any(new_details.values())

        if intent == "greeting":
            print("ChatBot: Hello there! How can I assist you with a booking or show you our menu?")

        elif intent == "booking" or found_booking_info:
            for key in booking_context:
                if new_details[key]:
                    booking_context[key] = new_details[key]

            print(f"ChatBot: Got it! So far — people: {booking_context['people'] or 'unknown'}, date: {booking_context['date'] or 'unknown'}, time: {booking_context['time'] or 'unknown'}")

            if all(booking_context.values()):
                print(f"ChatBot:  Confirmed! Booking a table for {booking_context['people']} on {booking_context['date']} at {booking_context['time']}.")
                booking_context = {"people": None, "date": None, "time": None}

        elif intent == "menu":
            print("ChatBot: Here's our menu:\n")
            for category, items in menu.items():
                print(f"{category}:")
                for item in items:
                    print(f"  - {item}")
                print()

        elif intent == "goodbye":
            print("ChatBot: Goodbye! Have a delicious day. ")
            break

        else:
            print("ChatBot: I'm not sure how to respond to that. You can ask about booking or our menu.")

run_chatbot()

