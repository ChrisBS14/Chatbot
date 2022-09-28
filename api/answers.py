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
        help = "You can choose between these topics 'Teamleader', 'CEO', 'HelpDesk', 'Invoice', 'Location' or 'Application'"
        return payload_helper(help)

    # if the answer is website
    if answer.lower() == "website":
        website = "https://itsolutions555.com/"
        return payload_helper(website)

    # add the answer 'chris' for the user replies
    if answer.lower() == "invoice":
        invoice = "Contact information of Hubert Gröninger - Team Leader IT 1st-Level : Tel: 040/69 69 403, E-Mail:hgroeninger@itsolutions555.com"
        return payload_helper(invoice)

    # add the answer 'CEO' for the user replies
    if answer.lower() == "ceo":
        ceo = "Contact information of CEO Peter Falter: Tel: 040/69 69 303, E-Mail:pfalter@itsolutions555.com"
        return payload_helper(ceo)

    # add the answer 'Teamleader' for the user replies
    if answer.lower() == "teamleader":
        teamleader = "If you want to call them: 040/6969503 or send a Mail to teamleader@itsolutions555.com. If you want to reach a specific support level type in 'level'"
        return payload_helper(teamleader)

    # add the answer 'Level' for the user replies
    if answer.lower() == "level":
        level = "First Level: helpdesk@itsolutions555.com, 2nd Level: serverteam@itsolutions555.com, 3rd Level: datacenter@itsolutions555.com"
        return payload_helper(level)

    # add the answer 'HelpDesk' for the user replies
    if answer.lower() == "helpdesk":
        helpdesk = "If you want to open a Ticket send a Mail to helpdesk@itsolutions555.com or call them at 040/6969603"
        return payload_helper(helpdesk)

    # add the answer 'Location' for the user replies
    if answer.lower() == "location":
        location = "Friedrich-Ebert-Damm 311, 22159 Hamburg"
        return payload_helper(location)

    # add the answer 'Application' for the user replies
    if answer.lower() == "application":
        application = "For applications via mail please send it to Mr. Neutron, Friedrich-Ebert-Damm 311, 22159 Hamburg or via e-Mail: jimmy.neutron@itsolutions555.com for further requirements regarding the job offer please visit our website https://itsolutions555.com/jobapplications/requirements"
        return payload_helper(application)

    # if the answer is bye
    if answer.lower() == "bye":
        return payload_helper("bye bye")

    # if the answer is not in the user replies send a basic robot answer
    payload = payload_helper("You can choose between these topics 'Teamleader', 'CEO', 'HelpDesk', 'Invoice' or 'Location' or 'Application'" )

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
