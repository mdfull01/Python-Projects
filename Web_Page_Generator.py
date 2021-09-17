#
#   Python:     3.9.7    
#
#   Author:     Matt Fuller
#
#   Purpose:    Create an app that generates a simple webpage
#               which displays user input as body text

from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser

#==========frame_class===================================
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300)    #(Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        center_window(self,500,300)
        self.master.title('Web Page Generator')
        self.master.configure(bg='#F0F0F0')
        # loud gui widgets
        load_gui(self)


#=============gui=========================================
def load_gui(self):

    # creating labels and using grid() to locate/paint them on the window
    self.lbl_body = tk.Label(self.master,text='Enter text below to generate body content for your new webpage!')
    self.lbl_body.grid(row=0,column=1,columnspan=4,padx=(70,0),pady=(10,0),sticky=N+W)

    # creating text input field, scroll bar, and using grid() to locate/paint them on the window
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.txt_body = tk.Text(self.master,height=12,width=50,yscrollcommand=self.scrollbar1.set)
    self.scrollbar1.config(command=self.txt_body.yview)
    self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.txt_body.grid(row=1,column=2,padx=(50,0),pady=(0,0),sticky=N+E+S+W)

    # creating a generate button and using grid() to locate/paint it on the window
    self.btn_generate = tk.Button(self.master,width=24,height=2,text='Generate Web Page!',command=lambda: writeContent(self))
    self.btn_generate.grid(row=8,column=2,padx=(150,0),pady=(20,20),sticky=W)


#==========functions======================================

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get the user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def writeContent(self):
    # f will create or open (if exists) file in write mode
    f = open('webpage_generator.html', 'w')
    # ui variable stores the text that was entered into text box txt_body and strips leading/trailing spaces
    ui = self.txt_body.get('1.0',END).strip()
    # c variable stores string of html code for webpage_generator.html file where the body content is
    # the ui variable (text box contents)
    c = '''<html>
    <body>
    <h1>
    {}
    </h1>
    </body>
    </html>'''.format(ui)
    # if statement verifies there is content in the text box
    if len(ui) > 0:
        # writing the code from c into file
        f.write(c)
        # close the file
        f.close()
        openContent()
    else: 
        messagebox.showinfo('No content detected! \nPlease enter content into the text box and try again.')



def openContent():
    f = 'webpage_generator.html'
    # opens f file name in new tab 
    webbrowser.open(f, new = 2, autoraise=True)



if __name__ == '__main__':
    root = tk.Tk()  # to create a window from tkinter
    App = ParentWindow(root)    # passes the window to our class
    root.mainloop() # keeps the window open until it is closed or loop is canceled
    
   
