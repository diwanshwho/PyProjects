
import random
from tkinter import *
from tkinter import messagebox


def start():
    def like():
        return messagebox.showinfo('LUDO DICE', 'We Appreciate your LOVE ♥')
        
    def dislike():

        return messagebox.showinfo('LUDO DICE', 'We are improving our Services')

    def result1():

        for item in frame.winfo_children():
            item.destroy()

        numb = random.randint(1,6)
        number = Label(frame, font=("Arial Black", 25), fg='black', text=numb, bg='white')
        number.pack()
        
        if numb == 1:
            photoloc = PhotoImage(file="data\one.png")
        elif numb == 2:
            photoloc = PhotoImage(file="data\two.png")
        elif numb == 3:
            photoloc = PhotoImage(file="data\three.png")
        elif numb == 4:
            photoloc = PhotoImage(file="data\four.png")
        elif numb == 5:
            photoloc = PhotoImage(file="data\five.png")
        elif numb == 6:
            photoloc = PhotoImage(file="data\six.png")

        dieface = Label(frame, image=photoloc)
        dieface.photo = photoloc
        dieface.pack()

        roll_again = Button(frame, anchor='center', text="ROLL AGAIN", font=("Buffalo", 15), fg="black", bg="white",
                            command=result1, borderwidth=0.5, activebackground='#66ffcc', activeforeground='white',
                            relief="flat")
        roll_again.pack(ipadx=10, ipady=10, padx=30, pady=15)

        likedpic = PhotoImage(file="data\liked.png")

        like_button = Button(frame, justify=LEFT, image=likedpic, command=like, borderwidth=0.5,
                             activebackground='#66ffcc', activeforeground='white', relief="flat")
        like_button.photo = likedpic
        like_button.pack(padx=30, pady=15, side=LEFT)

        dislikedpic = PhotoImage(file="data\dislike.png")

        dislike_button = Button(frame, image=dislikedpic, command=dislike, borderwidth=0.5, activebackground='#66ffcc',
                                activeforeground='white', relief="flat")
        dislike_button.photo = dislikedpic
        dislike_button.pack(padx=30, pady=15, side=LEFT)

    root = Tk()
    root.title("LUDO DICE")
    photo = PhotoImage(file="data\source.gif")
    root.iconphoto(False, photo)
    root.configure(bg='white', height=200, width=1000, padx=20, pady=20)
    
    welcome = Label(root,
                  font=("Lean Foreword",35),
                  fg='black',
                  text='Welcome to Ludo Dice',
                  bg='white')
    welcome.pack()
    welcome2 = Label(root,
                  font=("James Fajardo", 10),
                  fg='black',
                  text='by Diwanshu Sharma\n',
                  bg='white')
    welcome2.pack()

    frame = Frame(root, bg="white")
    frame.pack()

    roll = Label(frame,
                   font=("Arial Black",15),
                   fg='black',
                   text='Press Roll ↓',
                   pady=2,
                   padx=5,
                   bg='white')
    roll.pack()

    rolled = Button(frame,
                 anchor='center',
                 text="ROLL",
                 font=("Copperplate Gothic Bold",15),
                 fg="black",
                 command=result1,
                 borderwidth=0.5,
                 activebackground='#66ffcc',
                 activeforeground='white',
                 relief="flat")
    rolled.pack(ipadx=10,ipady=10,padx=30,pady=15)
    
    
    root.mainloop()


start()
