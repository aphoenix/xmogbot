#This is the bot for the Transmogrification subreddit.

##WHAT IT DOES

- scans for flair keywords
- adds flair
- leaves a comment in the thread that it did something
- completely ignores posts that don't fit a pattern (see TODO)
- 'logs' to screen

##TODO

- smarter logging -> post to /r/aptbot?
- add reminders to post gear lists


##REQUIREMENTS

Built on top of [praw](/praw-dev/praw).

Requires an additional file called creds.py which only requires
a uid and pw:

uid = "scoobydoo"           # your userid
pw = "scoobydoopassword"    # your password

is sufficient.




