from usr import USR
import sys

def main():
		"""
		Main function to run the USR algorithm.

		Usage: python script.py [input_directory] [output_directory] [input_mode]

		Parameters:
		- input_directory (str): Path to the input directory containing data.
		- output_directory (str): Path to the output directory for storing results.
		- input_mode (int): Input mode, 0 for a single root folder, 1 if root folder contains subfolders.

		If command-line arguments are not provided, default values will be used.
		"""
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


if __name__ == "__main__":
    main()