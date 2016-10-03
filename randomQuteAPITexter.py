###########################################################################################
# Name: Abhishek Shah
# Date: 04/17/16
# Description: This program uses an API from andrux-net to generate random quotes and texts them to my phone.
###########################################################################################
import unirest, json
from random import randint
from twilio.rest import TwilioRestClient


accountSID = ''
authToken = ''
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilionumber = '+'
myCellPhone = '+'
X_Mashape_Key = ""

# type of the quote generated (usually choose index 0)
types = ['famous', 'movies']
# list of inspirational messages to tag along with each text (randomly selected)
inspirational_messages = ["do great things today.", 
                            "be awesome.", 
                            "you can make a difference.", 
                            "change the world.", 
                            "attitude is everything.", 
                            "if you do not feed from feedback, you will go back."
                            ]

def callback_function(response):
#   print response.code # The HTTP status code
#   print response.headers # The HTTP headers
#   print response.body # The parsed response
#   print response.raw_body # The unparsed response
    
    # get appropiate values from the returned JSON
    quote = response.body['quote']
    author = response.body['author']
    # send the message                                                      
    message = twilioCli.messages.create(body="%s once said: \n%s\nThat said, %s" % 
                                                        # randomly select a message from the inspirational message list
    (author, quote, inspirational_messages[randint(0, len(inspirational_messages) - 1)]),
        from_=myTwilionumber, 
        to=myCellPhone)


# These code snippets use an open-source library.
response = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/",
  headers={
    "X-Mashape-Key": X_Mashape_Key,
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  }, 
  # parameters (for example: ?cat=movies&...)
  params={ 
      "cat": types[0]
  }, 
  callback=callback_function
)
