# Program to replace problemset.html and stylebutwhite.css files with the files in this directory

import os
from shutil import copyfile

# https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory

for directory in os.listdir("../problemsets/amc8"):
	if(directory[-4:] == "html"):
		continue
	print(directory)
	print("../problemsets/amc8/" + directory + "/stylebutwhite.css")
	copyfile("stylebutwhite.css", "../problemsets/amc8/" + directory + "/stylebutwhite.css")

for directory in os.listdir("../problemsets/amc10"):
	if(directory[-4:] == "html"):
		continue
	print(directory)
	print("../problemsets/amc10/" + directory + "/A/stylebutwhite.css")
	copyfile("stylebutwhite.css", "../problemsets/amc10/" + directory + "/A/stylebutwhite.css")
	print("../problemsets/amc10/" + directory + "/B/stylebutwhite.css")
	copyfile("stylebutwhite.css", "../problemsets/amc10/" + directory + "/B/stylebutwhite.css")

for directory in os.listdir("../problemsets/amc12"):
	if(directory[-4:] == "html"):
		continue
	print(directory)
	print("../problemsets/amc12/" + directory + "/A/stylebutwhite.css")
	copyfile("stylebutwhite.css", "../problemsets/amc12/" + directory + "/A/stylebutwhite.css")
	print("../problemsets/amc12/" + directory + "/B/stylebutwhite.css")
	copyfile("stylebutwhite.css", "../problemsets/amc12/" + directory + "/B/stylebutwhite.css")

for directory in os.listdir("../problemsets/aime"):
	if(directory[-4:] == "html"):
		continue
	print(directory)
	print("../problemsets/aime/" + directory + "/I/stylebutwhite.css")
	copyfile("stylebutwhite.css", "../problemsets/aime/" + directory + "/I/stylebutwhite.css")
	print("../problemsets/aime/" + directory + "/II/stylebutwhite.css")
	copyfile("stylebutwhite.css", "../problemsets/aime/" + directory + "/II/stylebutwhite.css")

copyfile("stylebutwhite.css", "../scraper/stylebutwhite.css")
