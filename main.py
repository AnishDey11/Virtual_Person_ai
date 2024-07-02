import google.generativeai as genai
from apigemini import API_KEY
from tkinter import *

name = ''
user_name = ''
region = ''
language = ''
relation = ''

def save_input():
  global user_name, name, region, language, relation
  user_name = entry_your_name.get()
  name = entry_person_name.get()
  region = entry_region.get()
  language = entry_language.get()
  relation = entry_relation.get()

  input_window.destroy()  

input_window = Tk()
input_window.geometry('400x300')
input_window.title("Input Details")

input_window.grid_columnconfigure(1, weight=1)

label_your_name = Label(input_window, text="Your Name:")
label_your_name.grid(row=0, column=0, padx=10, pady=5, sticky=E)
entry_your_name = Entry(input_window, width=30)
entry_your_name.grid(row=0, column=1, padx=10, pady=5)

label_person_name = Label(input_window, text="Person's Name:")
label_person_name.grid(row=1, column=0, padx=10, pady=5, sticky=E)
entry_person_name = Entry(input_window, width=30)
entry_person_name.grid(row=1, column=1, padx=10, pady=5)

label_region = Label(input_window, text="Region:")
label_region.grid(row=2, column=0, padx=10, pady=5, sticky=E)
entry_region = Entry(input_window, width=30)
entry_region.grid(row=2, column=1, padx=10, pady=5)

label_language = Label(input_window, text="Language:")
label_language.grid(row=3, column=0, padx=10, pady=5, sticky=E)
entry_language = Entry(input_window, width=30)
entry_language.grid(row=3, column=1, padx=10, pady=5)

label_relation = Label(input_window, text="Relation:")
label_relation.grid(row=4, column=0, padx=10, pady=5, sticky=E)
entry_relation = Entry(input_window, width=30)
entry_relation.grid(row=4, column=1, padx=10, pady=5)

submit_button = Button(input_window, text="Submit", command=save_input)
submit_button.grid(row=5, columnspan=2, pady=20)

input_window.mainloop()

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


