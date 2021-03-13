from tkinter import *

class Application(Frame):

    def  __init__(self,master):
        super(Application,self).__init__()
        self.task=""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.user_input = Entry(self, bg = "#5BC8AC", 
        bd = 29, insertwidth = 4, width = 24,
        font = ("Verdana", 20, "bold"), textvariable = self.UserIn, justify = RIGHT)
        self.user_input.grid(columnspan = 4)

        self.user_input.insert(0,"0")

        self.button1 = Button(self, bg = "#95dbc6", bd= 12,
        text = "7", padx = 33, pady = 25,
        font= ("Helvetica", 20, "bold"), command = lambda: self.buttonClick(7)
        self.button1.grid(row = 2, column = 0 , sticky = W)