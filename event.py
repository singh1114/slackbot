import command
import time
 
class Event:
    def __init__(self, bot):
        self.bot = bot
        self.command = command.Command()
     
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
                time.sleep(response)
                self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="Hi!", as_user=True)

                # Again to sleep for 24 hrs
                while(True):
                    time.sleep(24*60*60)
                    self.bot.slack_client.api_call("chat.postMessage", channel=channel, text="Hi!", as_user=True)
            else:
                self.bot.slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)