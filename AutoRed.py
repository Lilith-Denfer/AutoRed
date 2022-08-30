from random import randint
import praw
#import tweepy
from datetime import datetime, timedelta
import time
import json
import configparser
import getpass
from cleantext import clean
import csv 


class reddit: 
    def __init__(self,config):
        self.reddit = praw.Reddit(
            client_id= config['CONFIG']['REDDIT_CLIENT_ID'],
            client_secret= config['CONFIG']['REDDIT_CLIENT_SECRET'],
            username= config['CONFIG']['REDDIT_USERNAME'],
            password= config['CONFIG']['REDDIT_PASSWORD'],
            user_agent= '/u/Lilith_Denfer bot')
        self.reddit.validate_on_submit = True
    
    def post(self, subreddit, title, url=None, flair=False, flair_text=None, nsfw=False):
        if flair == False:
            try:
                submission = self.reddit.subreddit(subreddit).submit(title=title,url=url, nsfw=nsfw)
                return submission
            except Exception as exp:
                print('• Exception: {}'.format(exp))
        else:
            try:
                choices = list(self.reddit.subreddit(subreddit).flair.link_templates.user_selectable())
                id = next(x for x in choices if x["flair_text"] == flair_text)["flair_template_id"]
                submission = self.reddit.subreddit(subreddit).submit(title=title, url=url, nsfw=nsfw, flair_id=id)
                return submission
            except Exception as exp:
                print('• Exception: {}'.format(exp))

    def xpost(self, submission, subreddit, flair=False, flair_text=None, nsfw=False):
        if flair == False:
            try:
                newsubmission = submission.crosspost(subreddit, nsfw = nsfw)
                return newsubmission
            except Exception as exp:
                print('• Exception: {}'.format(exp))
        else:
            try:
                choices = list(self.reddit.subreddit(subreddit).flair.link_templates.user_selectable())
                id = next(x for x in choices if x["flair_text"] == flair_text)["flair_template_id"]
                newsubmission = submission.crosspost(subreddit, nsfw=nsfw, flair_id=id)
                return newsubmission
            except Exception as exp:
                print('• Exception: {}'.format(exp))

    def comment(self, submission, comment=''):
        comment = submission.reply(body = comment)
        return comment

    def upvote(self, item):
        item.upvote()

    def delete(self,item):
        item.delete()

# For AutoTwit development.
# class twitter:
#     def __init__(self,config):
#         auth = tweepy.OAuthHandler(
#             access_token= config['CONFIG']['TWITTER_CLIENT_ID'],
#             access_token_secret= config['CONFIG']['TWITTER_CLIENT_SECRET']
#         )
#         auth.set_access_token(
#             key= config['CONFIG']['TWITTER_ACCESS_TOKEN'],
#             secret= config['CONFIG']['TWITTER_ACCESS_TOKEN_SECRET']
#         )
#         self.twitter = tweepy.API(auth)

#     def tweet(self,body):
#         status = self.twitter.update_status(status=body)
#         return status

#•––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––•

log = open('log.txt', 'w')


def post(reddit, row, title, url, comment, wait):
    try:
        sub = row['Name']
        if row['HasFlair'] == 'TRUE':
            submission = reddit.post(sub, title, url, flair=True, flair_text=row['Flair Name'], nsfw=True)
            reddit.comment(submission, comment)
        else:
            submission = reddit.post(sub, title, url, nsfw=True)
            reddit.comment(submission, comment)

        print('• Posted on {}. Post ID: {}'.format(sub, submission.id))
        log.write('• Posted on {}. Post ID: {}\n'.format(sub, submission.id))
        time.sleep(wait*randint(1,180))
    except Exception as exp:
        print('• Exception: {}'.format(exp))


def xpost(reddit,row,post,comment,wait):
    try:
        sub = row['Name']
        if row['HasFlair'] == 'TRUE':
            submission = reddit.xpost(post,sub, flair=True, flair_text=row['Flair Name'], nsfw=True)
            reddit.comment(submission,comment)
        else:
            submission = reddit.xpost(post,sub, nsfw=True)
            reddit.comment(submission, comment)

        print('• Posted on {}. Post ID: {}'.format(sub, submission.id))
        log.write('• Posted on {}. Post ID: {}'.format(sub, submission.id))
        time.sleep(wait)
    except Exception as exp:
        print('• Exception: {}'.format(exp))
    
