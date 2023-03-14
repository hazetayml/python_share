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
dirName = "unsorted_photos"
sortedDirName = "sorted"

dirs = os.listdir(sortedDirName)

#Loop through each subfolder in sorted folder
for subfolder in dirs:
   print(subfolder)
   
   #check if is a directory, only copy files in directory
   if os.path.isdir(sortedDirName+"/"+subfolder):
      folderName = sortedDirName+"/"+subfolder
      filesInDir = os.listdir(folderName)
      print(folderName)
      
      # loop through each file in subfolder yyyy_mm
      for file in filesInDir:
         fileName = sortedDirName+"/"+subfolder+"/"+file
         newFileName = dirName +"/"+file
         shutil.move(fileName, newFileName)
         print("Moved: "+fileName)       
      os.rmdir(sortedDirName+"/"+subfolder)
      
      
 