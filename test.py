import json
import datetime
import sys


global f
global f_list
global current_tweet
global tweet_lines

def open_file() :
    f = open("tweetdhead300000.json","r+")

    for lines in f :
        f_list[tweet_lines] = json.load(lines)
        tweet_lines = tweet_lines + 1

    current_tweet = 0 
    f.fseek(0)    


def read_last_tweet() :
    current_tweet = tweet_lines
    print(f_list[current_tweet]['text'])

def read_current_tweet() :
    while True :
        tweet_id = int(input("gine the id of the tweet you want : "))
        if 0<=tweet_id<=tweet_lines :
            break
    
    current_tweet=tweet_id
    
    print(f_list[current_tweet]['text'])

def read_current_tweet_plus() :
    if ((current_tweet + 1) > (tweet_lines)) :
        print("ERROR: The current tweet tap sky!")
    
    current_tweet = current_tweet + 1

def read_current_tweet_minus() :
    if ((current_tweet - 1) < 0) :
        print("ERROR: The current tweet tap the bottom!")
    
    current_tweet = current_tweet - 1

#def delete_current_tweet() :
def print_current_tweet():
    print(f_list[current_tweet]['text'])

def create_tweet() :
    tweets_lines = tweets_lines + 1
    current_tweet = tweets_lines 
    new_text = str(input("gine the text : "))
    f_list.appends({"text":new_text, "create_at":datetime.datetime.now()})


def quit_without_saving() :
    f.close
    print("goodbye!")
    sys.exit()

def quit_without_saving() :
    json.dumps(f_list,f) 
    f.close()
    print("goodbye!")
    sys.exit