def isOk(row, is24Mode, isTest, isDick):
    if is24Mode and (row['IsDaily'] == 'TRUE'):
        return False
    elif isTest and (row['IsTest'] == 'FALSE'):
        return False
    elif (not isDick) and (row['dickOnly'] == 'TRUE'):
        return False
    else:
        return True

def isXOk(row,isX):
    if isX and (row['isXOK'] == 'FALSE'):
        return False
    else:
        return True


def comConstruct(row, comments, isX=False):
    comment = comments[0]
    if (row['IsPromoSub'] == 'TRUE'):
        if isX and isXOk(row, isX):
            pass
        else:
            comment = comment + comments[1]

    if row['IsPromoOF'] == 'TRUE':
        comment = comment + comments[2]

    sub = row['Name']
    if sub == 'Shemales':
        comment = clean(comment, no_emoji=True)
    return comment


def funLoad(delay, dotnum):
    for i in range(dotnum):
        time.sleep(delay)
        print('•')
        log.write('•\n')
    time.sleep(delay)


c = configparser.ConfigParser()
c.read('config.ini')
try:
    delay = float(c['CONFIG']['WAIT'])
except KeyError:
    delay = 0.25



def endQuit():
    funLoad(delay, 1)
    print('• Bye!')
    print('•—————————————————————————————————————————————————————————————————————————•')
    log.write('• Bye!\n')
    log.write('•—————————————————————————————————————————————————————————————————————————•\n')
    quit()

def binQues(str):
    yes = ['y', 'yes']
    out = False
    value = input(str + ' (Y/N) ')
    log.write(str + ' (Y/N)\n')
    v = value.lower()
    if v == '':
        log.write('• User answered: No\n')
        return out
    if any(str in v for str in yes):
        log.write('• User answered: Yes\n')
        return True
    return out


def inputQues(str):
    out = False; value = ''
    log.write(str + '\n')
    value = input(str)
    if value == '':
        log.write('• User entered nothing\n')
        return value, out
    funLoad(delay, 0)
    out = binQues('• You entered: "' + value + '" Is this OK?')
    log.write('• You entered: "' + value + '" Is this OK?\n')
    log.write('• User answered: ' + value + '\n')
    if value:
        log.write('• User answered: Yes\n')
    else:
        log.write('• User answered: No\n')
    return value, out

def timeCheck():
    nowTime = datetime.now()
    pastTime = open('time.txt', 'r')
    lastPost = pastTime.read()
    pastTime.close()

    time24 = timedelta(days=1)
    past = datetime.strptime(lastPost, '%m/%d/%Y %H:%M:%S')
    interval = nowTime - past

    out = False
    timeAns = False
    if interval < time24:
        print('• It has not been 24 hours since your last post(s) at {}.'.format(past.strftime('%m/%d/%Y %H:%M:%S')))
        log.write('• It has not been 24 hours since your last post(s) at {}.\n'.format(past.strftime('%m/%d/%Y %H:%M:%S')))
        funLoad(delay, 0)
        timeAns = binQues('• Do you still want to continue with subreddits without 24-hour limits?')
        funLoad(delay, 1)
        if not timeAns:
            log.write('• User answered: No\n')
            endQuit()
    if timeAns:
        log.write('• User answered: Yes\n')
        out = True
    return out 

def timeWrite():
    t = open('time.txt', 'w')
    t.write(datetime.now().strftime('%m/%d/%Y %H:%M:%S'))
    t.close()

def getPost(is24Mode):
    isTest = False
    isDick = False
    isX = False
    title = ''
    url = ''
    
    
    readFromCSV = binQues('• Would you like to read from CSV?')
    funLoad(delay, 1)
    if readFromCSV:
        with open('posts.csv', newline='') as csvfile:
            posts = csv.DictReader(csvfile)
            count = 0
            for row in posts:
                if row['Date'] == (datetime.now().strftime('%m/%d/%Y')):
                    count = count + 1
                    if count > 1:
                        print('• Too many posts for today in table!')
                        log.write('• Too many posts for today in table!\n')
                        endQuit()
                    
                    if row['IsTest'] == 'TRUE':
                        isTest = True

                    if row['HasDick'] == 'TRUE':
                        isDick = True

                    if not is24Mode and (row['Is24Mode'] == 'TRUE'):
                        is24Mode = True
                    
                    title = row['Title']
                    url = row['Imgur Link']
                
            if count == 0:
                print('• Current date not in table')
                log.write('• Current date not in table\n')
                endQuit()
    else:
        title, out1 = inputQues('• Enter a Title: ')
        funLoad(delay, 1)
        if not out1:
            print('• Bye!')
            log.write('• Bye!\n')
            quit()
        isTest = binQues('• Is this post a test?')
        funLoad(delay, 1)
        isDick = binQues('• Does this post include 🍆?')
        funLoad(delay, 1)
        url, out2 = inputQues('• Please paste link url here: ')
        funLoad(delay, 1)
        if not out2:
            endQuit()
        if not is24Mode:
            is24Mode = binQues('• Would you like to skip 24-hour limit subs?')
        
    isX = binQues('• Would you like to crosspost from FemCreators?')
    funLoad(delay, 1)
    return [isTest,isDick,is24Mode,title,url,isX]



