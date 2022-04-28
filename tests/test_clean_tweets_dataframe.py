import unittest
import pandas as pd

from extract_dataframe import read_json
from clean_tweets_dataframe import twt_data
from clean_tweets_dataframe import Clean_Tweets

columns = ['created_at', 'source', 'original_text','clean_text', 'sentiment','polarity','subjectivity', 'lang', 'favorite_count', 'retweet_count', 
    'original_author', 'screen_count', 'followers_count','friends_count','possibly_sensitive', 'hashtags', 'user_mentions', 'place', 'place_coord_boundaries']

class TestClean_Tweets(unittest.TestCase):

    def setUp(self) -> pd.DataFrame:
        self.df = Clean_Tweets(twt_data)

    def test_drop_unwanted_column(self):
        self.assertEqual(self.df.drop_unwanted_column(self.df), 0.1)

