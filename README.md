# slackbot
A simple slack bot


## Installations

### Using pip

- Fork the repo

`$ virtualenv slackbot`

`$ cd slackbot`

`$ source bin/activate`

`$ pip install slackclient`

`$ git clone https://github.com/YOUR_GITHUB_USERNAME/slackbot`

- change YOUR_GITHUB_USERNAME by your username

`$ cd slackbot`

- Fill in the details of bot in `bot.py` in line _7_ and _8_

`$ python anotherbot.py`

- Now, in the message box of slack, refer to your bot like @Your_bot_name `timezone`.

- Use the following format for timezone

- if it is +0530 use +5.5
- if it is -0550 use -5.5

- The bot will send a message at 12;00 pm refering to you.
