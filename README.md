###############

# DETAILS OF PROJECT

###############

1. # non_repeating_character_finder.py

   In the "class NonRepeatingCharacterFinder" function is defined as "find_first_non_repeating_character". With characters as an argument of this function, it is looped with each items of characters. if characters.count(i) == 1, it will return that item.

2. # app.py
   Function from class NonRepeatingCharacterFinder is imported in app.py and then called in the "main function". It takes characters argument as string, which in this case is "aabbeccdfgfg". This is stored in variable named as output_value. This is printed with the first non-repeating item of string.

(I found FIRST TWO steps easy when I did some thinking on my own and was later on able to do it

(NEXT STEPS I did were with bit of help from internet sources)

3. # rest_api.py

   To create our own client-server model. I had to create both client and server first. Python server was with the help of "flask framework". I found it very user friendly as it contains many stored functions within its framework like app.run(port=8000). Installing flask using "pip install flask".
   from NonRepeatingCharacterFinder imported non_repeating_character_finder.  
   Gave it first end point using flask by @app.route('/'). This will execute the function "non_repeating_character_finder" on local machine and shows it on terminal (http://127.0.0.1:8000) when server is run by command app.run(port=8000)

4. # Using Postman Client

   I installed Postman application to use it as client. Added new Collection and inserted local host url http://127.0.0.1:8000 in "Get". Then "Send" the request to server. Server takes the request from Client in the rest_api.py folder, takes the first end point ('/') and gives the response to client as "e". Which is first non-repeating character from the hard-coded string "aabbeccdfgfg" executed by find_first_non_repeating_character function.

5. # Send input param

   Then I created 2nd end point as by @app.route('/findNonRepeating'). Defined new function as nonRepeating.
   In the Postman, used this end point and gave it some query parameters. Tried different query parameters and tried debugging the erros which came on client such "Error 404" and "Error 500".
   Gave query parameter and changed the string http://127.0.0.1:8000/findNonRepeating?string=hhgghghssj.

6. # Use Input Parameter
   To request the input query parameter in flask we import request from flask.
   Then this query parameter which is equal to string is requested by request.args.get('string').
   This query parameter is extracted and stored in output_value.
   By returning this output_value as an argument of find_first_non_repeating_character function from NonRepeatingCharacterFinder, we get the first non-repeating character of desired input query parameter.
