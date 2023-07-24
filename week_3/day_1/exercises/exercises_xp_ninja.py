class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []
        print(f"New phone registered: {self.phone_number}")

    def call(self, other_phone):
        call_str = f"{self.phone_number} called {other_phone.phone_number}."
        print(call_str)
        self.call_history.append(call_str)
        other_phone.call_history.append(call_str)
        # other_phone.show_call_history()

    def show_call_history(self):
        print(self.call_history)

    def send_message(self, other_phone, msg):
        message = {
            "from": self.phone_number,
            "to": other_phone.phone_number,
            "content": msg,
        }
        self.messages.append(message)
        other_phone.messages.append(message)


v_phone = Phone(52560909)
b_phone = Phone(58372920)
a_phone = Phone(52863072)

v_phone.call(b_phone)
v_phone.call(b_phone)
v_phone.call(b_phone)
v_phone.call(b_phone)
# print(v_phone.call_history)
v_phone.show_call_history()

# b_phone.send_message(a_phone, "Hey dude, wanna grab lunch?")
# b_phone.send_message(a_phone, "What a bummer, I really wanted to have lunch with you")
# v_phone.send_message(b_phone, "Hey I heard Anas declined your offer, I want free food.")
# print(b_phone.messages)
# print("-------------------------------")
# print(v_phone.messages)
# print("-------------------------------")
# print(a_phone.messages)
