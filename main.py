print("Hello Stranger..Welcome to Arcade Abs"
      "\n")

print("What is your name?")
name = input()
print("\n"
      "Well,hello there " + name + "!"
      "\n")
print("What is your age if you don't mind me asking?")
age = input()
print("\n"
      "How often do you exercise?"
      "\n")
print("a:Once a week"
      "\n"
      "b:Three times a week"
      "\n"
      "c:Daily"
      "\n")

answer = input()
if answer == "a" or answer == "A":
  print("Why is that? Whats holding you back from exercising?")
if answer == "b" or answer == "B":
  print("Way to go!Good start!"
        "\n")
if answer == "c" or answer == "C":
  print("That is awesome!"
        "\n")

print("What type of training do you do?"
      "\n")
print("a:Strength"
      "\n"
      "b:Cardio"
      "\n"
      "c:Flexibility"
      "\n")

answer = input()
if answer == "a" or answer == "A":
  print("Go big or Go home huh?!Thats great!"
        "\n")
if answer == "b" or answer == "B":
  print(
      "Getting ready for the marathon i see!Those legs were made for running!"
      "\n")
if answer == "c" or answer == "C":
  print("I see you are a flexibility type!Dont forget to stretch!"
        "\n")
print("What are your goals for the future?"
        "\n")
answer = input()
print("Thats what i wanna hear!Lets make this happen shall we?.."
      "\n")
import tkinter as tk
from tkinter import messagebox

def sign_up():
    messagebox.showinfo("Arcade Abs", "UpsideDown this way!")
root = tk.Tk()
root.title("Sign Up Application")
sign_up_button = tk.Button(root, text="Sign Up", command=sign_up)
sign_up_button.pack(pady=20)
root.mainloop()

