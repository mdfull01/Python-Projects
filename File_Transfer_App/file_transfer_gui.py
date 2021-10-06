#
#   Python:     3.9.7    
#
#   Author:     Matt Fuller


from tkinter import *
import tkinter as tk

# importing other modules so we have access to them
import file_transfer_main
import file_transfer_func


def load_gui(self):

    # creating labels and using grid() to locate/paint them on the window
    self.lbl_sdir = tk.Label(self.master,text='Source Folder')
    self.lbl_sdir.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_ddir = tk.Label(self.master,text='Destination Folder')
    self.lbl_ddir.grid(row=3,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    

    # creating text boxes to display selected directories and using grid() to locate/paint them on the window
    # depending on the business application the ability to edit sdir and ddir entry fields may not be apporiate
    self.txt_sdir = tk.Entry(self.master,text='',width=75)
    self.txt_sdir.grid(row=1,column=0,rowspan=1,columnspan=8,padx=(30,0),pady=(0,0),sticky=N+E+W)
    self.txt_ddir = tk.Entry(self.master,text='',width=75)
    self.txt_ddir.grid(row=4,column=0,rowspan=1,columnspan=8,padx=(30,0),pady=(0,0),sticky=N+E+W)


    # creating buttons and using grid() to locate/paint them on the window
    self.btn_sdir = tk.Button(self.master,width=12,height=1,text='Browse',command=lambda: file_transfer_func.browse_source(self))
    self.btn_sdir.grid(row=2,column=0,padx=(30,0),pady=(10,10),sticky=W)
    self.btn_ddir = tk.Button(self.master,width=12,height=1,text='Browse',command=lambda: file_transfer_func.browse_destination(self))
    self.btn_ddir.grid(row=5,column=0,padx=(30,0),pady=(10,10),sticky=W)
    self.btn_ftrans = tk.Button(self.master,width=16,height=2,text='Transfer New Files',command=lambda: file_transfer_func.file_transfer(self))
    self.btn_ftrans.grid(row=8,column=2,padx=(0,0),pady=(45,10),sticky=W)
    








if __name__ == '__main__':
    pass
   
