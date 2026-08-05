from tkinter import Tk, Label, Button
import random
window = Tk()
window.title("Rock Paper Scissors Game")
window.geometry("1000x1000")

# Labels

label1 = Label(window, text ="Instructions:", padx = 5, pady = 5)
label1.grid(row = 0, column = 0)

label2 = Label(window, text = "Choose any one of the options against the robot.", padx = 5, pady = 5)
label2.grid(row = 0, column = 1)

# buttons

btn1 = Button(window,text = "Rock", command = lambda: choose("Rock"), padx = 5, pady = 5 )
btn1.grid(row = 2, column = 0)

btn2 = Button(window,text = "Paper", command =   lambda: choose("Paper"), padx = 5, pady = 5 )
btn2.grid(row = 2, column = 1)

btn3 = Button(window,text = "Scissors", command =  lambda: choose("Scissors"), padx = 5, pady = 5 )
btn3.grid(row = 2, column = 2)

# Final Function

def choose(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    if(choice == computer_choice):
        result = "Draw"

    elif(choice == "Scissors" and computer_choice == "Rock"):
        result = "You Lose"

    elif(choice == "Paper" and computer_choice == "Scissors"):
        result = "You Lose"

    elif(choice == "Rock" and computer_choice == "Paper"):
        result = "You Lose"

    else:
        result = "You Win!"

    label_result.config(text = f"You gave {choice} and the robot gave {computer_choice} so {result}")


label_result = Label(window, text = "result", padx = 5, pady = 5)
label_result.grid(row = 3, column = 0)


window.mainloop()







 