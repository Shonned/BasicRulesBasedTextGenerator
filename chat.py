import spacy

nlp = spacy.load("en_core_web_sm")

def main():
    print("Welcome to our chatbot for determining loan acceptance!")

    age = None
    while age is None:
        age_input = input("Quel est votre âge ? ")
        age = extract_age(age_input)
        if age is not None and age < 18:
            print("You must be over 18 to be eligible for a loan.")
            return

    hours_per_week = None
    while hours_per_week is None:
        hours_per_week_input = input("How many hours do you work a week?")
        hours_per_week = extract_hours(hours_per_week_input)
        if hours_per_week is not None and hours_per_week <= 18:
            print("If you change your hours from " + str(hours_per_week) + " to 18 your loan would approved.")
            return

    print("Congratulations! Your loan has been accepted.")


def extract_age(input_text):
    doc = nlp(input_text)
    for token in doc:
        if token.like_num:
            return int(token.text)
    print("I couldn't understand your age. Please enter a valid number.")
    return None


def extract_hours(input_text):
    doc = nlp(input_text)
    for token in doc:
        if token.like_num:
            return int(token.text)
    print("I couldn't understand the number of hours worked. Please enter a valid number.")
    return None


if __name__ == "__main__":
    main()
