import json
from datetime import datetime
import sys

TWEETS = []
CURRENT_ID = 0

def print_menu():
    print ('\n--------------------------------------------------------------\n')
    print ('\nActions:\n')
    print ('c -> Create tweet. Sets current tweet ID to be the created one.\n')
    print ('r<number> -> Read the tweet at line/with ID <number>. Sets current tweet ID to be the read one\n')
    print ('u<number> -> Update the tweet at line/with ID <number>. Sets current tweet ID to be the updated one.\n')
    print ('d- > Delete current tweet.\n')
    print ('$ -> Read the last tweet in the file. Sets current tweet ID to be the last one.\n')
    print ('- -> Read one tweet up from the current tweet.\n')
    print ('+ -> Read one tweet down from your current tweet.\n')
    print ('= -> Print current tweet ID.\n')
    print ('q -> Quit without save.\n')
    print ('w -> (Over)write file to disk.\n')
    print ('x -> Exit and save.\n')
    print ('\n--------------------------------------------------------------\n')

def check_choice(choice):
      correct_choices = ['c','d','$','-','+','=','q','w','x']
      correct_choices_1 = ['r','u']
      return choice[0] in correct_choices_1 or choice in correct_choices or False
      

def create_tweet():
      tweet_text = input("Please, input the text of the tweet:")
      time = datetime.now()
      creation_time = time.strftime("%a %b %d %H:%M:%S +0000 %Y")
      finished_tweet = {"text":tweet_text,"created_at":creation_time}
      TWEETS.append(json.dumps(finished_tweet) + "\n")
      global CURRENT_ID
      CURRENT_ID = len(TWEETS)

def read_with_id(number):
      if(0 <= number < len(TWEETS)):
            global CURRENT_ID
            CURRENT_ID = number
            data = TWEETS[CURRENT_ID]
            c = json.loads(data)
            print(f"\"{data['text']}\" Created at: {data['created_at']}")
      else:
            print("Invalid ID. Try again.\n")

def update_tweet(number):
      if(0 <= number < len(TWEETS)):
            tweet_text = input("Please, input the text of the tweet:")
            time = datetime.now()
            creation_time = time.strftime("%a %b %d %H:%M:%S +0000 %Y")
            finished_tweet = {"text":tweet_text,"created_at":creation_time}
            TWEETS[number] = json.dumps(finished_tweet + "\n")
            global CURRENT_ID
            CURRENT_ID = number
      else:
            print("Invalid ID. Try again.\n")

def deleted_tweets():
      global CURRENT_ID
      del TWEETS[CURRENT_ID]
      if CURRENT_ID >= len (TWEETS) :
            CURRENT_ID -= 1

def print_last():
      global CURRENT_ID
      CURRENT_ID = (len(TWEETS) - 1)
      converted_data = json.loads(TWEETS[-1])
      print (f"\"{converted_data['text']}\" Created at: {converted_data['created_at']}")

def read_prev():
      global CURRENT_ID
      if (CURRENT_ID - 1) < 0 :
            print ("LIMIT REACHED! NO MORE TWEETS ABOVE\n")
      else:
            CURRENT_ID -= 1
            converted_data = json.loads(TWEETS[CURRENT_ID])
            print(f"\"{converted_data['text']}\" Created at: {converted_data['created_at']}")

def read_next():
      global CURRENT_ID
      if (CURRENT_ID + 1) > (len(TWEETS) - 1):
            print("LIMIT REACHED! NO MORE TWEETS BELOW\n")
      else:
            CURRENT_ID += 1
            converted_data = json.loads(TWEETS[CURRENT_ID])
            print(f"\"{converted_data['text']}\" Created at: {converted_data['created_at']}")

def save_all():
      with open("tweetdhead300000.json", 'w') as file:
            for line in TWEETS:
                  file.write(line)
                  
def main():
      try:
            file = open ("tweetdhead300000.json", 'r')
      except:
            print ("Something went wrong while opening file. Make sure it exists!")
      else:
            global TWEETS
            TWEETS = [line for _, line in enumerate(file) ]
            file.close()
            while(True):
                  print_menu()
                  choice = input()
                  if(check_choice(choice)):
                        if choice == 'c':
                              create_tweet()
                        elif choice[0] == 'r':
                              read_with_id(int(choice[1:]) - 1)
                        elif choice[0] == 'u':
                              update_tweet(int(choice[1:]) - 1)
                        elif choice == 'd':
                              deleted_tweets()
                        elif choice == '$':
                              print_last()
                        elif choice == '-':
                              read_prev()
                        elif choice == '+':
                              read_next()
                        elif choice == '=':
                              print (CURRENT_ID + 1)
                        elif choice == 'q':
                              print ("Program closed without saving")
                              exit()
                        elif choice == 'w':
                              save_all()
                        elif choice == 'x':
                              save_all()
                              print ("Program closed with saving")
                              exit()
                  else:
                        print ("Invalid choice, please try again!")

if __name__ == "__main__":
      sys.exit(main())