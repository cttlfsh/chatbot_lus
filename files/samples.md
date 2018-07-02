## story 0
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* actor_name{"movie_name": "My Date with Drew"}
    - slot{"movie.name": "My Date with Drew"}
    - action_actor
    - slot{"actor.name": "John August"}
* goodbye
    - utter_goodbye

## story 1
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* director_name{"movie_name": "I am Sam"}
    - slot{"movie.name": "I am Sam"}
    - action_director
    - slot{"director.name": "Jessie Nelson"}
* goodbye
    - utter_goodbye

## story 2
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* genre{"movie_name": "Margaret"}
    - slot{"movie.name": "Margaret"}
    - action_genre
    - slot{"movie.genre": "Drama"}
* goodbye
    - utter_goodbye

## story 3
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* language{"movie_name": "Animals"}
    - slot{"movie.name": "Animals"}
    - action_language
    - slot{"movie.language": "English"}
* goodbye
    - utter_goodbye

## story 4
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* budget{"movie_name": "Ordinary People"}
    - slot{"movie.name": "Ordinary People"}
    - action_budget
    - slot{"movie.budget": ""}
* goodbye
    - utter_goodbye

## story 5
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* star_rating{"movie_name": "Trainspotting"}
    - slot{"movie.name": "Trainspotting"}
    - action_score
    - slot{"movie.star_rating": "8.2"}
* goodbye
    - utter_goodbye

## story 6
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* runtime{"movie_name": "Higher Ground"}
    - slot{"movie.name": "Higher Ground"}
    - action_duration
    - slot{"movie.duration": "109"}
* goodbye
    - utter_goodbye

## story 7
* greet
    - utter_greet
    - utter_ask_howcanhelp
    - action_listen
* year{"movie_name": "Q"}
    - slot{"movie.name": "Q"}
    - action_year
    - slot{"movie.duration": "2011"}
* country
    - action_country
    - slot{"movie.release_region": "France"}
* goodbye
    - utter_goodbye




























































