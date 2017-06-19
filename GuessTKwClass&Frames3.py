from tkinter import *
root = Tk()
import random

class GuessTheNumber():
    def __init__(self,master):
        self.topFrame = Frame(root)
        self.topFrame.pack(side=TOP)
        self.midFrame = Frame(root)
        self.midFrame.pack()
        self.bottomFrame = Frame(root)
        self.bottomFrame.pack(side=BOTTOM)

        self.FirstScreen(master)

    def Destroy(self,destroy_w):
        print('destroying')
        if destroy_w==destroy_a:
            try:
                self.L1.destroy()
                self.name.destroy()
                self.B1.destroy()
                self.B2.destroy()
                self.guess.destroy()

        elif destroy_w=='GuessTxtDestroy':
            try:
                self.L4.destroy()

        elif destroy_w=='destroyAll':
            self.Destroy()
            self.GuessTxtDestroy()
            try:
                self.L2.destroy()
                self.L3.destroy()

            except AttributeError:
                pass


# First screen
    def FirstScreen(self,name):
        self.Destroy('destroyAll')

        self.L1 = Label(self.topFrame, text='Hello. What is your name?')
        self.name = Entry(self.midFrame)
        self.B1 = Button(self.bottomFrame, text='Send')
        self.L1.pack()
        self.name.pack()
        self.B1.pack()
        self.name.bind('<Return>', self.Well)
        self.B1.bind('<Button-1>', self.Well)

#2nd screen
    def Well(self,think):
        self.YourName = self.name.get()
        self.Destroy()

        self.L2 = Label(self.topFrame, text='Well, ' + self.YourName + ', I am thinking of a number between 1 and 20')
        self.L2.pack()
        self.L3 = Label(self.topFrame, text='Take a guess:')
        self.L3.pack()
        self.secretNumber = random.randint(1, 20)
        self.NoGuessTaken = 0
        self.TakeaGuess(root)

#After u take a guess
    def YourGuess(self,uguess):
        if self.NoGuessTaken < 6:
            print('The secret number is:'+str(self.secretNumber)) #Debugging

            self.guessInput = int(self.guess.get())
            self.NoGuessTaken = self.NoGuessTaken + 1

            if self.guessInput < self.secretNumber:
                self.GuessTxtDestroy()
                self.L4=Label(root,text='Your guess is too low')
                self.L4.pack()
                self.TakeaGuess(root)  # Going back to take another guess
            elif self.guessInput > self.secretNumber:
                self.GuessTxtDestroy()
                self.L4=Label(root,text='Your guess is too high')
                self.L4.pack()
                self.TakeaGuess(root)  # Going back to take another guess
            else:
                self.GuessOrNo()

        else:
            self.GuessOrNo()


#Take a guess
    def TakeaGuess(self,aguess):
        self.Destroy()
        self.guess = Entry(self.midFrame)
        self.guess.pack()
        self.B1=Button(self.bottomFrame,text='Send')
        self.B1.pack(side=RIGHT)
        self.B2=Button(self.bottomFrame, text='Back')
        self.B2.pack(side=LEFT)
        self.B1.bind('<Button-1>',self.YourGuess)
        self.guess.bind('<Return>',self.YourGuess)
        self.B2.bind('<Button-1>',self.FirstScreen)

    def GuessOrNo(self):
        self.DestroyAll()
        if self.guessInput == self.secretNumber:
            self.L1=Label(self.topFrame, text='Good job,' +self.YourName+'! You guessed my number in '
                          +str(self.NoGuessTaken)+' guesses.')
        else:
            self.L1=Label(self.topFrame,text='Nope. The number I was thinking of was '+ str(self.secretNumber))

        self.B1 = Button(self.bottomFrame, text='Try again')
        self.B1.bind('<Button-1>', self.FirstScreen)
        self.B1.pack()
        self.L1.pack()


a=GuessTheNumber(root)
root.mainloop()
