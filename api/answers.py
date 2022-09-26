import json
from flask import Blueprint, abort, request
import random
import database.chatbot_replies
import database.user_replies



api_answers = Blueprint('answers', __name__, template_folder='templates')


@api_answers.route('/api/answers', methods=['POST'])
def answers():

    # if the request method is not POST, return a 400 error
    if not request.method == "POST":
        return abort(400)

    # get the answer from the user (chat field)
    answer = request.json['answer']

    # if the answer is empt
    if answer == "" or not answer.isalnum():
        rand_num = randNum(database.chatbot_replies.no_text)
        return payload_helper(database.chatbot_replies.no_text[rand_num])

    # if the answer is in the user_replies array
    if answer.lower() in database.user_replies.hello:
        rand_num = randNum(database.chatbot_replies.answers_to_hello)
        return payload_helper(database.chatbot_replies.answers_to_hello[rand_num])

    # if the answer is help
    if answer.lower() == "help":
        help = "You have the following options to get the contact details - 'chris' or 'peter'"
        return payload_helper(help)

    # add the answer 'chris' for the user replies
    if answer.lower() == "chris":
        chris = "Contact data of Chris: Telefon: 0123456789, E-Mail:test@test.test"
        return payload_helper(chris)

    # add the answer 'peter' for the user replies
    if answer.lower() == "peter":
        peter = "Contact data of Peter: Telefon: 0123456789, E-Mail:peter@peter.peter"
        return payload_helper(peter)

    # if the answer is bye
    if answer.lower() == "bye":
        return payload_helper("bye bye")

    # if the answer is not in the user replies send a basic robot answer
    payload = payload_helper("Beep boop beep")

    # return the JSON payload
    return payload



def payload_helper(question: str) -> str:

    # build the JSON payload
    payload = {
        "question": question,
    }

    # turn the variable to a json object and then return it
    payload = json.dumps(payload)

    return payload


# generate a random number with the arrays length
def randNum(array: list):
    return random.randint(0, len(array) - 1)
