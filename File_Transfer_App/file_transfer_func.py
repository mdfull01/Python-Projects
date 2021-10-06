#
#   Python:     3.9.7    
#
#   Author:     Matt Fuller

import os
from os import path
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import shutil
from datetime import datetime, timedelta

# importing other modules so we have access to them
import file_transfer_main
import file_transfer_gui


def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get the user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel('Exit program', 'Okay to exit application?'):
        # This closes app
        self.master.destroy()
        os._exit(0)

# use filedialog to pop up a window and allow user to select source directory
def browse_source(self):
    # create variable sdir to save path for selected source directory
    sdir = tk.filedialog.askdirectory()
    # display selected source directory file path in dir entry window
    self.txt_sdir.delete(0,END)
    self.txt_sdir.insert(0,sdir)
    print(sdir)

# use filedialog to pop up a window and allow user to select destination directory
def browse_destination(self):
    # create variable ddir to save path for selected destination directory
    ddir = tk.filedialog.askdirectory()
    # display selected destination directory file path in dir entry window
    self.txt_ddir.delete(0,END)
    self.txt_ddir.insert(0,ddir)
    print(ddir)


def file_transfer(self):
    # get source and destination directory file paths
    sdir = self.txt_sdir.get()
    ddir = self.txt_ddir.get()
    # get file names from source directory
    files = os.listdir(sdir)
    # set new_time to 24 hours before current time
    new_time = datetime.now() - timedelta(hours=24)
    # create a list that will hold file paths of copied files
    c_files = []
    
    # check to see that user has selected both directories and that they are different file paths
    if (len(sdir) >0) and (len(ddir) >0) and (sdir != ddir):
        print(False)
        # loop through each file in selected source directory
        for i in range(len(files)):
            # create full file path for current file in source directory
            file_path = os.path.join(sdir,files[i])
            # set file_mtime to last modified time of current file to be evaluated
            file_mtime = datetime.fromtimestamp(path.getmtime(file_path))
            # evaluate current file modified time vs current time minus 24 hours
            # if the last modified time is less than 24 hours ago
            if file_mtime > new_time:
                # if the last modified time is less than 24 hours ago, copy
                shutil.copy2(file_path, ddir)
                # add file path to list of copied files
                c_files.append(file_path)
        
    else:
        # error message if source/destination directories are missing or the same directory
        messagebox.showerror('Text','Selected Folder Error''Please ensure that you have selected a source folder,\n'
                             'a destination folder, and that they are not the same folder.')
    # check to see if any files were copied
    if len(c_files) > 0:
        # if files were copied display how many, what directory they were copied to, and their file names
        # in a real application this message would work better as a new text document report of the transfer
        # with the datetime.now info for when it was processed
        messagebox.showinfo('Text','{} files created/modified in the last 24 hours\n'
                            'were found and copied to: {}\n'
                            '{}'.format(len(c_files),ddir,c_files))
        

    else:
        # if no files were copied display message that no files were copied
        messagebox.showinfo('Text','No files created/modified in the last 24 hours\n'
                            'were found or copied.')
        
        
        
if __name__ == '__main__':
    pass
   
