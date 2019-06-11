from flask import Flask, request
import json
from bot import Bot
PAGE_ACCESS_TOKEN = 'EAAEXm0CJeicBAOwLUXFCsejHYcJGC4isNkNTzG9sB2uMDNZCJ8rOuNhXKaBqw5ZALYmvulIHyirDWxcYZAXpY0xu4zgTdYZC0sIe4JLXX4ftWmLWCAwUuOMZC26GNV3AFn1FzGZAQyzCznz8rTNrow5JpljDoCRrJE2UrHNOfbHky5GYoRm9ZCs'

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def verify():    
    token = request.args.get('hub.verify_token')
    challenge= request.args.get('hub.challenge')
    #to verify the token in our fb
    #stop s.o else from intercepting
    if token == 'secret':
        return str(challenge)
    return '400 '#bad request
    #It could not be called if it is an integer
#405 method not allowed

@app.route('/', methods = ['POST'])
def webhook():
    #print what we get from fb
    data = json.loads(request.data)        
    messaging_events = data['entry'][0]['messaging']
    bot = Bot(PAGE_ACCESS_TOKEN)

    for message in messaging_events:
        user_id = message['sender']['id']
        #get only text message from user
        text_input = message['message'].get('text')
        print(f'message from user id {user_id} : {text_input}')
        bot.send_text_message(user_id, 'hello world')
    return '200'

#write the code for the development server
#run this module only if someone get custom module
#won't run it if someone tries to import it
if __name__ == '__main__':
    #run in debug mode
    # if make any code changes, development server refreshes automatically
    app.run(debug = True)

    