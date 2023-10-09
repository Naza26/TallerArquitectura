import unittest


class MyTestCase(unittest.TestCase):
    def test01(self):
        magazine = {}

        articles = system.list_of_articles()

        self.assertEqual(len(articles), 0)


if __name__ == '__main__':
    unittest.main()
