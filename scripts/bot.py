from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.events import SlotSet
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_core.channels.telegram import TelegramInput
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.interpreter import RasaNLUInterpreter, RegexInterpreter



import argparse
import logging
import sys

DATA = "../files/nlu_data.json"
CONFIG_NLU = "../models/config_nlu.yml"
CONFIG = "../models/domain.yml"
MODEL_DIR = "../models"
MODEL_DIALOGUE = "../models/dialogue"
CHAT = "../models/default/chat"

STORIES = "stories.md"


def train_nlu():
    training_data = load_data(DATA)
    trainer = Trainer(config.load(CONFIG_NLU))
    trainer.train(training_data)
    model_directory = trainer.persist(MODEL_DIR, fixed_model_name = 'chat')
    return model_directory

def train_dialogue():
    interpreter = RasaNLUInterpreter(CHAT)
    agent = Agent(CONFIG, policies=[MemoizationPolicy(max_history=3), KerasPolicy()], interpreter=interpreter)

    training_data = STORIES ###TODO
    agent.train(
            training_data,
            epochs=500,
            batch_size=100,
            validation_split=0.3
    )
    agent.persist(MODEL_DIALOGUE)

    # input_channel = TelegramInput(
    #     access_token="577522303:AAG6_5NcdBVRq-ndzThybnOh7SHL9I2ylKo", # you get this when setting up a bot
    #     verify="chatmoviedomainbot", # this is your bots username
    #     webhook_url="https://07958fff.ngrok.io" # the url your bot should listen for messages
    # )

    input_channel = ConsoleInputChannel()
    agent.train_online(
                training_data,
                input_channel=input_channel,
                epochs=400,
                batch_size=100
        )
    
    return agent

def run(serve_forever=True):
    interpreter = RasaNLUInterpreter(CHAT)
    agent = Agent.load(MODEL_DIALOGUE, interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent



if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            'task',
            choices=["train-nlu", "train-dialogue", "run"],
            help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "run":
        run()