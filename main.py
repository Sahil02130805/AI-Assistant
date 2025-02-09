import google.generativeai as ai

API_KEY = 'AIzaSyCSvB4tA4RoTL5SXGoRo6cNTvM8zsKfY3Y'

ai.configure(api_key=API_KEY)

model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

while True:
    message = input("You: ")
    if message.lower() == 'bye':
        print("Gemini: Goodbye!")
        break
    response = chat.send_message(message)
    print("Gemini: " + response.text)