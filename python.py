import json
import os
from datetime import datetime

currentId = 0

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
      for i in correctChoices:
            if(i == choice):
                  return True
      return False

def createTweet():
      tweetText = input("Please, input the text of the tweet:")
      time = datetime.now()
      creationTime = time.strftime("%a %b %d %H:%M:%S +0000 %Y")
      finishedTweet = dict({"text":tweetText,"created_at":creationTime})
      with open("C:\\Users\\giorg\\Documents\\Python Projects\\tweetdhead300000.json", 'a+') as file:
            for lastId, _ in enumerate(file):
                  pass
            currentId = lastId
            file.write(json.dumps(finishedTweet) + "\n")
            print(finishedTweet)

def readWithId(number):
      with open("C:\\Users\\giorg\\Documents\\Python Projects\\tweetdhead300000.json", 'r') as file:
            for i, line in enumerate(file):
                  if i == number:
                        break
            data = json.loads(line)
            print("\"" +data['text'] + "\" Created at: " + data['created_at'])

def printLast():
      with open("C:\\Users\\giorg\\Documents\\Python Projects\\tweetdhead300000.json", 'r') as file:
            for lastId, line in enumerate(file):
                pass
            currentId = lastId
            data = json.loads(line)
            print("\"" +data['text'] + "\" Created at: " + data['created_at'])

def readPrev():
      if (currentId-1) < 0:
            print("LIMIT REACHED! NO MORE TWEETS ABOVE\n")
      else:
            currentId =- 1
            with open("C:\\Users\\giorg\\Documents\\Python Projects\\tweetdhead300000.json", 'r') as file:
                  for i, line in enumerate(file):
                        if i == currentId:
                              break
                  data = json.loads(line)
                  print("\"" +data['text'] + "\" Created at: " + data['created_at'])

def readNext():
      if (currentId+1) > 0:
            print("LIMIT REACHED! NO MORE TWEETS BELOW\n")
      else:
            with open("C:\\Users\\giorg\\Documents\\Python Projects\\tweetdhead300000.json", 'r') as file:
                  currentId =+ 1
                  for i, line in enumerate(file):
                        if i == currentId:
                              break
                  data = json.loads(line)
                  print("\"" +data['text'] + "\" Created at: " + data['created_at']) 

def printCur():
      print(currentId)
              

try:
      file = open("C:\\Users\\giorg\\Documents\\Python Projects\\tweetdhead300000.json", 'r+')
except:
      print("Something went wrong while opening file. Make sure it exists!")
else:
      file.close()
      while(True):
            printMenu()
            choice = input()
            if(checkChoice(choice[0])):
                  match(choice[0]):
                        case('c'):
                              createTweet()
                        case('r'):
                              readWithId(int(choice[1:]))
                        case('x'):
                              pass
                        case('$'):
                              printLast()
                        case('-'):
                              readPrev()
                        case('+'):
                              readNext()
                        case('='):
                              printCur()
                        case  _:
                              print("oof\n")