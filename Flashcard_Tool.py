import json

def load_flashcards(file_path="flashcard.json"):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError):
        return []

def save_flashcards(flashcards,file_path="flashcard.json"):
    try:
        with open(file_path,"w") as file:
            json.dump(flashcards,file,indent=4)
    except FileNotFoundError:
        print("file is not found")

def add_flashcards():
    question=input("enter the questions you want to add")
    answer=input("enter the answer of that question")
    flashcards=load_flashcards()
    flashcards.append({"question":question,"answer":answer,"learned":False})
    save_flashcards(flashcards)
    print("successfully saved the flashcard")

def review_flashcards():
    flashcards=load_flashcards()
    for card in flashcards:
        if not card["learned"]:
            print(card["question"])
            answer=input("enter the answer")
            if answer.lower() == card["answer"]:
                print("correct answer")
            else:
                print(f"wrong, correct answer is {card['answer']}")
            return
    print("no more flashcards reviewed")

def mark_as_learned():
    flashcards=load_flashcards()
    for card in flashcards:
        if not card["learned"]:
            print(card["question"])
            answer=input("did you learn this question(yes/no)")
            if answer=="yes":
                card["learned"]=True
                save_flashcards(flashcards)
                print("successfully updated the question")
                return
    print("no more flashcards to learn")

def main():
    print("welcome to the flashcard learning app")
    while True:
        print("1-add flashcard")
        print("2-review flashcard")
        print("3-mark flashcard")
        print("4-exit")
        choice=int(input("enter your choice"))
        if choice==1:
            add_flashcards()
        elif choice==2:
            review_flashcards()
        elif choice==3:
            mark_as_learned()
        elif choice==4:
            print("goodbye")
            break
        else:
            print("invaid choice")

if __name__=="__main__":
    main()
