import os, sys
from flask import Flask, request
from pymessenger import Bot
from LogisticRegression.chat_using_LogisticRegression import chat_bot_LR

app = Flask("My bot")

verify_token = os.getenv('VERIFY_TOKEN', None)
access_token = os.getenv('ACCESS_TOKEN', None)
my_app_secret =os.getenv('app_secret', None)
# FB_ACCESS_TOKEN ='EABakQxDO86ABOyaTjPYRmPu6wZCwbvAQKroKo1Y86EpdP3Fahmfo5vp4hSQYUcnZCD8LIZCNrM3CfxuywO61T3GCNUWySqVeIPDZCi1bPBt4Fwh1x6wVvZBOtZCPenbSztTkjU3bhgPddjGmylV4m2pJaDa2t2H4aFZAlYW5HglmBDKCZAaZB9jltz9Bvfk7Mvw7c2Q2yLCDN5usBZAcXT'
bot = Bot(access_token,app_secret=my_app_secret)


@app.route('/webhook', methods = ['GET'])
def verify():
    print(request.args)
    # Xác minh webhook
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == verify_token:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200

@app.route('/webhook', methods=['POST'])
def webhook():
	print(request.data)
	data = request.get_json()
	if data['object'] == "page":
		entries = data['entry']
		for entry in entries:
			messaging = entry['messaging']
			for messaging_event in messaging:
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']
				if messaging_event.get('message'):
					# HANDLE NORMAL MESSAGES HERE
					if messaging_event['message'].get('text'):
						print(messaging_event['message'].get('text'))
						# HANDLE TEXT MESSAGES
						query = chat_bot_LR(messaging_event['message']['text'])
						# ECHO THE RECEIVED MESSAGE
						bot.send_text_message(sender_id, query)
					if messaging_event['message'].get('attachments'):
						for att in messaging_event['message'].get('attachments'):
							if att['type'] == "image":
								attachment_url = att['payload']['url']
								bot.send_image_url(sender_id, attachment_url)	
								bot.send_text_message(sender_id, 'Did you just send me this image?')						
	return "ok", 200


if __name__ == "__main__":
    app.run(port=8000, use_reloader = True, debug=True)
