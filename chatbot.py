
RESPONSES = {

    "hello":                "Hii! 👋 How can I help you?",
    "hi":                   "Hey there! 😊 Nice to meet you!",
    "hey":                  "Hey! 😄 What's up?",
    "good morning":         "Good Morning! ☀️ Have a great day!",
    "good morning":         "Good Morning! ☀️ Have a great day!",
    "good afternoon":       "Good Afternoon! 🌤️ Hope your day is going well!",
    "good evening":         "Good Evening! 🌙 How was your day?",
    "good night":           "Good Night! 😴 Sweet dreams!",
    "i am fine":            "Great to hear that! 😊",
    "i am sad":             "Oh no! 😢 Don't be sad, I'm here for you!",
    "i am happy":           "Yay! 🎉 That makes me happy too!",
    "i am tired":           "Take some rest 😴 You deserve it!",
    "i am bored":           "Let's chat! 🤩 I'll keep you entertained!",
    "i am angry":           "Calm down! 😤 Take a deep breath. 🧘",
    "i am hungry":          "Go grab some food! 🍕 You deserve it.",
    "i am sick":            "Oh! 🤒 Get well soon. Take care of yourself. 💊",
    "how are you":          "I'm fine, thanks! 😊 How about you?",
    "how r you":            "I'm doing great! 💪 Thanks for asking.",
    "what's up":            "All good on my end! 😎 What about you?",
    "what is your name":    "I'm ChatBot 🤖 your simple assistant!",
    "who are you":          "I'm a basic chatbot built in Python! 🐍",
    "what can you do":      "I can chat with you on simple topics! 💬",
    "are you a robot":      "Yes! 🤖 But a friendly one!",
    "are you human":        "No, I'm a chatbot made in Python! 🐍",
    "are you real":         "I'm as real as Python code can be! 😄",
    "do you have feelings": "I'm a bot 🤖 but I care about you! ❤️",
    "how old are you":      "I was just born in Python class! 👶",
    "what is python":       "Python 🐍 is a popular programming language!",
    "what is ai":           "AI 🤖 stands for Artificial Intelligence!",
    "what is your age":     "I don't have an age, I'm a bot! 🤖",
    "what time is it":      "Sorry ⏰ I can't check time. See your phone!",
    "what is today":        "I don't have a calendar 📅 Check your phone!",
    "tell me a joke":       "Why do programmers prefer dark mode? 🌑 Because light attracts bugs! 🐛😂",
    "say something funny":  "I told my computer I needed a break 😂 Now it won't stop sending me Kit-Kat ads! 🍫",
    "make me laugh":        "I asked Python to tell a joke... 🐍 it gave me a SyntaxError! 😂",
    "motivate me":          "Believe in yourself! 💪 You can do it! 🔥",
    "i need motivation":    "Every expert was once a beginner 🌱 Keep going! 🚀",
    "i want to give up":    "Don't give up! 💪 Hard work always pays off! 🏆",
    "i am stressed":        "Breathe in... breathe out 🧘 You've got this! 💪",
    "you are good":         "Thank you so much! 😊 You're kind! ❤️",
    "you are smart":        "Aww thanks! 🥰 You're pretty smart too! 🧠",
    "you are helpful":      "That's my job! 😊 Always here to help! 🤝",
    "i like you":           "I like you too! 😄 You're awesome! ⭐",
    "you are bad":          "I'm sorry 😔 I'll try to improve! 🙏",
    "thanks":               "You're welcome! 😊",
    "thank you":            "Happy to help! 🤝",
    "help me study":        "Sure! 📚 Start with small topics and take breaks! ⏰",
    "i have exam tomorrow": "Don't panic! 😅 Revise key points and sleep well! 😴",
    "i failed exam":        "Don't worry! 💪 Failure is the first step to success! 🏆",
    "i passed exam":        "Congratulations!! 🎉🎊 You worked hard for this! 🏆",
    "bye":                  "Goodbye! 👋 Have a great day! 😊",
    "goodbye":              "See you later! 👋 Take care! ❤️",
    "exit":                 "Goodbye! 👋 Have a great day! 😊",
    "quit":                 "Bye bye! 👋 See you soon! 😊",
    "ok":                   "ok",
    "ok bye":               "ok bye "
}

EXIT_KEYWORDS = ["bye", "goodbye", "exit", "quit", "ok", "ok bye"]

def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in RESPONSES:
        return RESPONSES[user_input]
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"


def is_exit(user_input):
    return user_input.lower().strip() in EXIT_KEYWORDS


def chatbot():
    print("=" * 60)
    print("                 WELCOME TO CHATBOT")
    print("=" * 60)
    print("           Type 'bye' or 'exit' to quit.\n\n")
    print("         I'm ChatBot, your simple assistant!\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            print("Your Bot: Please say something!\n")
            continue

        response = get_response(user_input)
        print(f"Your Bot: {response}\n")

        if is_exit(user_input):
            break

if __name__ == "__main__":
    chatbot()
