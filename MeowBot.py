import praw

r = praw.Reddit(username = "YourUsername", password = 'YourPassword', client_id = 'YourClientID', client_secret = 'YourClientSecret', user_agent = 'MeowBot 0.0.1 by /u/username')

#Choose a subreddit
subr = r.subreddit('funny')
for comment in subr.stream.comments(skip_existing=True):
    try:
        if "cat" in comment.body:
            comment.reply("MEOW MEOW MOTHERFUCKER!!")
    except:
        praw.exceptions.APIException
        print("Probably a rate limit....")