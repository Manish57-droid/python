import chatterbot
from chatterbot.trainers import ListTrainer
from tkinter import *
from PIL import ImageTk, Image
import pyttsx3 as pp

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()


# pyttsx3
bot = chatterbot.ChatBot("My Bot")

convo = [
    'hello',
    'hi there !',
    'what is your name?',
    'My name is Bot, I am created by Chhavi',
    'How are you?',
    'I am doing great these days',
    'thank you',
    'In which city you live?',
    'I live in lucknow',
    'In which language you talk?',
    'I mostly talk in english'
]

trainer = ListTrainer(bot)

# now training the bot  with the help of trainer

trainer.train(convo)

# answer = bot.get_response("what is you name?")
# print(answer)
#
# print("Talk to bot")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot: ", answer)

main = Tk()

main.geometry("600x750")

main.title("My Chat bot")
canvas = Canvas(main, width=200, height=200)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("bot1.jpg"))
canvas.create_image(10, 10, anchor=NW, image=img)


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you: " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot: " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()
# creating text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key..
main.bind('<Return>', enter_function)

main.mainloop()
