from usr import USR
import sys

n = len(sys.argv)

input_dir = str(sys.argv[1])
output_dir = str(sys.argv[2])

if input_dir == "":
	input_dir = "./test"	#change to data storage location
if output_dir == "":
	output_dir = "./results_test"	#change to result storage location

usr = USR()
usr.set_root_folder_path(input_dir)
usr.set_res_folder_path(output_dir)
usr.run()
