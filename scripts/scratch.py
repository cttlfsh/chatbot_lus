import mysql.connector

from new_db_manager import DBManager

# def get_movie():


# def check_list(listC):
# 	for i, el in enumerate(listC):
# 		print(str(i) + ". " + el)
# 	title = raw_input("Which one do you mean? (Select the number) ")
# 	return title

def get_director(movie, cursor):
	listT = []
	movieQ = ("SELECT title FROM movie WHERE title LIKE %s")
	cursor.execute(movieQ, ("%" + movie + "%",))
	for t in cursor:
		listT.append(t[0])
		#print(type(t))
	# if len(listT) > 1:
	# 	ind = check_list(listT)
	# else:
	# 	ind = 0
	return listT

	# query = ("SELECT director FROM movie WHERE title LIKE %s")
	# cursor.execute(query, ("%" + listT[int(ind)] + "%",))
	# for t in cursor:
	# 	director.append(t[0].decode("utf-8"))
	# return director[0]


cnx = mysql.connector.connect(user='lus', password='lus',
                              host='127.0.0.1',
                              database='moviedb')
director = []
cursor = cnx.cursor()

inpt = raw_input("Ask me something: ")
director = get_director(inpt, cursor)
print (director)

cursor.close()
cnx.close()




# db = DBManager()

# inpt = raw_input("Ask me something: ")
# dirw = db.get_director(inpt)
# print(dirw)
