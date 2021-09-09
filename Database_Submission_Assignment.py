#
#   Python:     3.9.7    
#
#   Author:     Matt Fuller
#
#   Purpose:    Create a database, parse a file list
#               add .txt files to db, print db entries

import sqlite3

# create tuple to hold given file name data
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# create files list to store file names containing .txt
files = []

# for loop that searches fileList data for .txt and ads .txt file names to files if they exist
for x in fileList:
    if '.txt' in x:
        files.append(x)

# create variable to hold db connection data
conn = sqlite3.connect('fileList.db')

# connect to fileList.db 
with conn:
    # create cur to hold conn.cursor()
    cur = conn.cursor()
    # use cursor() and execute() to create tbl_file with two columns if it doesnt already exist
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_file(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname STRING \
        )')
    # commit changes
    conn.commit()
    # for loop to use cursor() and execute() to add all values from files into tbl_file
    for x in files:
        cur.execute('INSERT INTO tbl_file(col_fname) VALUES (?)',(x,))
    # commit changes
    conn.commit()
# close connection to fileList.db
conn.close()

# print file names that were added to tbl_file
print(files)







   
