import random
import os
import pygame
import time
from tkinter import *
os.chdir(os.path.dirname(__file__))
words = None
with open("words.txt") as f:
        words = f.readlines()
random.shuffle(words)
hangman_stages = [
    # مرحله 0
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    # مرحله 1
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    # مرحله 2
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    # مرحله 3
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    # مرحله 4
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    # مرحله 5
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    # مرحله 6
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]
chance = 0
win_times = 0
lose_times = 0
the_word = "".join(list(random.choice(words)[:-1]))
the_player_word = list("_" * len(the_word))
def check():
    global chance
    global the_word
    global the_player_word
    global win_times
    global lose_times
    if len(guess.get()) == 1:
        if guess.get() in the_word:
            for i in range(len(the_word)):
                if the_word[i] == guess.get():
                    the_player_word[i] = guess.get()
            pygame.mixer.init()
            pygame.mixer.music.load("sounds/correct.mp3")
            pygame.mixer.music.play()
            the_win_word.configure(text=" ".join(the_player_word))
            the_win_word.configure(font=("Arial",20))
        else:
            chance += 1
            pygame.mixer.init()
            pygame.mixer.music.load("sounds/false.mp3")
            pygame.mixer.music.play()
            man.configure(text=hangman_stages[chance])
            man.configure(font=("Arial",20))
            if chance == 6:
                the_win_word.configure(text=the_word)
                the_win_word.configure(font=("Arial",20))
                the_win_word.configure(width=25,anchor="center")
                man.configure(text=hangman_stages[6])
                man.configure(font=("Arial",20))
                lose_times += 1
                loses.configure(text=f"loses: {lose_times}")
                win.update_idletasks()
                pygame.mixer.init()
                pygame.mixer.music.load("sounds/gameover.mp3")
                pygame.mixer.music.play()
                time.sleep(5)
                the_word = "".join(list(random.choice(words)[:-1]))
                the_player_word = list("_" * len(the_word))
                the_win_word.configure(text=the_player_word)
                the_win_word.configure(font=("Arial",20))
                chance = 0
                man.configure(text=hangman_stages[chance])
                man.configure(font=("Arial",20))
    elif len(guess.get()) > 1:
        if guess.get() == the_word:
            the_win_word.configure(text=the_word)
            the_win_word.configure(font=("Arial",20))
            win_times += 1
            wins.configure(text=f"wins: {win_times}")
            win.update_idletasks()
            pygame.mixer.init()
            pygame.mixer.music.load("sounds/victory.mp3")
            pygame.mixer.music.play()
            time.sleep(6)
            the_word = "".join(list(random.choice(words)[:-1]))
            the_player_word = list("_" * len(the_word))
            the_win_word.configure(text=the_player_word)
            the_win_word.configure(font=("Arial",20))
            chance = 0
            man.configure(text=hangman_stages[chance])
            man.configure(font=("Arial",20))
        else:
            chance += 1
            pygame.mixer.init()
            pygame.mixer.music.load("sounds/false.mp3")
            pygame.mixer.music.play()
            man.configure(text=hangman_stages[chance])
            man.configure(font=("Arial",20))
            if chance == 6:
                man.configure(text=hangman_stages[6])
                man.configure(font=("Arial",20))
                the_win_word.configure(text=the_word)
                the_win_word.configure(font=("Arial",20))
                the_win_word.configure(width=25,anchor="center")
                lose_times += 1
                loses.configure(text=f"loses: {lose_times}")
                win.update_idletasks()
                pygame.mixer.init()
                pygame.mixer.music.load("sounds/gameover.mp3")
                pygame.mixer.music.play()
                time.sleep(5)
                the_word = "".join(list(random.choice(words)[:-1]))
                the_player_word = list("_" * len(the_word))
                the_win_word.configure(text=the_player_word)
                the_win_word.configure(font=("Arial",20))
                chance = 0
                man.configure(text=hangman_stages[chance])
                man.configure(font=("Arial",20))
    guess.delete(0,END)
win = Tk()
win.minsize(350,470)
win.maxsize(350,470)
win.title("hang-man")
man = Label(text=hangman_stages[chance])
man.configure(font=("Arial",20))
man.pack()
the_win_word = Label(text=" ".join(the_player_word))
the_win_word.configure(font=("Arial",20))
the_win_word.pack(padx=0,pady=20)
guess= Entry(win)
guess.pack(ipadx=8,ipady=4)
btn = Button(text="Enter",command=check,padx=23,pady=4)
btn.pack()
win.bind("<Return>",lambda e:btn.invoke())
wins = Label(text=f"wins: {win_times}")
wins.configure(font=("Arial",12))
wins.place(x=38,y=375)
loses = Label(text=f"loses: {lose_times}")
loses.configure(font=("Arial",12))
loses.place(x=261,y=373)
#------------------------------------------------finish-----------------------------------------------------
win.mainloop()


            


 
