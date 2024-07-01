from tkinter import *
from tkinter import scrolledtext
from main import chatting, name

def send_chat(event=None):
    prompt = chat_text.get('1.0', END).strip()
    if prompt:
        chat_text.delete('1.0', END)
        response = chatting(prompt)
        display_msg(prompt, response)

def display_msg(msg, response):
    chats.config(state='normal')
    chats.insert(END, f'You: {msg}\n', 'user')
    chats.insert(END, f'{name.title()}: {response}\n', 'friend')
    chats.yview(END)
    chats.config(state='disabled')

window = Tk()
window.geometry('760x560')
window.title("Chat App")

chat_text_frame = Frame(window, height=50, width=760)
chat_text_frame.pack_propagate(False)
chat_text_frame.pack(side=BOTTOM, fill=X)

chat_text = Text(chat_text_frame, width=62, height=1, font=("Arial", 15), padx=2, pady=5)
chat_text.pack_propagate(False)
chat_text.pack(side=LEFT, pady=5, padx=2)
chat_text.bind('<Return>', lambda event: send_chat(event) or 'break')

send_button = Button(chat_text_frame, text='Send', height=2, width=8, command=send_chat)
send_button.pack(side=RIGHT, padx=2, pady=2)

chat_show_frame = Frame(window, height=510, width=760)
chat_show_frame.pack_propagate(False)
chat_show_frame.pack(side=TOP, fill=BOTH, expand=True)

chats = scrolledtext.ScrolledText(chat_show_frame, wrap=WORD, state='disabled', font=("Arial", 12))
chats.pack(fill=BOTH, expand=True)
chats.tag_configure('user', foreground='blue')
chats.tag_configure('friend', foreground='green')

window.mainloop()
