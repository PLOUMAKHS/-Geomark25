import json
import os
from datetime import datetime

tweets = []
currentId = 0

def printMenu():
    print('\nPlease, choose what you would like to do:\n')
    print('c: Create tweet. Sets current tweet ID to be the created one.\n')
    print('r<number>: Read the tweet at line/with ID <number>. Sets current tweet ID to be the read one\n')
    print('u<number>: Update the tweet at line/with ID <number>. Sets current tweet ID to be the updated one.\n')
    print('d: Delete current tweet.\n')
    print('$: Read the last tweet in the file. Sets current tweet ID to be the last one.\n')
    print('-: Read one tweet up from the current tweet.\n')
    print('+: Read one tweet down from your current tweet.\n')
    print('=: Print current tweet ID.\n')
    print('q: Quit without save.\n')
    print('w: (Over)write file to disk.\n')
    print('x: Exit and save.\n')

def checkChoice(choice):
      correctChoices = ['c','d','$','-','+','=','q','w','x']
      correctChoices1 = ['r','u']
      for i in correctChoices:
            if(i == choice):
                  return True
      for i in correctChoices1:
            if(i == choice[0]):
                  return True
      return False

def createTweet():
      tweetText = input("Please, input the text of the tweet:")
      time = datetime.now()
      creationTime = time.strftime("%a %b %d %H:%M:%S +0000 %Y")
      finishedTweet = {"text":tweetText,"created_at":creationTime}
      tweets.append(finishedTweet)
      global currentId
      currentId = len(tweets)

def readWithId(number):
      if(number >= 0 and number < len(tweets)):
            global currentId
            currentId = number
            data = tweets[currentId]
            print(str("\"" +data['text'] + "\" Created at: " + data['created_at']))
      else:
            print("Invalid ID. Try again.\n")

def updateTweet(number):
      if(number >= 0 and number < len(tweets)):
            tweetText = input("Please, input the text of the tweet:")
            time = datetime.now()
            creationTime = time.strftime("%a %b %d %H:%M:%S +0000 %Y")
            finishedTweet = {"text":tweetText,"created_at":creationTime}
            tweets[number] = finishedTweet
            global currentId
            currentId = number
      else:
            print("Invalid ID. Try again.\n")

def deleteTweet():
      global currentId
      del tweets[currentId]
      if currentId >= len(tweets):
            currentId -= 1

def printLast():
      global currentId
      currentId = (len(tweets) - 1)
      data = tweets[-1]
      print(str("\"" +data['text'] + "\" Created at: " + data['created_at']))

def readPrev():
      global currentId
      if (currentId-1) < 0:
            print("LIMIT REACHED! NO MORE TWEETS ABOVE\n")
      else:
            currentId -= 1
            data = tweets[currentId]
            print(str("\"" +data['text'] + "\" Created at: " + data['created_at']))

def readNext():
      global currentId
      if (currentId + 1) > (len(tweets) - 1):
            print("LIMIT REACHED! NO MORE TWEETS BELOW\n")
      else:
            currentId += 1
            data = tweets[currentId]
            print(str("\"" +data['text'] + "\" Created at: " + data['created_at'])) 

def saveAll():
      with open("tweetdhead300000.json", 'w') as file:
            for line in tweets:
                  convert = json.dumps(line)
                  file.write(convert + "\n")
                  

try:
      file = open("tweetdhead300000.json", 'r')
except:
      print("Something went wrong while opening file. Make sure it exists!")
else:
      for i, line in enumerate(file):
            tweets.append(json.loads(line))
      file.close()
      while(True):
            printMenu()
            choice = input()
            if(checkChoice(choice)):
                  match(choice[0]):
                        case('c'):
                              createTweet()
                        case('r'):
                              readWithId(int(choice[1:]) - 1)
                        case('u'):
                              updateTweet(int(choice[1:]) - 1)
                        case('d'):
                              deleteTweet()
                        case('$'):
                              printLast()
                        case('-'):
                              readPrev()
                        case('+'):
                              readNext()
                        case('='):
                              print(currentId)
                        case('q'):
                              print("Program closed without saving")
                              exit()
                        case('w'):
                              saveAll()
                        case('x'):
                              saveAll()
                              print("Program closed with saving")
                              exit()
            else:
                  print("Invalid choice, please try again!")