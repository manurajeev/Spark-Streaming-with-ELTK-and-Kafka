from kafka import KafkaProducer
from textblob import TextBlob
import tweepy
import configparser
from tweepy import StreamingClient, StreamRule
import time

config = configparser.ConfigParser(interpolation=None)
config.read('config.ini')
bearer_token = config['args']['bearer_token']
search_terms = config['args']['search_term']
topic_name = config['args']['topic']

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def check_polarity(tweet):
    score = TextBlob(tweet).sentiment.polarity
    if score < 0:
        return "Negative"
    elif score == 0:
        return "Neutral"
    else:
        return "Positive"

class TweetPrinterV2(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(f"{tweet.text}")
        print("-"*30)
        transformer_sentiment = check_polarity(tweet.text)
        producer.send(topic_name, transformer_sentiment.encode('utf-8'))
        time.sleep(1)
    
    def on_connection_error(self):
        print("Connection Error")
        return super().on_connection_error()

printer = TweetPrinterV2(bearer_token)
existing_rules = printer.get_rules()
printer.delete_rules(existing_rules.data)
for term in search_terms:
    printer.add_rules(StreamRule(value=term))
printer.filter()