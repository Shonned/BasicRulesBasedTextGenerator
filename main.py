from classes.user import User
from classes.chat import Chat


def main():
    user_data = {
        "name": "Kilian",
        "lastname": "Peyron",
        "age": 20,
        "email": "kilianpeyn@gmail.com",
        "phone": "0782647212",
        "address": "100 Hillview Rd",
        "city": "Peterculter",
        "state": "Aberdeen",
        "country": "Scotland"
    }

    user = User(**user_data)
    user.set_jobs("Web developer")

    chat = Chat(user)
    chat.initialize_chatbot()

if __name__ == "__main__":
    main()
