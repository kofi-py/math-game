#!"C:\Python310\python.exe"
from tkinter import *

# Setup game
root = Tk()
root.title("Math Quiz")
root.geometry("500x500")

givenAnswer = IntVar()

# Title 
titleLabel = Label(
    text="Math Quiz",
    font=("Arial Black", 40),
    bg="yellow",
    relief=SUNKEN,
    borderwidth=10)
titleLabel.grid(row=0, column=0)


# Question Label
questionLabel = Label(
    text="question",
    font=("Arial", 40),
    bg="#83c167",
    relief=SUNKEN,
    borderwidth=10)
questionLabel.grid(row=1, column=0)

# Answer Entry
answerEntry = Entry(
    textvariable=givenAnswer,
    font=("Arial Bold", 30),
    bg="#58c4dd",
    relief=SUNKEN,
    borderwidth=10,
)
answerEntry.grid(row=2, column=0)
# Submit Button
submitButton = Button(
    text="Submit",
    font=("Carlito Bold", 30),
    bg="white",
    relief=RAISED,
    borderwidth=10
)
submitButton.grid(row=3, column=0)
# Score Label
scoreLabel = Label(
    text= "0 / 10",
    font=("Arial Black", 40),
)
scoreLabel.grid(row=4, column=0)
# Game loop
root.mainloop()
