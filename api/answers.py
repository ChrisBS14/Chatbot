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

    # if the answer is empty
    if answer == "" or not answer.isalnum():
        rand_num = randNum(database.chatbot_replies.no_text)
        return payload_helper(database.chatbot_replies.no_text[rand_num])

    # if the answer is in the user_replies array
    if answer.lower() in database.user_replies.hello:
        rand_num = randNum(database.chatbot_replies.answers_to_hello)
        return payload_helper(database.chatbot_replies.answers_to_hello[rand_num])

    # if the answer is help
    if answer.lower() == "help":
        help = "You can choose between these topics 'Teamleader', 'CEO', 'Support', 'HelpDesk', 'Invoice' or 'Ticket-Status'"
        return payload_helper(help)

    # if the answer is website
    if answer.lower() == "website":
        website = "If you would like to visit our website then answer with ‘website’"
        return payload_helper(website)

    # add the answer 'chris' for the user replies
    if answer.lower() == "invoice":
        invoice = "Contact data from Hubert Gröninger - Team Leader IT 1st-Level : Telefon: 040/69 69 403, E-Mail:hgroeninger@sit.com"
        return payload_helper(invoice)

    # add the answer 'ceo' for the user replies
    if answer.lower() == "ceo":
        CEO = "Contact data of CEO Peter Falter: Telefon: 040/69 69 303, E-Mail:pfalter@sit.com"
        return payload_helper(CEO)

    # add the answer 'Teamleader' for the user replies
    if answer.lower() == "teamleader":
        Teamleader = "If you want to call them: 040/6969503 or send a Mail to teamleader@sit.com"
        return payload_helper(Teamleader)

    # add the answer 'level' for the user replies
    if answer.lower() == "level":
        Level = "If you want to see an overview about all Departments type in 'level'"
        return payload_helper(Level)

    # add the answer 'HelpDesk' for the user replies
    if answer.lower() == "helpdesk":
        HelpDesk = "If you want to open a Ticket send a Mail to support@sit.com or call them at 040/6969603"
        return payload_helper(HelpDesk)

    # if the answer is bye
    if answer.lower() == "bye":
        return payload_helper("bye bye")

    # if the answer is not in the user replies send a basic robot answer
    payload = payload_helper("You can choose between these topics 'Teamleader', 'CEO', 'Support', 'HelpDesk', 'Invoice' or 'Ticket-Status'" )

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
