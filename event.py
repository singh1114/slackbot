import command
import time
import some
from slackclient import SlackClient

app = Celery('tasks', backend='rpc://', broker='pyamqp://localhost')
 
class Event:
    def __init__(self, bot):
        self.bot = bot
        self.command = command.Command()
     
    @app.task
    def send_message_async(channel):
        slack_client = SlackClient("xoxb*********")
        slack_client.api_call("chat.postMessage", channel=channel, text='Hi!', as_user=True)

    def wait_for_event(self):
        events = self.bot.slack_client.rtm_read()
         
        if events and len(events) > 0:
            for event in events:
                #print event
                self.parse_event(event)
                 
    def parse_event(self, event):
        if event and 'text' in event and self.bot.bot_id in event['text']:
            self.handle_event(event['user'], event['text'].split(self.bot.bot_id)[1].strip().lower(), event['channel'])
     
    def handle_event(self, user, command, channel):
        if command and channel:
            print("Received command: " + command + " in channel: " + channel + " from user: " + user)
            response = self.command.handle_command(user, command)
            if(type(response) is int):
                # time to sleep till 12 pm of the timeline
                self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="I will say hi in "+str(response), as_user=True)
                #time.sleep(response)
                self.send_message_async.apply_async([channel], countdown=response)
                # Again to sleep for 24 hrs
                sleep_time = 24*60*60

                #TODO use periodic_task instead of while True: http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
                while True:
                    self.send_message_async.apply_async([channel], countdown=sleep_time)
            else:
                self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)
