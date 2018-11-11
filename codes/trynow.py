import tweepy
import time
import json
import os

auth = tweepy.OAuthHandler("7vle689cxEvLicIJBR3viEi26", "nKGkPpGEC6BWGznRUhyHZ8TSrdsWzBMWSk9PFca0AWyzpED0Wt")
auth.set_access_token("1097206363-JQ14FwNwNcOotuQ0nuWOp41SXc95y5NNfFVgw7R", "a5bYf21KMi726FKNnkFZcxB7nCDvPx5aXKYWjv6Fgoaf1")

api = tweepy.API(auth)
with open("Twitter.txt") as f:
    content = f.readlines()
f = open("userids_0.txt","w")
users = []
mapevents = {}
wrongdat = []
with open("wrongdata.txt","r") as wf:
    wcont = wf.readlines()
    wcont = [w.strip() for w in wcont]
print(wcont)
for x in content:
    indus = []
    words = x.split()
    tostop = 0
    evid = words[0].split(":")
    print(evid)
    if evid[1] not in wcont:
        continue
    labid = words[1].split(":")
    if len(words)>502:
        continue
    newf = open(evid[1] + "_" + labid[1] + ".txt", "w")
    newf.write("[")
    for y in range(2,len(words)):
        print(words[y])
        try:
            tweet = api.get_status(words[y])
            user = tweet.user.id
            if user not in indus:
                indus.append(user)

            json.dump(tweet._json,newf)
            if y == len(words)-1:
                newf.write("]")
            else:
                newf.write(",")
        except tweepy.RateLimitError, re:
            print("rest now")
            time.sleep(60 * 15)
        except tweepy.TweepError, e:

            print e
            if y == len(words)-1:
                newf.seek(-1, os.SEEK_END)
                newf.truncate()
                newf.write("]")

    print("writing an event \n")
    ids = ",".join(str(x) for x in indus)
    #f.write("\n"+words[0]+" "+ids+"\n")
print(len(users))
print(len(mapevents))
print("DONE")