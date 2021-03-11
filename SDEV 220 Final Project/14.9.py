"""
Mwai Banda
SDEV 220  Exercise 14.9  Page 497
Hangman
Due August 2, 2020.
"""

import words
import random
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase


class Hangman:
    def __init__(self):
        window = Tk()
        window.title("Hangman Game")

        # Store hangman PNGs
        photos = []
        for i in range(0, 12):
            photos.append(PhotoImage(file="images/hang" + str(i) + ".png"))

        # Store missed char
        global missedTextList
        missedTextList = []

        # Enter Key to restart game
        def enterKey(event):
            newGame()

        window.bind("<Return>", enterKey)
        window.focus_set()

        # Start new game
        def newGame():
            global dashedWord
            global numberOfGuess
            global word
            global hintText
            numberOfGuess = 4  # Initialize number of guess to allow 7 times
            imageLabel.config(image=photos[4])
            word = random.choice(words.wordList)  # pick random word
            word = word.upper()  # convert word to uppercase
            dashedWord = " ".join(word)
            LabelWord.set(" ".join("_" * len(word)))

            hintText = Message(window, text="IMPORTANT: Hint Only shows first letter, on first try.", width=900,
                               fg="RED")
            hintText.grid(row=5, column=0, columnspan=8, sticky=N + S + W + E)

        # compare keyboard character to actual word
        def guess(ch):
            global numberOfGuess
            if numberOfGuess < 11:
                guessText = list(dashedWord)
                guessedChar = list(LabelWord.get())

                if guessText.count(ch) > 0:
                    for i in range(len(guessText)):
                        # compare each character
                        if guessText[i] == ch:
                            guessedChar[i] = ch
                            LabelWord.set("".join(guessedChar))

                        # compare word
                        if LabelWord.get() == dashedWord:
                            LabelWord.set(" ".join(word))
                            EnterTxt = Message(window, font="Consolas 14 bold",
                                               text="CONGRATULATION! YOU'VE WON. TO CONTINUE THE GAME, PRESS 'ENTER'",
                                               width=530, fg="RED", bg="WHITE")
                            EnterTxt.grid(row=5, column=0, columnspan=8, )
                            hintText.config(fg="White")
                            missedTextList.clear()

                # increment count & append Character that doesn't match
                else:
                    numberOfGuess += 1
                    imageLabel.config(image=photos[numberOfGuess])
                    missedTextList.append(ch)

                    if numberOfGuess == 11:
                        LabelWord.set(" ".join(word))
                        EnterTxt = Message(window, font="Consolas 16 bold",
                                           text="TO CONTINUE THE GAME, PRESS 'ENTER'",
                                           width=900, fg="RED", bg="WHITE")
                        EnterTxt.grid(row=5, column=0, columnspan=8, )
                        hintText.config(fg="White")
                        messagebox.showwarning("Hangman", "You're out of try's. Game Over")
                        missedTextList.clear()

                missedTxt = Text(window, font="Consolas 16 bold", width=1, height=1, fg="RED", )
                missedTxt.grid(row=1, column=0, columnspan=4, sticky=N + S + W + E)
                missedTxt.config(state="normal")
                missedTxt.insert(INSERT, "Missed letters: ")
                for i in missedTextList:
                    missedTxt.insert(INSERT, i + " ")
                missedTxt.config(state="disabled")

        # hint function
        def hint():
            if numberOfGuess < 5:
                LabelWord.set(" ".join(word[0] + "_" * (len(word) - 1)))
            else:
                messagebox.showwarning("Hangman", "Sorry you can only use hint once  on first try :)")

        # place hangman PNG
        imageLabel = Label(window)
        imageLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
        imageLabel.config(image=photos[4])

        # place hangman word
        LabelWord = StringVar()
        label = Label(window, textvariable=LabelWord, font="Consolas 24 bold")
        label.grid(row=0, column=3, columnspan=6, padx=10, pady=40)

        # place hangman keyboard
        n = 0
        for ch in ascii_uppercase:
            keyboardKey = Button(window, text=ch,
                                 command=lambda ch=ch: guess(ch),
                                 font="Helvetica 18", width=6, height=2)
            keyboardKey.grid(row=2 + n // 9, column=n % 9)
            n += 1

        # place new game button
        newGButton = Button(window, text="New\nGame", font="Helvetica 10 bold",
                            command=newGame, width=5)
        newGButton.grid(row=4, column=8, sticky="NSWE")

        # place hint button
        hintBtn = Button(window, text="HINT", font="Helvetica 15 bold",
                         command=hint, width=5)
        hintBtn.grid(row=0, column=8, sticky="NSWE", rowspan=2)

        newGame()
        window.mainloop()


Hangman()
