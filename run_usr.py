from usr import USR

input_dir = "./data"	#change to data storage location
output_dir = "./results"	#change to result storage location

usr = USR()
usr.set_root_folder_path(input_dir)
usr.set_res_folder_path(output_dir)
usr.run()