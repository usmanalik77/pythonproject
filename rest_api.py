"""" 6. Complete the rest_api.py to call the find_first_non_repeating_character()
7. Call the rest api using for example Postman on your localhost
8. Make a change to the rest api to send and use input param for find_first_non_repeating_character()"""

#TODO Add code here to receive incoming url
from non_repeating_character_finder import NonRepeatingCharacterFinder
from flask import Flask, request

app = Flask (__name__)

@app.route('/')            #first end-point

def home():
    return NonRepeatingCharacterFinder.find_first_non_repeating_character("aabbeccdfgfg")


@app.route('/findNonRepeating')              #second end-point


def nonRepeating():
    output_value = request.args.get('string')
    print(output_value)
    return NonRepeatingCharacterFinder.find_first_non_repeating_character(output_value)

app.run(port=8000)