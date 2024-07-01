from tkinter import *
from main import chatting

def send_chat():
    prompt = chat_text.get('1.0', END)
    chat_text.delete('1.0', END)
    response = chatting(prompt)
    print(response)

window = Tk()
window.geometry('760x560')

chat_text_frame = Frame(window, height=50, width=760)
chat_text_frame.pack_propagate(False)
chat_text_frame.pack(side=BOTTOM)

chat_text = Text(chat_text_frame, width=85, height=3)
chat_text.pack_propagate(False)
chat_text.pack(side=LEFT, pady=5, padx=2)

send_button = Button(chat_text_frame, text='send', height=3, width=8, command=send_chat)
send_button.pack(side=RIGHT, padx=2, pady=2)

window.mainloop()