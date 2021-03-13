from tkinter import *

class Application(Frame):

    def  __init__(self,master):
        super(Application,self).__init__()
        self.task=""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()