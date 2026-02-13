# 📚 Flashcard Learning App

A simple command-line Flashcard Learning Application built using Python.  
It allows users to add, review, and mark flashcards as learned using a JSON file for storage.

---

## 🚀 Features

- Add new flashcards
- Review unlearned flashcards
- Mark flashcards as learned
- Stores data in a JSON file
- Simple menu-driven interface

---

## 🛠️ Requirements

- Python 3.x  
- No external libraries required (uses built-in `json` module)

---

## 📂 Project Structure

Flashcard_Tool.py
flashcard.json
README.md


---

## 📦 Data Storage Format

Flashcards are stored in `flashcard.json` as:

```json
[
    {
        "question": "What is Python?",
        "answer": "programming language",
        "learned": false
    }
]
Fields:
question → The flashcard question

answer → The correct answer

learned → Boolean value (true or false)

▶️ How to Run
Make sure Flashcard_Tool.py is in your directory.

Run the program:

python Flashcard_Tool.py
Choose from the menu:

1 - Add flashcard
2 - Review flashcard
3 - Mark flashcard as learned
4 - Exit
🧠 How It Works
1️⃣ load_flashcards()
Loads flashcards from flashcard.json

Returns empty list if file does not exist

2️⃣ save_flashcards()
Saves flashcards into JSON file

Formats JSON using indentation

3️⃣ add_flashcards()
Takes user input (question & answer)

Stores new flashcard with "learned": False

4️⃣ review_flashcards()
Displays first unlearned flashcard

Checks user answer

Shows correct answer if wrong

5️⃣ mark_as_learned()
Displays first unlearned flashcard

Marks it as learned if user enters "yes"

6️⃣ main()
Displays menu

Runs program in loop until user exits

📌 Example Output
Welcome to the flashcard learning app
1-add flashcard
2-review flashcard
3-mark flashcard
4-exit
Enter your choice: 1
Enter the question you want to add: What is AI?
Enter the answer of that question: artificial intelligence
Successfully saved the flashcard
