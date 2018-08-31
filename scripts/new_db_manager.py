import mysql.connector
import difflib

class DBManager:
	def __init__(self):
		self.db = mysql.connector.connect(user='lus', password='lus',
                              host='127.0.0.1',
                              database='moviedb',
                              charset='utf8',
                              use_unicode=True)
		self.cursor = self.db.cursor()



	def get_movie(self, movie):
		listT = []
		### I append in the first position the research, from the second the results
		listT.append(movie)
		movieQ = ("SELECT title FROM movie WHERE title LIKE %s")
		self.cursor.execute(movieQ, ("%" + movie + "%",))
		if self.cursor is None:
			return None
		for t in self.cursor:
			listT.append(t[0])
		#print(listT)
		return listT

	def check_list(self, listC):
		match = []
		for i, el in enumerate(listC):
			if i >= 1:
				match.append(el)
			#print(str(i) + ". " + str(el))
		res = difflib.get_close_matches(listC[0], match)
		#print(res)
		if len(res) > 0:
			return str(res[0])
		else:
			return None

	def get_actors(self, movie):
		actors = []
		movie_l = self.get_movie(movie)
		best_res = str(self.check_list(movie_l))
		query = ("SELECT actors FROM movie WHERE title = %s ")
		self.cursor.execute(query, (best_res, ))
		#print ("Best_res: " + best_res)
		if best_res is None:
			return None;
		actors.append(best_res)
		for t in self.cursor:
			actors.append(t[0])
		#print(actors)
		return actors

	def get_director(self, movie):
		director = []
		movie_l = self.get_movie(movie)
		best_res = str(self.check_list(movie_l))
		query = ("SELECT director FROM movie WHERE title = %s ")
		self.cursor.execute(query, (best_res, ))
		#print ("Best_res: " + best_res)
		if best_res is None:
			return None;
		director.append(best_res)
		for t in self.cursor:
			director.append(t[0])
		#print(director)
		return director

	def get_budget(self, movie):
		budget = []
		movie_l = self.get_movie(movie)
		best_res = str(self.check_list(movie_l))
		query = ("SELECT budget FROM movie WHERE title = %s")
		self.cursor.execute(query, (best_res,))
		if best_res is None:
			return None;
		budget.append(best_res)
		for t in self.cursor:
			budget.append(t[0])
		return budget

	def get_year(self, movie):
		year = []
		movie_l = self.get_movie(movie)
		best_res = str(self.check_list(movie_l))
		query = ("SELECT year FROM movie WHERE title = %s")
		self.cursor.execute(query, (best_res,))
		if best_res is None:
			return None;
		year.append(best_res)
		for t in self.cursor:
			year.append(t[0])
		return year

	def get_country(self, movie):
		country = []
		movie_l = self.get_movie(movie)
		best_res = str(self.check_list(movie_l))
		query = ("SELECT country FROM movie WHERE title = %s")
		self.cursor.execute(query, (best_res,))
		if best_res is None:
			return None;
		country.append(best_res)
		for t in self.cursor:
			country.append(t[0].encode("utf8"))
		return country

	def get_gross(self, movie):
		gross = []
		movie_l = self.get_movie(movie)
		best_res = str(self.check_list(movie_l))
		query = ("SELECT gross FROM movie WHERE title = %s")
		self.cursor.execute(query, (best_res,))
		if best_res is None:
			return None;
		gross.append(best_res)
		for t in self.cursor:
			gross.append(t[0])
		return gross

	def get_score(self, movie):
		score = []
		movie_l = self.get_movie(movie)
		best_res = str(self.check_list(movie_l))
		query = ("SELECT imdb_score FROM movie WHERE title = %s")
		self.cursor.execute(query, (best_res,))
		if best_res is None:
			return None;
		score.append(best_res)
		for t in self.cursor:
			score.append(t[0])
		return score

	def get_likes(self, movie):
		likes = []
		movie_l = self.get_movie(movie)
		best_res = str(self.check_list(movie_l))
		query = ("SELECT movie_facebook_likes FROM movie WHERE title = %s")
		self.cursor.execute(query, (best_res,))
		if best_res is None:
			return None;
		likes.append(best_res)
		for t in self.cursor:
			likes.append(t[0])
		return likes

	def get_genres(self, movie):
		genre = []
		movie_l = self.get_movie(movie)
		best_res = str(self.check_list(movie_l))
		query = ("SELECT genres FROM movie WHERE title = %s")
		self.cursor.execute(query, (best_res,))
		if best_res is None:
			return None;
			genre.append(best_res)
		for t in self.cursor:
			genre.append(t[0])
		return genre

	def get_keywords(self, movie):
		keywords = []
		movie_l = self.get_movie(movie)
		best_res = str(self.check_list(movie_l))
		query = ("SELECT plot_keywords FROM movie WHERE title = %s")
		self.cursor.execute(query, (best_res,))
		if best_res is None:
			return None;
		keywords.append(best_res)
		for t in self.cursor:
			keywords.append(t[0])
		return keywords

	def get_link(self, movie):
		link = []
		movie_l = self.get_movie(movie)
		best_res = str(self.check_list(movie_l))
		query = ("SELECT movie_imdb_link FROM movie WHERE title = %s")
		self.cursor.execute(query, (best_res,))
		if best_res is None:
			return None;
		link.append(best_res)
		for t in self.cursor:
			link.append(t[0])
		return link

	def get_language(self, movie):
		lang = []
		movie_l = self.get_movie(movie)
		best_res = str(self.check_list(movie_l))
		query = ("SELECT language FROM movie WHERE title = %s")
		self.cursor.execute(query, (best_res,))
		if best_res is None:
			return None;
		lang.append(best_res)
		for t in self.cursor:
			lang.append(t[0])
		return lang

	def get_duration(self, movie):
		duration = []
		movie_l = self.get_movie(movie)
		best_res = str(self.check_list(movie_l))
		query = ("SELECT duration FROM movie WHERE title = %s")
		self.cursor.execute(query, (best_res,))
		if best_res is None:
			return None;
		duration.append(best_res)
		for t in self.cursor:
			duration.append(t[0])
		return duration








	