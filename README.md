````markdown
# AI Restaurant Chatbot System

An interactive *restaurant booking assistant chatbot* built with Python, scikit-learn, and regex-based NLP.  
The chatbot can greet customers, show the menu, handle table booking requests, and extract booking details (date, time, and number of people).

---

## Features
- **Greetings**: Responds to basic greetings.
- **Menu Display**: Lists available items in Starters, Main Course, Desserts, and Drinks.
- **Table Booking**:
  - Detects booking intent from user queries.
  - Extracts number of people, date, and time using regex and `dateparser`.
  - Confirms booking once all details are provided.
- **Goodbye Handling**: Politely ends the conversation.

---

## Technologies Used
- **Python 3**
- **scikit-learn** (Naive Bayes for intent classification)
- **TfidfVectorizer** (for text feature extraction)
- **Regex** (for extracting structured booking details)
- **dateparser** (for parsing natural language date/time inputs)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-chatbot-restaurant-system.git
   cd ai-chatbot-restaurant-system
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   **requirements.txt**

   ```
   scikit-learn
   dateparser
   ```

---

## Usage

Run the chatbot:

```bash
python chatbot.py
```

Sample interaction:

```
ChatBot: Hello! I’m your restaurant assistant. How can I help you today?
You: I want to book a table for 2 people tomorrow at 7 pm
ChatBot: Got it! So far — people: 2, date: 2025-09-03, time: 7 pm
ChatBot: Confirmed! Booking a table for 2 on 2025-09-03 at 7 pm.
```

---

## Example Menu

```
Starters:
  - Spring Rolls
  - Garlic Bread
  - Chicken Wings

Main Course:
  - Grilled Chicken
  - Beef Steak
  - Paneer Tikka Masala

Desserts:
  - Brownie
  - Ice Cream
  - Cheesecake

Drinks:
  - Coke
  - Orange Juice
  - Mint Margarita
```

---

## License

This project is available under the MIT License.

```
