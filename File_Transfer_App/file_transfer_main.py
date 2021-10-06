#
#   Python:     3.9.7    
#
#   Author:     Matt Fuller
#
#   Purpose:    Create application with GUI that allows user to
#               select source and destination folders, preform
#               a file check process that will locate and copy all
#               files from source folder that have been modified in
#               last 24 hours and add them to destination folder.

from tkinter import *
import tkinter as tk

#importing other modules
import file_transfer_gui
import file_transfer_func


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300)    #(Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        file_transfer_func.center_window(self,500,300)
        self.master.title('File Transfer Application')
        self.master.configure(bg='#F0F0F0')
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, 'X' in Windows OS.
        self.master.protocol('WM_DELETE_WINDOW', lambda: file_transfer_func.ask_quit(self))

        # load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        file_transfer_gui.load_gui(self)









if __name__ == '__main__':
    root = tk.Tk()  # to create a window from tkinter
    App = ParentWindow(root)    # passes the window to our class
    root.mainloop() # keeps the window open until it is closed or loop is canceled

   
