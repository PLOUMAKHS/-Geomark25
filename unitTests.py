import unittest
from datetime import datetime
import json

#Assert created tweet is type 'dict'
class TestMain(unittest.TestCase):

    def setUp(self):
        global tweets
        tweets = []
        global file
        file = open("testJson.json", 'r')
        for i, line in enumerate(file):
            tweets.append(json.loads(line))
    
    def test_create_tweet(self):
        text = "Today we are going to finish the python project" 
        time = datetime.now()
        creationTime = time.strftime("%a %b %d %H:%M:%S +0000 %Y")
        finishedTweet = {"text":text,"created_at":creationTime}
        self.assertEqual(str(type(finishedTweet)),"<class 'dict'>", "Not dictionary!")

    def test_print_last(self):
        data = tweets[-1]
        self.assertEqual(data['text'], "test6", "Did not read last text!")

    def test_print_last_while_deleting_last(self):
        del tweets[-1]
        data = tweets[-1]
        self.assertEqual(data['text'], "test5", "Did not read last text!")

    def test_print_last_while_adding_tweet(self):
        tweetText = "test7"
        time = datetime.now()
        creationTime = time.strftime("%a %b %d %H:%M:%S +0000 %Y")
        finishedTweet = {"text":tweetText,"created_at":creationTime}
        tweets.append(finishedTweet)
        data = tweets[-1]
        self.assertEqual(data['text'], "test7", "Did not read last text!")

    def test_read_tweet_with_id(self):
        userInput = 1 
        currentId = userInput - 1 
        data = tweets[currentId]
        self.assertEqual(data['text'],"test1" ,"Did not read the text ")

    def test_read_tweet_with_id_while_deleted_text(self):
        del tweets [0]
        userInput = 1 
        currentId = userInput - 1 
        data = tweets[currentId]
        self.assertEqual(data['text'],"test2" ,"Did not read the text ")

    def test_read_tweet_with_id_invalid_input(self):
        userInput = 8
        number = userInput -1
        self.assertNotEqual((number >= 0 and number < len(tweets)),1,"OUPS")
        userInput = 0
        number = userInput -1
        self.assertNotEqual((number >= 0 and number < len(tweets)),1,"OUPS")



    def test_update_tweet(self):
        userInput =1
        currentid = userInput -1
        time = datetime.now()
        text = "Today we are going to finish the python project"
        creationTime = time.strftime("%a %b %d %H:%M:%S +0000 %Y")
        finishedTweet = {"text":text,"created_at":creationTime}
        self.assertEqual(str(type(finishedTweet)),"<class 'dict'>", "Not dictionary!")

    def test_update_tweet_invalid_input(self):
        userInput = 7
        number = userInput -1
        self.assertNotEqual((number >= 0 and number < len(tweets)),1,"OUPS")
        userInput = 0
        number = userInput -1
        self.assertNotEqual((number >= 0 and number < len(tweets)),1,"OUPS")\

    def test_deleted_tweet(self):
        del tweets[0]
        data = tweets[0]
        userInput = 1
        number = userInput -1
        self.assertEqual(data['text'], "test2", "Did not read last text!")



    def tearDown(self):
        file.close()


unittest.main()
