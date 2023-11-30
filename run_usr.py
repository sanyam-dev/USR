from usr import USR
import sys

n = len(sys.argv)

input_dir = str(sys.argv[1])
output_dir = str(sys.argv[2])
input_mode = int(sys.argv[3])

if input_dir == "":
	input_dir = "./test"	#change to data storage location
if output_dir == "":
	output_dir = "./results_test"	#change to result storage location

usr = USR()
usr.set_root_folder_path(input_dir)
usr.set_res_folder_path(output_dir)
usr.set_input_mode(input_mode)	# set input mode == 0 for single root folder
																# in case root folder contains sub folders, use input mode 1
usr.run()
