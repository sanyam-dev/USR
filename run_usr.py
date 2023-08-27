from usr import USR

input_dir = "./test"	#change to data storage location
output_dir = "./results_test"	#change to result storage location

usr = USR()
usr.set_root_folder_path(input_dir)
usr.set_res_folder_path(output_dir)
usr.run()