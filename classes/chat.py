from classes.user import User
import spacy

# Load the model
nlp = spacy.load("en_core_web_sm")


class Chat:
    def __init__(self, user):
        self.user = user

    def initialize_chatbot(self):
        print("Welcome to our chatbot for determining loan acceptance!")
        hours_per_week_input = input("How many hours do you work a week? ")
        hours_per_week_input = self.extract_hours(hours_per_week_input)
        self.user.set_hours_per_week(hours_per_week_input)

        if self.check_age() and self.check_hours():
            print("Congratulations! Your loan has been accepted.")


    def extract_hours(self, input_text):
        doc = nlp(input_text)
        for token in doc:
            if token.like_num:
                return int(token.text)
        print("I couldn't understand the number of hours worked. Please enter a valid number.")
        return None

    def check_age(self):
        age = self.user.get_age()
        if age is not None and age < 18:
            print("You must be over 18 to be eligible for a loan.")
            return False
        return True


    def check_hours(self):
        hours_per_week = self.user.get_hours_per_week()
        if hours_per_week is not None and hours_per_week < 18:
            # Advises the user
            print("If you change your hours from " + str(hours_per_week) + " to 18 your loan would approved.")

            return False
        return True
