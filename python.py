import json
from datetime import datetime

tweetMemory = []
currentId = 0

mia paparia

def printMenu():
    print('\nPlease, choose what you would like to do:\n')
    print('c: Create tweet by giving its “text”(derive “created at” by system date time).'
          '\n   Every created tweet is appended at the end of the rest (in memory and, if saved, in the twitter file).'
          '\n   Sets current tweet ID to be the created one.\n')
    print('r<number>: Read the tweet at line/with ID <number>. Sets current tweet ID to be the read one\n')
    print('u<number>: Update the tweet at line/with ID <number>, by giving its new “text” (derive “created at” by system date time).'
          '\n           Sets current tweet ID to be the updated one.\n')
    print('d: Delete current tweet (Hint: adjust tweet IDs when needed).\n')
    print('$: Read the last tweet in the file. Sets current tweet ID to be the last one.\n')
    print('-: Read one tweet up from the current tweet. Updates current tweet ID accordingly.\n')
    print('+: Read one tweet down from your current tweet. Updates current tweet ID accordingly.\n')
    print('=: Print current tweet ID.\n')
    print('q: Quit without save.\n')
    print('w: (Over)write file to disk.\n')
    print('x: Exit and save.\n')

def checkChoice(choice):
      correctChoices = ['c','r','u','d','$','-','+','=','q','w','x']
      for i in range(0, len(correctChoices)):
            if(choice[0] == correctChoices[i]):
                  return True
      return False

def createTweet():
      print("Please, input the text of the tweet:")
      tweetText = input()
      print("Now, input tweet's ID:")
      tweetId = input()
      time = datetime.now()
      creationTime = time.strftime("%a %b %d %H:%M:%S +0000 %Y")
      
      

global file
try:
      file = open("tweetdhead300000.json", 'r')
except:
      print("Something went wrong while opening file. Make sure it exists!")
else:
      lines = file.readlines()
      while(True):
            printMenu()
            choice = input()
            if(checkChoice(choice)):
                  match(choice):
                        case('c'):
                              tweetMemory.append(input())
                        case('x'):
                              for i in tweetMemory:
                                    print(i)
                        case  _:
                              print("oof\n")