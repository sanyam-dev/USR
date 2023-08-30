import os
from wxconv import WXC

class USR:
		def __init__(self) -> None:
				self.markers = {"Ora", "evaM", "waWA", "agara", "yaxi", "wo", "kyoMki",
					"isIlie","jabaki","yaxyapi","waWApi","yaxyapi","Pira BI",
					"lekina","kiMwu","paraMwu","jaba","waba","yA","aWavA"}
				
				self.discourse_relation = {
						"Ora" : "samuccaya",
						"evaM" : "samuccaya",
						"waWA" : "samuccaya",
						"agara" : "AvaSyakwA-pariNAma",
						"yaxi" : "AvaSyakwA-pariNAma",
						"wo" : "AvaSyakwA-pariNAma",
						"kyoMki" : "kArya-kAraNa",
						"isIlie" : "kArya-kAraNa",
						"jabaki" : "vyABicAra",
						"yaxyapi" : "vyABicAra",
						"waWApi" : "vyABicAra",
						"Pira BI" : "vyABicAra",
						"lekina" : "viroXi",
						"kiMwu" : "viroXi",
						"paraMwu" : "viroXi",
						"jaba" : "samAnakAla",
						"waba": "samAnakAla",
						"yA": "anyawra",
						"aWavA": "anyawra",
				}
				
				self.discourse_pos = {
					"samuccaya" : "1",
					"anyawra": "1",
					"samAnakAla":"0",
					"viroXi": "1",
					"vyaBicAra":"0",
					"kArya-kAraNa": "0",
					"AvaSyakwA-pariNAma": "0"
				}
				
				self.con = WXC(order='utf2wx')
				self.res_folder_path = ""
				self.root_folder_path = ""
		
		
		def set_res_folder_path(self, res_path):
			self.res_folder_path = res_path
			
		def get_res_folder_path(self):
			return self.res_folder_path

		def set_root_folder_path(self, root_path):
			self.root_folder_path = root_path
		
		def get_root_folder_path(self):
			return self.root_folder_path
		
		def create_res_folder(self, path):
			try:
				os.makedirs(path)
			except FileExistsError:
				print("error, folder already exists")
				# filename += str(random.randint(0,100))
				# path = os.path.join(parent_dir, filename)
				# os.makedirs(path)
			return path		
		
		def convert_to_usr(self, file_path):
			with open(file_path, 'r') as file:
					content = file.read()
					return [string.split(",") for string in content.split("\n")]
					# print(content_usr_list)
		
		def save_usr_to_txt(self, prev_usr, prev_filename,  sub_folder_path):
			with open(sub_folder_path + "/" + prev_filename + '.txt', "w") as file:
					for usr_entry in prev_usr:
							for item in usr_entry:
									file.write(item + ",")
							file.write("\n")
					file.close()
			print("data written")
		
		# returns discourse relation for a given string (use curr_usr string)
		def mpd(self,str2):
			words1 = str2.split()
			for word in words1:
				if word in self.markers:
					#print(word)
					return self.discourse_relation[word]
			
			return "-1"

		def get_main_str(self, usr):
			strings_with_main = ""
			i = 1
			for item in usr[5]:
				if item == "0:main":
					strings_with_main += str(i)
				i+=1
			return strings_with_main, i
			
		def process_usr(self,prev_filename, prev_usr, curr_filename, curr_usr):
				str1 = curr_usr[0][0][1:]
				str1 = self.con.convert(str1)
				# print("str: " , self.con.convert(str1))
				discourse_rel = self.mpd(str1)
				if(discourse_rel == "-1"):
					return prev_usr, curr_usr
				y = self.discourse_pos[discourse_rel]
				# y == 0  means discourse relation to be added to prev_usr
				# y == 1  means discourse relation to be added to curr_usr
				if y == 0:
					# find main of curr_usr
					strings_with_main, iii = self.get_main_str(curr_usr)
					usr_id = curr_filename
					fin = usr_id + "." + strings_with_main + ":" + discourse_rel
					position_of_discourse = iii
					prev_usr[6][position_of_discourse] = fin
					# fin = usr_id + "." + strings_with_main
				else:
					strings_with_main, iii = self.get_main_str(prev_usr)
					usr_id = prev_filename
					usr_id = usr_id[:-4]
					fin = usr_id + "." + strings_with_main + ":" + discourse_rel
					position_of_discourse = iii
					curr_usr[6][position_of_discourse] = fin
				
				return prev_usr, curr_usr
		
		def run(self):
			
			self.create_res_folder(self.res_folder_path)
			for folder_name, sub_folder, filenames in os.walk(self.root_folder_path):
				print("foldername ", folder_name)
				print("subfolder", sub_folder)
				print("filename: " , filenames)
				
				if sub_folder.__sizeof__ != 0:
					
					for sub_folder_name in sub_folder:
						sub_folder_path = self.root_folder_path +  "/" + sub_folder_name
						# print(sub_folder_path)
						path = self.res_folder_path + "/" + sub_folder_name 
						self.create_res_folder(path)
						for _, _, filenames in os.walk(sub_folder_path): 
							filenames = sorted(filenames)
							
							prev_usr = []
							curr_usr = []
							prev_filename = "0"
							for filename in filenames:
								file_path	= sub_folder_path + "/" + filename
						
								with open(file_path, "r") as file:
										content = file.read()
										print(filename, ":->", len(content), ":->>", content.find("\n"))
										
										if content.find("\n") != -1:
											curr_usr = self.convert_to_usr(file_path)
											prev_usr, curr_usr = self.process_usr(prev_filename, prev_usr, filename, curr_usr)
											self.save_usr_to_txt(prev_usr, prev_filename, path)
											self.save_usr_to_txt(curr_usr, filename, path)
											prev_filename = filename
											prev_usr = curr_usr
											
											# fn(prev_usr, curr_usr)
											
										# content.find("\n")
										# hindi_str = content.partition("\n")
										# print(hindi_str)
							break
			