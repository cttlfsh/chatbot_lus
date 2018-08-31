from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import random

# from policy import RestaurantPolicy, ScriptedPolicy
from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.actions.forms import FormAction
from rasa_core.actions.forms import EntityFormField
from rasa_core.agent import Agent
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.channels.telegram import TelegramInput
from rasa_core.events import SlotSet, AllSlotsReset, Restarted
from rasa_core.interpreter import RasaNLUInterpreter, RegexInterpreter
from rasa_core.policies.memoization import MemoizationPolicy

from new_db_manager import DBManager


slots = ["movie.name", "movie.genre", "movie.location", 
			"movie.year", "movie.language", "actor.name",
			"director.name", "movie.budget", "movie.duration",
			"language", "color", "movie.release_date", "movie.plot_keywords",
			"movie.star_rating", "movie.likes", "movie.gross_revenue"
		]

def error_messages():
	messages = [
				"Error 404: Sarcasm module not found",
				"I'm sorry, but I can't do that",
				"That does not compute",
				"Error: Division by 0",
	]

	return random.choice(messages)

class ActionRestarted(Action):
    def name(self):
        return "action_restarted"
    
    def run(self, dispatcher, tracker, domain):
        return [Restarted()]

class ActionAllSlotReset(Action):
    def name(self):
        return "action_slot_reset"

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


#### CUSTOM CLASSES

# #Deprecated
# class ActionMovie(FormAction):

# 	# @staticmethod
# 	# def required_fields():
# 	# 	return[EntityFormField("movie.name", "movie.name"),
#  #    	EntityFormField("movie.name", "movie.choice")]


# 	def name(self):
# 		return "action_movie"

# 	def run(self, dispatcher, tracker, domain):
# 		movie_list = []
# 		butt_dict_key = {}
# 		buttons = []

# 		movie = tracker.get_slot("movie.name")

# 		if movie is None:
# 			dispatcher.utter_message(error_messages())
# 			dispatcher.utter_template("utter_repeat")
# 		else:
# 			movie_db = DBManager()
# 			movie_list = movie_db.get_movie(movie)
# 			#print(type(movie_list[0]) + " <-- TIPO ELEMENTO")
# 			#print(movie_list)
# 			if movie_list is None:
# 				dispatcher.utter_template("utter_say_noresults")
# 			elif len(movie_list) > 1:
# 				for el in movie_list:
# 					butt_dict_key["title"] = el.decode('utf8')
# 					butt_dict_key["payload"] = el.decode('utf8')
# 					buttons.append(butt_dict_key.copy())
# 				dispatcher.utter_button_message("I found these results, which one do you prefer?\n", buttons)
# 				#choice = movie_db.check_list(movie_list)
# 				return[SlotSet("movie.list", buttons)]
# 			else:
# 				choice = movie_list[0].decode('utf8')
# 				dispatcher.utter_message("I found this result: " + choice + " is it correct?\n")
# 				return[SlotSet("movie.name", choice)]

# 			return[]
# #Deprecated
# class ActionChoice(FormAction):

# 	def name(self):
# 		return "action_choice"

# 	def run(self, dispatcher, tracker, domain):
# 		movie_list = []
# 		butt_dict_key = {}
# 		buttons = []

# 		movie = tracker.get_slot("movie.name")
# 		c = tracker.get_slot("movie.choice")
# 		listM = tracker.get_slot("movie.list")

# 		dispatcher.utter_message("So you mean" + listM[int(movie)][1])
# 		if c is not None:
# 			return[SlotSet("movie.name", listM[int(movie)][1])]

class ActionActors(Action):
	def name(self):
		return "action_actors"

	def run(self, dispatcher, tracker, domain):
		result = []
		actors = []
		butt_dict_key = {}
		buttons = []
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
			dispatcher.utter_template("utter_repeat")
		else:
			movie_db = DBManager()
			result = movie_db.get_actors(movie)
			if actors is None:
				dispatcher.utter_message(error_messages())
			else:
				actors = result[1].split("|")
				for el in actors:
					butt_dict_key["title"] = ""
					butt_dict_key["payload"] = el
					buttons.append(butt_dict_key.copy())
				dispatcher.utter_button_message("Actors for " + result[0] + " are: ", buttons)
				return[SlotSet("actor.name", actors)]


class ActionDirector(Action):
	def name(self):
		return "action_director"

	def run(self, dispatcher, tracker, domain):
		director = []
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
			dispatcher.utter_template("utter_repeat")
		else:
			movie_db = DBManager()
			director = movie_db.get_director(movie)
			if director[1] is None:
				dispatcher.utter_message(error_messages())
			else:
				#dispatcher.utter_message("Movie " + movie_result)
				dispatcher.utter_message("The director of " + director[0] + " is: " + director[1])
				return[SlotSet("director.name", director[1])]

class ActionBudget(Action):
	def name(self):
		return "action_budget"

	def run(self, dispatcher, tracker, domain):
		result = []
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
			dispatcher.utter_template("utter_repeat")
		else:
			movie_db = DBManager()
			result = movie_db.get_budget(movie)
			if result[1] is None:
				dispatcher.utter_message(error_messages())
			else:
				#dispatcher.utter_message("Movie " + movie_result)
				dispatcher.utter_message(result[0] + " had a budget of: " + str(result[1]))
				return[SlotSet("movie.budget", result[1])]

