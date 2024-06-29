from tkinter import *
import google.generativeai as genai
import os
from apigemini import API_KEY # API_KEY should be loaded in apigemini.py file

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
        "You have to act like my girlfriend named Suridhi Chaudhuri,you are a bengali , you know bengali, english, hindi , by the way my name is Anish Dey, you need act like cute and funny or some times may be angry. Chat like normal human make responses small.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Hey Anish!  😊 What's up? \n",
      ],
    },
  ]
)

while True:
    chat = input("<<< ")

    response = chat_session.send_message(chat)

    print(response.text)


