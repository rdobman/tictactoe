from tkinter import *
import tkinter.messagebox

tk = Tk()
f = Frame(tk, bg="orange", width=500, height=500)
f.pack(side=BOTTOM, expand=1)
f2 = Frame(tk, height=100, width=100)
f2.pack(side=LEFT, expand=0)
tk.title("Tic Tac Toe")

bclick = True
winner = False
whoWon = ""
xWins = 0
oWins = 0
ties = 0


def ttt(buttons):
    global bclick

    if buttons["text"] == " " and bclick:
        buttons["text"] = "X"
        end_game()
        bclick = False

    elif buttons["text"] == " " and not bclick:
        buttons["text"] = "O"
        end_game()
        bclick = True


def end_game():
    global whoWon
    global winner
    global xWins
    global oWins
    global ties
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):

            whoWon = "X"
            winner = True
            xWins += 1
            tkinter.messagebox.showinfo("Player X", "Winner is X! X has " + str(xWins) + " win(s)")
            reset()

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O'or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O'or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O'or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O'or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O'or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O'or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):

            whoWon = "O"
            winner = True
            oWins += 1
            tkinter.messagebox.showinfo("Player O", 'Winner is O! O has ' + str(oWins) + " win(s)")
            reset()

    elif (button1['text'] != " " and button2['text'] != " " and button3['text'] != " " and
          button4['text'] != " " and button5['text'] != " " and button6['text'] != " " and
          button7['text'] != " " and button8['text'] != " " and button9['text'] != " "):
        ties += 1
        tkinter.messagebox.showinfo("Tie", "Game ended in a tie. There have been " + str(ties) + " tie(s)")
        reset()


def reset():
    global winner
    button1.config(text=" ")
    button2.config(text=" ")
    button3.config(text=" ")
    button4.config(text=" ")
    button5.config(text=" ")
    button6.config(text=" ")
    button7.config(text=" ")
    button8.config(text=" ")
    button9.config(text=" ")
    winner = False

buttons = StringVar()

b = Button(f2, text="Reset", width=10, command=reset)
b.grid(row=0, column=0)
b.pack()


button1 = Button(f, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button1))
button1.grid(row=1, column=0)

button2 = Button(f, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button2))
button2.grid(row=1, column=1)

button3 = Button(f, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button3))
button3.grid(row=1, column=2)

button4 = Button(f, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button4))
button4.grid(row=2, column=0)

button5 = Button(f, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button5))
button5.grid(row=2, column=1)

button6 = Button(f, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button6))
button6.grid(row=2, column=2)

button7 = Button(f, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button7))
button7.grid(row=3, column=0)

button8 = Button(f, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button8))
button8.grid(row=3, column=1)

button9 = Button(f, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                 command=lambda: ttt(button9))
button9.grid(row=3, column=2)

tk.mainloop()