def main():

    print('•———————————————————————————————————————————————————————————————•')
    log.write('•———————————————————————————————————————————————————————————————•\n')
    funLoad(delay, 0)
    print('• Starting AutoRed 5.0')
    log.write('• Starting AutoRed 5.0\n')
    funLoad(delay, 2)
    print('• Welcome to AutoRed:')
    log.write('• Welcome to AutoRed:\n')
    funLoad(delay, 0)
    print('• An excellent app crafted to help post your smut online ;)')
    log.write('• An excellent app crafted to help post your smut online ;)\n')
    funLoad(delay, 2)


    is24Mode = timeCheck()

    config = configparser.ConfigParser()
    config.read('config.ini')
    try:
        config['CONFIG']['REDDIT_PASSWORD']
    except KeyError:
        config['CONFIG']['REDDIT_PASSWORD'] = getpass('• Password for Reddit account ' + config['CONFIG']['USERNAME'] + ': ')
        funLoad(delay, 1)
    try:
        wait = float(config['CONFIG']['WAIT'])
    except KeyError:
        wait = 1

    autoRed = reddit(config)
    
    items = getPost(is24Mode)
    isTest = items[0]
    isDick = items[1]
    is24Mode = items[2]
    title = items[3]
    url = items[4]
    isX = items[5]

    print('• Title: {}'.format(title))
    log.write('• Title: {}\n'.format(title))
    funLoad(delay, 0)
    print('• Url: {}'.format(url))
    log.write('• Url: {}\n'.format(url))
    funLoad(delay, 1)
    cont=binQues('• Does this look okay?')
    funLoad(delay, 1)
    if not cont:
        endQuit()


    if len(url) < 7:
        print('• url is too short ')
        log.write('• url is too short\n')
        endQuit()
    elif url.startswith('https://i.imgur.com/') or url.startswith('https://redgifs.com/watch/'):
        with open('comments.json') as f:
            info = json.load(f)
        for item in info['Items']:
            comments = [item['General Comment'], item['Sub Promo'], item['OF Promo']]
    

        xPostSub = 'FemCreators'
        if isX:
            initPost = autoRed.post(xPostSub, title, url, flair=True, flair_text='Photo', nsfw=True)
            print('• Reference Post on {}. Post ID: {}'.format(xPostSub, initPost.id))
            log.write('• Reference Post on {}. Post ID: {}\n'.format(xPostSub, initPost.id))
            funLoad(wait,1)
    
        with open('subreddits.csv', newline='') as csvfile:
            subreddits = csv.DictReader(csvfile)
            count = 0
            sub_count = 0
            for row in subreddits:
                comment = comConstruct(row,comments,isX)
                if isOk(row,is24Mode,isTest,isDick):
                    if isX and isXOk(row,isX):
                        if row['Name'] != xPostSub:
                            xpost(autoRed,row,initPost,comment,wait)
                            count = count + 1
                    else:
                        post(autoRed,row,title,url,comment,wait)
                        count = count + 1
                sub_count = sub_count + 1
            if not isTest and not is24Mode:        
                timeWrite()
            print('• Posted on ({}/{}) Subs '.format(count, sub_count))
            log.write('• Posted on ({}/{}) Subs\n'.format(count, sub_count))
            endQuit()
    else:
        if url.startswith('https://imgur.com/'):
            print('• Url is not from a proper host type, use the direct link ')
            log.write('• Url is not from a proper host type, use the direct link \n')
        else:
            print('• Url is not from a proper host type ')
            log.write('• Url is not from a proper host type\n')
        endQuit()


if __name__=='__main__':
    main()

log.close()
