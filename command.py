from datetime import datetime
from datetime import timedelta
import time
import re

class Command(object):
    
    def __init__(self):
        self.commands = { 
            "jump" : self.jump,
            "help" : self.help,
            "timezone" : self.timezone,
        }
 
    def handle_command(self, user, command):
        response = "<@" + user + ">: "
     
        if command in self.commands:
            response += self.commands[command]()
        elif re.match(r'^[+-]?\d+[.]?\d+?$', command):
            utc_time = datetime.utcnow()
            print(utc_time)

            timezone_time = utc_time + timedelta(hours=float(command))
            print(timezone_time)

            utc_hour = utc_time.hour + utc_time.minute / 60 + utc_time.second / 3600

            if(timezone_time.hour<12):
                time_till_noon = 11 - timezone_time.hour
                print(time_till_noon)
                seconds_remaining = time_till_noon * 60 * 60 + (59-timezone_time.minute) * 60 + (59-timezone_time.second)
            else:
                time_till_noon = 36 - timezone_time.hour
                seconds_remaining = time_till_noon * 60 * 60 - timezone_time.minute * 60 - timezone_time.second

            print(seconds_remaining)

            response = seconds_remaining
        else:
            response += "Sorry I don't understand the command: " + command + ". " + self.help()
         
        return response
         
    def jump(self):
        return "Kris Kross will make you jump jump"

    def timezone(self):
        return "What is your timezone?"

     
    def help(self):
        response = "Currently I support the following commands:\r\n"
         
        for command in self.commands:
            response += command + "\r\n"
             
        return response