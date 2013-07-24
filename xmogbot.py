import praw
import time
try:
    import creds
except ImportError:
    print "Must have creds.py with valid reddit login credentials. uid pw"
    exit()


user_agent = "aphoenix's bot for the Transmogrification subreddit"
thing_limit = 25 


r = praw.Reddit(user_agent=user_agent)
r.login(creds.uid,creds.pw)
xmog = r.get_subreddit('Transmogrification')


cloth = ['cloth','warlock','mage','priest','cloth', 'lock','demonology','demo',
                        'destro','affliction','shadow']
leather = ['leather','rogue','druid','monk','leather','boomkin','kitty','feral',
                        'assassination','mutliation']
mail = ['mail','hunter','shaman','mail','huntard','shammy','totem']
plate = ['plate','warrior','death knight','dk','pally','paladin','plate'] 
meta = ['meta','help']
types = [cloth,leather,mail,plate,meta]


thanks = ['thanks', 'thank you', 'awesome', 'obliged']
welcome = ['No problem!', 'You\'re welcome.', 'I live but to serve.', 'Happy to help!', 'Don\'t mention it', 'No worries.']


fightinwords = ['shit', 'piss', 'cunt', 'fuck', 'cocksucker', 'motherfucker', 'tits']
realbadwords = ['nigger', 'faggot', 'whore']


flagurls = ['imgur','min.us']


def explainupdate(flair):
    '''Tells the user which flair they received'''
    updated = " I tagged your post as "
    updated += flair
    updated += ". If it's wrong, tell the mods."
    return updated

# already taken care of = atco
# f = flair
# i = item list
atcof = []
atcoi = []


def checkarmor(type, submission):
    '''check against armor type keywords in title to auto assign flair'''
    if any (word in submission.title.lower() for word in type):
        print 'setting flair for ' + submission.id + ' to ' + type[0].capitalize()
        try:
            submission.set_flair(type[0].capitalize(),type[0])
            submission.add_comment(explainupdate(type[0].capitalize()))
            atcof.append(submission.id)
        except Exception:
            print 'did not add flair'


#def checkitemlist(submission):
#    '''check to see if the url is imgur or min.us. Then, if there are
#    no comments by the OP, tell them to post an item list.'''
#    if any (word in flagurls for word in submission.getinfo(url) and 
#                            submission.id not in atcoi):
#        for comment in submission.get_comments():
#            get_comments


running = True
while (running):
    try:
        for submission in xmog.get_hot(limit=thing_limit):
            if (submission.link_flair_text == None and submission.id not in atcof):
                for type in types:
                    checkarmor(type, submission)
        for message in r.get_unread(limit=thing_limit):
            print message.body
            print message.author
        time.sleep(600)
    except:
        print 'reddit timed out a bit there'
        time.sleep(1200)
