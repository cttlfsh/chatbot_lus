from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import random

# from policy import RestaurantPolicy, ScriptedPolicy
from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.channels.telegram import TelegramInput
from rasa_core.events import SlotSet, AllSlotsReset, Restarted
from rasa_core.interpreter import RasaNLUInterpreter, RegexInterpreter
from rasa_core.policies.memoization import MemoizationPolicy

from db_manager import DBManager


slots = ["movie.name", "movie.genre", "movie.country", 
			"movie.year", "movie.language", "actor.name",
			"director.name", "movie.budget", "movie.duration",
			"language", "color", "country", "year", "plot_keywords",
			"score", "likes"
		]

LINK_TO_DB = "mysql://lus:lus@localhost:3306/moviedb"

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

class ActionMovie(Action):
	def name(self):
		return "action_movie"

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message("Catchphrase. Searching...")

		dic = {}
		for s in slots:
			dic[s] = tracker.get_slot(s)

		movie_db = DBManager(LINK_TO_DB)
		res = movie_db.get_title(**dic)

		if dic is None:
			dispatcher.utter_message("My database does not contain the movie you are searching")
		else:
			dispatcher.utter_message("Got you! The search gave this output: " + res[0])

		return [SlotSet("movie.name", res[0])]


class ActionActor(Action):
	def name(self):
		return "action_actor"

	def run(self, dispatcher, tracker, domain):
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
		else:
			movie_db = DBManager(LINK_TO_DB)
			act_list = movie_db.get_actor(movie)

			if act_list is None:
				dispatcher.utter_message(error_messages())
			else:
				### if there is more than 1 actor, keep the first
				### one, that is the main actor
				if "|" in act_list:
					a = act_list.split("|")[0]
				else: 
					a = act_list
				dispatcher.utter_message("Actor name for " + movie + " is " + a)
				return [SlotSet("actor.name", a)]


class ActionDirector(Action):
	def name(self):
		return "action_director"

	def run(self, dispatcher, tracker, domain):
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
		else:
			movie_db = DBManager(LINK_TO_DB)
			director = movie_db.get_director(movie)

			if director is None:
				dispatcher.utter_message(error_messages())
			else:
				dispatcher.utter_message("Director of the movie " + movie + " is " + director)
				return[SlotSet("director.name", director)]

class ActionGenre(Action):
	def name(self):
		return "action_genre"

	def run(self, dispatcher, tracker, domain):
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
		else:
			movie_db = DBManager(LINK_TO_DB)
			genre_list = movie_db.get_genre(movie)

			if genre_list is None:
				dispatcher.utter_message(error_messages())
			else:
				genre = genre_list.split("|")[0]
				dispatcher.utter_message("Main genre for " + movie + " is: " + genre)
				return(SlotSet("movie.genre", genre))

class ActionCountry(Action):
	def name(self):
		return "action_country"

	def run(self, dispatcher, tracker, domain):
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
		else:
			movie_db = DBManager(LINK_TO_DB)
			country = movie_db.get_country(movie)

			if country is None:
				dispatcher.utter_message(error_messages())
			else:
				dispatcher.utter_message("The film was made in:" + country)
				return [SlotSet("movie.release_region", country), SlotSet("country.name", country), SlotSet("movie.location", country)]

class ActionYear(Action):
	def name(self):
		return "action_year"

	def run(self, dispatcher, tracker, domain):
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
		else:
			movie_db = DBManager(LINK_TO_DB)
			year = movie_db.get_year(movie)

			if year is None:
				dispatcher.utter_message(error_messages())
			else:
				dispatcher.utter_message("The film was made in:" + str(year))
				return [SlotSet("movie.release_date", str(year))]


class ActionLanguage(Action):
	def name(self):
		return "action_language"

	def run(self, dispatcher, tracker, domain):
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
		else:
			movie_db = DBManager(LINK_TO_DB)
			language = movie_db.get_language(movie)

			if language is None:
				dispatcher.utter_message(error_messages())
			else:
				dispatcher.utter_message("Language of " + movie + " is: " + language)
				return [SlotSet("movie.language", language), SlotSet("language", language)]

class ActionDuration(Action):
	def name(self):
		return "action_duration"

	def run(self, dispatcher, tracker, domain):
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
		else:
			movie_db = DBManager(LINK_TO_DB)
			duration = movie_db.get_duration(movie)

			if language is None:
				dispatcher.utter_message(error_messages())
			else:
				dispatcher.utter_message("The film lasts:" + duration)
				return [SlotSet("movie.duration", duration)]

class ActionBudget(Action):
	def name(self):
		return "action_budget"

	def run(self, dispatcher, tracker, domain):
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
		else:
			movie_db = DBManager(LINK_TO_DB)
			budget = movie_db.get_budget(movie)

			if budget is None:
				dispatcher.utter_message(error_messages())
			else:
				dispatcher.utter_message("The film had a budget of: " + budget + " mln")
				return [SlotSet("movie.budget", budget)]

class ActionScore(Action):
	def name(self):
		return "action_score"

	def run(self, dispatcher, tracker, domain):
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
		else:
			movie_db = DBManager(LINK_TO_DB)
			rating = movie_db.get_score(movie)

			if rating is None:
				dispatcher.utter_message(error_messages())
			else:
				return [SlotSet("score", rating)]

class ActionLike(Action):
	def name(self):
		return "action_likes"

	def run(self, dispatcher, tracker, domain):
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
		else:
			movie_db = DBManager(LINK_TO_DB)
			likes = movie_db.get_likes(movie)

			if likes is None:
				dispatcher.utter_message(error_messages())
			else:
				return [SlotSet("likes", likes)]

class ActionGross(Action):
	def name(self):
		return "action_gross"

	def run(self, dispatcher, tracker, domain):
		movie = tracker.get_slot("movie.name")
		if movie is None:
			dispatcher.utter_message(error_messages())
		else:
			movie_db = DBManager(LINK_TO_DB)
			gross = movie_db.get_gross(movie)

			if gross is None:
				dispatcher.utter_message(error_messages())
			else:
				return [SlotSet("likes", gross)]

