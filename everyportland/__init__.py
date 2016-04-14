import tweepy # for tweeting
from .secrets import consumer_secret, consumer_key, access_token, access_token_secret
import random
import inflect
import logging
import os.path as path

PATH = path.dirname(__file__)

def random_modifier():
  # open text file
  text_file = open(path.join(PATH, 'modifiers.txt'), 'r')
  text_string = text_file.read()
  return random.choice(text_string.split('\n'))

def get_next_chunk():
  # open text file
  text_file = open(path.join(PATH, 'book.txt'), 'r+')
  text_string = text_file.read()
  chunk = text_string.split('\n')[0]

  # delete what we just tweeted from the text file
  text_file.seek(0)
  text_file.write(text_string[len(chunk) + 1:len(text_string)])
  text_file.truncate()
  text_file.close()

  p = inflect.engine()
  return p.plural(chunk)

def portland_word():
  return random_modifier() + ' ' + get_next_chunk()

def tweet(message):
  logger = logging.getLogger('everyportland')
  logger.setLevel(logging.DEBUG)
  fh = logging.FileHandler('/opt/bots/everyportland/portland_tweets.log')
  fh.setLevel(logging.DEBUG)
  logger.addHandler(fh)
  logger.debug('getting ready to tweet')

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)
  api = tweepy.API(auth)
  auth.secure = True
  logger.debug("Posting message {}".format(message))
  api.update_status(status=message)

if __name__ == '__main__':
  tweet(portland_word())