class ActionYear(Action):
	def name(self):
		return "action_year"

	def run(self, dispatcher, tracker, domain):
		result = []
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
			dispatcher.utter_template("utter_repeat")
		else:
			movie_db = DBManager()
			result = movie_db.get_year(movie)
			if result[1] is None:
				dispatcher.utter_message(error_messages())
			else:
				dispatcher.utter_message("Release year for " + result[0] + " is: " + str(result[1]))
				return[SlotSet("movie.release_date", result[1])]

class ActionCountry(Action):
	def name(self):
		return "action_country"

	def run(self, dispatcher, tracker, domain):
		result = []
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
			dispatcher.utter_template("utter_repeat")
		else:
			movie_db = DBManager()
			result = movie_db.get_country(movie)
			if result[1] is None:
				dispatcher.utter_message(error_messages())
			else:
				dispatcher.utter_message("Release region for " + result[0] + " is: " + result[1])
				return[SlotSet("movie.location", result[1])]

class ActionGross(Action):
	def name(self):
		return "action_gross"

	def run(self, dispatcher, tracker, domain):
		result = []
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
			dispatcher.utter_template("utter_repeat")
		else:
			movie_db = DBManager()
			result = movie_db.get_gross(movie)
			if result[1] is None:
				dispatcher.utter_message(error_messages())
			else:
				#dispatcher.utter_message("Movie " + movie_result)
				dispatcher.utter_message("Gross revenue of " + result[0] + " is: " + str(result[1]))
				return[SlotSet("movie.gross_revenue", result[1])]

class ActionScore(Action):
	def name(self):
		return "action_score"

	def run(self, dispatcher, tracker, domain):
		result = []
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
			dispatcher.utter_template("utter_repeat")
		else:
			movie_db = DBManager()
			result = movie_db.get_score(movie)
			if result[1] is None:
				dispatcher.utter_message(error_messages())
			else:
				#dispatcher.utter_message("Movie " + choice)
				dispatcher.utter_message("IMDB score of " + result[0] + " is: " + str(result[1]))
				return[SlotSet("movie.star_rating", result[1])]


class ActionLikes(Action):
	def name(self):
		return "action_likes"

	def run(self, dispatcher, tracker, domain):
		result = []
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
			dispatcher.utter_template("utter_repeat")
		else:
			movie_db = DBManager()
			result = movie_db.get_likes(movie)
			if result[1] is None:
				dispatcher.utter_message(error_messages())
			else:
				#dispatcher.utter_message("Movie " + choice)
				dispatcher.utter_message(result[0] + " has " + str(result[1]) + " Facebook likes")
				return[SlotSet("movie.likes", result[1])]

class ActionLink(Action):
	def name(self):
		return "action_link"

	def run(self, dispatcher, tracker, domain):
		result = []
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
			dispatcher.utter_template("utter_repeat")
		else:
			movie_db = DBManager()
			result = movie_db.get_link(movie)
			if result[1] is None:
				dispatcher.utter_message(error_messages())
			else:
				#dispatcher.utter_message("Movie " + choice)
				dispatcher.utter_message(result[0] + " has " + str(result[1]) + " Facebook likes")
				return[SlotSet("movie.imdb_link", result[1])]

class ActionGenres(Action):
	def name(self):
		return "action_genres"

	def run(self, dispatcher, tracker, domain):
		result = []
		genres = []
		butt_dict_key = {}
		buttons = []
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
			dispatcher.utter_template("utter_repeat")
		else:
			movie_db = DBManager()
			result = movie_db.get_genres(movie)
			if result[1] is None:
				dispatcher.utter_message(error_messages())
			else:
				genres = result[1].split("|")
				for el in genres:
					butt_dict_key["title"] = ""
					butt_dict_key["payload"] = el
					buttons.append(butt_dict_key.copy())
				dispatcher.utter_button_message("Genres for " + result[0] + " are: ", buttons)
				return[SlotSet("movie.genre", genres)]

class ActionKeywords(Action):
	def name(self):
		return "action_keywords"

	def run(self, dispatcher, tracker, domain):
		result = []
		keywords = []
		butt_dict_key = {}
		buttons = []
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
			dispatcher.utter_template("utter_repeat")
		else:
			movie_db = DBManager()
			result = movie_db.get_keywords(movie)
			if result[1] is None:
				dispatcher.utter_message(error_messages())
			else:
				keywords = result[1].split("|")
				for el in keywords:
					butt_dict_key["title"] = ""
					butt_dict_key["payload"] = el
					buttons.append(butt_dict_key.copy())
				dispatcher.utter_button_message("Plot keywords for " + result[0] + " are: ", buttons)
				return[SlotSet("movie.plot_keywords", genres)]


class ActionLanguage(Action):
	def name(self):
		return "action_language"

	def run(self, dispatcher, tracker, domain):
		result = []
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
		else:
			movie_db = DBManager()
			result = movie_db.get_language(movie)
			if result[1] is None:
				dispatcher.utter_message(error_messages())
			else:
				dispatcher.utter_message("Language of " + result[0] + " is: " + result[1])
				return [SlotSet("movie.language", result[1])]

class ActionDuration(Action):
	def name(self):
		return "action_duration"

	def run(self, dispatcher, tracker, domain):
		result = []
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
		else:
			movie_db = DBManager()
			result[1] = movie_db.get_duration(movie)
			if result[1] is None:
				dispatcher.utter_message(error_messages())
			else:
				dispatcher.utter_message(result[0] + " lasts:" + result[1])
				return [SlotSet("movie.duration", result[1])]
