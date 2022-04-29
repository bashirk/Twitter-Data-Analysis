import unittest
import pandas as pd
import sys, os
 
sys.path.append(os.path.abspath(os.path.join('../..')))

from extract_dataframe import read_json
from clean_tweets_dataframe import twt_data
from clean_tweets_dataframe import Clean_Tweets

tweets_list = read_json("data/Economic_Twitter_Data.json")


class TestClean_Tweets(unittest.TestCase):

    def setUp(self) -> pd.DataFrame:
        self.df = tweets_list

        self.df = Clean_Tweets(self.df)

    def test_drop_unwanted_column(self):
        self.assertEqual(len(self.df.columns),len(self.df_cleanser.drop_unwanted_column(self.df).columns))

