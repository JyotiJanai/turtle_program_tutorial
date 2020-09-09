import os
def rename_files():
	# get the file name from a folder
	file_list = os.listdir(r"E:\Udacity_Python_Course\prank")
	print(file_list)
	saved_path = os.getcwd()
	print("Current working directory is",  saved_path)
	os.chdir(r"E:\Udacity_Python_Course\prank")
	#for each file, rename file
	for file_name in file_list:
		print(file_name)
		os.rename(file_name,file_name.translate("0123456789"))
	os.chdir(saved_path)
	
rename_files()
