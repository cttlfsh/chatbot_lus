from data_processing import intent_processing
from db_manager import DBManager

moviedb = DBManager("mysql://lus:lus@localhost:3306/moviedb")

# lab_list = []
# entity_list =[]

# with open("../intents_db/NLSPARQL.train.utt.labels.txt", "r") as f:
# 	for line in f:
# 		lab_list.append(line[:-1])

# unique_lab = set(lab_list)
# lab_list = list(unique_lab)
# #print(lab_list)
# lab_list.sort()

# # with open("../files/train_labels.txt", "w") as f:
# # 	for line in lab_list:
# # 		proc_line = intent_processing(line)
# # 		f.write(proc_line + "\n")

# with open("../intents_db/NLSPARQL.train.data", "r") as f:
# 	for line in f.readlines():
# 		if line != "\n":
# 			entity_list.append(line.split("\t")[1][2:-1])

# unique_ent = set(entity_list)
# entity_list = list(unique_ent)
# entity_list.sort()

# with open("../files/entities.txt", "w") as f:
# 	for line in entity_list:
# 		f.write(str(line) + "\n")
