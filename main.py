import sel_code
import os
import sys

sel_code.browser_setup()
sel_code.login()

# TODO Change parameter, depending on the file you are pulling in.
sel_code.category_choice("Productos")

# Open a folder
path = "/home/nick/Downloads"
dirs = os.listdir(path)

# This would print all the files and directories
for file in dirs:
    file_location = (path + "/" + file)
    sel_code.import_files(file_location)

sel_code.browser_close()







