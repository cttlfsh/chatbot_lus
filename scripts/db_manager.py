from sqlalchemy import and_
from difflib import get_close_matches

import sqlsoup



class DBManager:
	def __init__(self, uri):
		self.db = sqlsoup.SQLSoup(uri)
		self.movie = self.db.movie
		### self.movies = self.db.movies
		

	### Using **kwargs means passing lists
	def filter(self, **kwargs):
		found = False
		result = and_()
		for key in kwargs:
			val = kwargs[key]

			### dont know what to put inside ilike
			if key == "title":
				result = and_(result, self.movie.title.ilike("%" + val + "%"))
				if not found:
					found = True
			elif key =="actor":
				result = and_(result, self.movie.actor.ilike("%" + val + "%"))
				if not found:
					found = True
			elif key =="director":
				result = and_(result, self.movie.director.ilike("%" + val + "%"))
				if not found:
					found = True
			elif key =="genre":
				result = and_(result, self.movie.genre.ilike("%" + val + "%"))
				if not found:
					found = True
			elif (key =="country"):
				result = and_(result, self.movie.country.ilike("%" + val + "%"))
				if not found:
					found = True
			elif (key =="yar"):
				result = and_(result, self.movie.year.ilike("%" + val + "%"))
				if not found:
					found = True
			elif (key =="language" ):
				result = and_(result, self.movie.language.ilike("%" + val + "%"))
				if not found:
					found = True
			elif key =="runtime":
				result = and_(result, self.movie.duration.ilike("%" + val + "%"))
				if not found:
					found = True
			elif key =="color":
				result = and_(result, self.movie.color.ilike("%" + val + "%"))
				if not found:
					found = True
			elif key == "budget":
				result = and_(result, self.movie.budget.ilike("%" + val + "%"))
				if not found:
					found = True
			elif key =="score":
				result = and_(result, self.movie.imdb_score.ilike("%" + val + "%"))
				if not found:
					found = True
			elif key =="likes":
				result = and_(result, self.movie.imdb_score.ilike("%" + val + "%"))
				if not found:
					found = True
		if found:
			return result
		return None


	def get_movie(self, **kwargs):
		query = self.filter(**kwargs)
		if (query is not None):
			return self.movie.filter(select).all()
		else:
			return None

	### Since get_movie() returns a list, I need to check the 
	### closest result of all, which will theoretically be the right
	### one
	def best_match(self, result, title):
		matches_list = {}
		### filling the list to be checked
		for r in result:
			matches_list[r.title] = r
		### this checks the closest matches between "title" and all the key
		### of the dictionary
		check = difflib.get_close_matches(title, matches_list.keys())

		### The closest match of all is the one stored in the first
		### position ==> check[0]
		if len(check) > 0:
			return matches_list(check[0])

		return None



	#### NOW I SHOULD PROVIDE ALL NECESSARY IMPLEMENTATIONS
	#### FOR SELECTING THE RIGHT COLUMN IN THE DB

	### 1] Title
	def get_title(self, **kwargs):
		query = self.filter(**kwargs)
		if query is not None:
			result = self.movie.filter(query)
		if result is not None:
			return result.all()
		return None

	### 2] actors
	def get_actors(self, title):
		result = self.get_movie(title=title)
		if result is not None:
			bm = best_match(result, title)
			if bm is not None:
				return bm.actors
			return None

	### 3] director
	def get_director(self, title):
		result = self.get_movie(title=title)
		if result is not None:
			bm = best_match(result, title)
			if bm is not None:
				return bm.director
			return None

	### 4] genre
	def get_genre(self, title):
		result = self.get_movie(title=title)
		if result is not None:
			bm = best_match(result, title)
			if bm is not None:
				return bm.genre
			return None

	### 5] country
	def get_country(self, title):
		result = self.get_movie(title=title)
		if result is not None:
			bm = best_match(result, title)
			if bm is not None:
				return bm.country
			return None

	### 6] year
	def get_year(self, title):
		result = self.get_movie(title=title)
		if result is not None:
			bm = best_match(result, title)
			if bm is not None:
				return bm.year
			return None

	### 7] language
	def get_language(self, title):
		result = self.get_movie(title=title)
		if result is not None:
			bm = best_match(result, title)
			if bm is not None:
				return bm.language
			return None

	### 8] duration
	def get_duration(self, title):
		result = self.get_movie(title=title)
		if result is not None:
			bm = best_match(result, title)
			if bm is not None:
				return bm.duration
			return None

	### 9] color
	def get_color(self, title):
		result = self.get_movie(title=title)
		if result is not None:
			bm = best_match(result, title)
			if bm is not None:
				return bm.color
			return None

	### 10] budget
	def get_budget(self, title):
		result = self.get_movie(title=title)
		if result is not None:
			bm = best_match(result, title)
			if bm is not None:
				return bm.budget
			return None

	### 11] imdb_score
	def get_score(self, title):
		result = self.get_movie(title=title)
		if result is not None:
			bm = best_match(result, title)
			if bm is not None:
				return bm.imdb_score
			return None

	### 11] facebook_likes
	def get_likes(self, title):
		result = self.get_movie(title=title)
		if result is not None:
			bm = best_match(result, title)
			if bm is not None:
				return bm.movie_facebook_likes
			return None

	























