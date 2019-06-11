import requests
import json

#https://graph.facebook.com/v3.3/me/messages?access_token=<PAGE_ACCESS_TOKEN>
FACEBOOK_GRAPH_URL = 'https://graph.facebook.com/v3.3/me/'

class Bot(object):
    #if user doesn't provide any url, then we'll use default
    def __init__(self, access_token, api_url = FACEBOOK_GRAPH_URL):
        self.access_token = access_token
        self.api_url = api_url
    def send_text_message(self, psid, message, messaging_type='RESPONSE'):
        headers = {
            'Content-Type': 'application/json'
        }

        data = {
            'messaging_type' : messaging_type,
            'recipient': {
                'id': psid
            },
            'message':{
                'text': message
            }
        }

        params = {'access_token': self.access_token}
        self.api_url = self.api_url + 'messages'
        #response to user
        response = requests.post(self.api_url,headers = headers, params = params, data = json.dumps(data))
        print(response.content)

#PAGE_ACCESS_TOKEN
# bot = Bot('EAAEXm0CJeicBAOwLUXFCsejHYcJGC4isNkNTzG9sB2uMDNZCJ8rOuNhXKaBqw5ZALYmvulIHyirDWxcYZAXpY0xu4zgTdYZC0sIe4JLXX4ftWmLWCAwUuOMZC26GNV3AFn1FzGZAQyzCznz8rTNrow5JpljDoCRrJE2UrHNOfbHky5GYoRm9ZCs')
#get the user_id == id of the sender
# bot.send_text_message(2138535822930395, 'Testing....')

'''
curl -X POST -H "Content-Type: application/json" -d '{
  "messaging_type": "<MESSAGING_TYPE>",
  "recipient": {
    "id": "<PSID>"
  },
  "message": {
    "text": "hello, world!"
  }
}' "https://graph.facebook.com/v3.3/me/messages?access_token=<PAGE_ACCESS_TOKEN>"
'''
