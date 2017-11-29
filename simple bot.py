import os
import time
import schedule
from slackclient import SlackClient
from flask import Flask, request, Response, jsonify

SLACK_TOKEN = 'xoxp-278618040055-278416006470-277594264468-9731ab76b3f41c85868b37dfd5e4ab28'
#SLACK_TOKEN = os.environ.get('SLACK_TOKEN',None)
slack_client = SlackClient(SLACK_TOKEN)

app = Flask(__name__)

SLACK_WEBHOOK_SECRET = 't7XAxGhTYIruj4OB0hqwycxq'

def send_message(channel_id, message):
	slack_client.api_call(
		"chat.postMessage",
		channel=channel_id,
		text=message,
		username='HiBOT',
		icon_emoji=':robot_face:'
		)

@app.route('/slack', methods=['POST'])
def slack():
	if request.form.get('token') == SLACK_WEBHOOK_SECRET :
	    text = request.form.get('text', '')
	    channel = request.form.get('channel_name')
	    username = request.form.get('user_name')
	    if 'wish' in text.lower() :
	    	schedule.every(1).minute.do(send_message(channel,"Hi "+username+" how are you doing :) !!"))
	        while True:
	        	schedule.run_pending()
	        	time.sleep(1)
	        #return jsonify(text="Hi "+username+" how are you doing :) !!")
    	return Response(), 200


if __name__ == "__main__":
	app.run(debug=True)