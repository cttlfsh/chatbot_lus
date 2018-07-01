# Development of Dialog System within Rasa in the Movie Domain

This is the final project of the Language Understanding System course, the aim is to develop o Dialog System within Rasa in the Movie Domain capable of understanding what the user requires and of providing the correct answer.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To succesfully run the project you need to download two external tool:  
   
* Rasa-Core, see [RasaCore](https://github.com/RasaHQ/rasa_core)
* Rasa-NLU, see [RasaNLU](https://github.com/RasaHQ/rasa_nlu)
* Rasa additional dependecies: 
   * Spacy, see [Spacy](https://spacy.io/usage/)
   * CRF Suite, through pip

   ```
   pip install sklearn_crfsuite
   ```   


### Make the project run

To run the system, the procedure is very straight:  

* From terminal, move to the /scripts folder  

```
cd scripts
```

* Choose which options you want to perform between training the NLU, training the dialogue manager and run and launch the script with the respective parameter  

```
python bot.py <parameter>
```
with <parameter> from train-nlu, train-dialogue, run  

* The python script will perform all requested action


## Deployment 
1. train-nlu  
   First action to be performed. Main operations are:  
   
   * Load the training data   
   * Pass the domain file (.yml) to the Trainer
   * Train the NLU
   * Results are stored in:

   ```
   /models/default/chat
   ```

2. train-dialogue
   To be performed immediately after the training of the NLU, main operations are:  
   
   * Create the RasaNLUInterpreter with the result of the previous training as input   
   * Create the Agent and setting its caracteristics: Policies (Memoization, Keras), Interpreter, configuration file of the NLU
   * Train the Agent with the stories, namely a file of exaples of conversations
   * (Optional) Enable the "Training online", that allows you to manually correct bot intents/actions to improve its precision
   * Results are stored in:

   ```
   /models/dialogue
   ```

3. run  
   * Load the interpreter   
   * Pass the interpreter to the agent
   * Run the bot

## Authors

* **Andrea Montagner** - *ID:189514*

