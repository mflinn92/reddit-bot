import unittest
from src.bot.api_read import subreddit 

class Test_api_call(unittest.TestCase):
    def test_retrieve_titles(self):
        test_result = subreddit.hot(limit=5)
        res = [result.title for result in test_result]
        self.assertEqual(len(res), 5)
        for title in res:
            self.assertEqual(isinstance(title, str), True)