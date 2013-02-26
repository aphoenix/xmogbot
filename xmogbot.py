import praw
import time


user_agent = "aphoenix's bot for the Transmogrification subreddit"
thing_limit = 15 


r = praw.Reddit(user_agent=user_agent)
r.login('aptbot','yTp["H]iP]<iHveX2:]oJo\Yp')
xmog = r.get_subreddit('Transmogrification')


cloth = ['cloth','warlock','mage','priest','cloth', 'lock','demonology','demo',
                        'destro','affliction','shadow']
leather = ['leather','rogue','druid','monk','leather','boomkin','kitty','feral',
                        'assassination','mutliation']
mail = ['mail','hunter','shaman','mail','huntard','shammy','totem']
plate = ['plate','warrior','death knight','dk','pally','paladin','plate'] 
meta = ['meta','help']
types = [cloth,leather,mail,plate,meta]


updated = """Your friendly neighbourhood flairbot added flair to your post
            automatically. If your flair is in error, please do not
            hesitate to tell /u/aphoenix about it."""


finito = []


def checkarmor(type, submission):
    '''check against armor type keywords in title to auto assign flair'''
    if any (word in submission.title.lower() for word in type):
        print 'setting flair for ' + submission.id + ' to ' + type[0]
        try:
            submission.set_flair(submission.id,type[0].capitalize,type[0])
            submission.add_comment(updated)
            finito.append(submission.id)
        except Exception:
            print 'did not add flair'


running = True
while (running):
    for submission in xmog.get_hot(limit=thing_limit):
        if (submission.link_flair_text == None and submission.id not in finito):
            for type in types:
                checkarmor(type, submission)
    time.sleep(180)
