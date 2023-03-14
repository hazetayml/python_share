'''
Author: Tay Mei Lan (hazetay@gmail.com)
Change: 
- 13 Nov 2020: Creation
- 08 Oct 2022: Added comments 
'''

import os
import shutil
from datetime import datetime

# change the directory name to the name of unsorted folder
dirname = "unsorted_photos"
sortedDirName = "sorted"

# list all the files
listOfFiles = os.listdir(dirname)
for i in listOfFiles:
    filename = dirname+"/"+i
    # get last modified time
    lastModified = os.path.getmtime(filename)

    # format datetime to yyyy_mm to identify folder to move file to
    dt_object = datetime.fromtimestamp(lastModified)
    folderName =dt_object.strftime("%Y_%m")
    
    print(i + "-> "+folderName)
    #create new folder if does not exist
    if (not (os.path.isdir(sortedDirName+"/"+folderName))):
        os.mkdir(sortedDirName+"/"+folderName)
    
    # move file to relevant folder based on year and mth
    newFileName = sortedDirName+"/"+folderName+"/"+i
    shutil.move(filename, newFileName)
    print("Moved: "+i)

        