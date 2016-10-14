import os;
import platform;
import A2

"""
@Author: Siddarth Krishnan
@Date:	 10/14/2016
		 This function takes a filepath that is entered by the user and opens the file to be played
"""
def openFile(musicFilePath):
	if platform.system() == 'Windows':
		os.startfile(musicFilePath)
	else:
	    os.system("open" + " " + musicFilePath)

input1 = input("Enter a path: ")
openFile(input1)
A2.run()

