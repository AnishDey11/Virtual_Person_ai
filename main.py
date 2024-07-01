import google.generativeai as genai
from apigemini import API_KEY
from tkinter import *
from tkinter import simpledialog

window = Tk()
window.withdraw()

user_name = simpledialog.askstring("Input", 'Your Name: ')
name = simpledialog.askstring("Input", 'Persons name: ')
language = simpledialog.askstring("Input", 'Language you want to use: ')
region = simpledialog.askstring("Input", 'Where the person from: ')
relation = simpledialog.askstring("Input", 'Relation with you: ')

window.destroy()

genai.configure(api_key=API_KEY)

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 0,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.0-pro",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        f"You have to act like a person named {name}, you are my {relation}, you are from {region}, you know {language}, by the way my name is {user_name}, you need to act like the person and chat like normal human make responses small.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hey! 😊 What's up? \n",
      ],
    },
  ]
)

def chatting(chat):
    response = chat_session.send_message(chat)
    return response.text

if __name__ == '__main__':
  user_name = input('Your name: ')
  name = input('Persons name: ')
  region = input('Where are you form: ')
  language = input('Language you want to use: ')
  relation = input('Relation: ')

  while True:
    chat = input("<<< ")
    response = chatting(chat)
    print(response)


