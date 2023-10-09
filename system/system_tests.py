import unittest

from business.article import Article
from system import System


class MyTestCase(unittest.TestCase):
    def test01(self):
        system = System()

        articles = system.list_of_articles()

        self.assertEqual(len(articles), 0)

    def test02(self):
        system = System()

        system.publish({"title": "x" * Article.MINIMUM_TITLE_LENGTH, "text": "x" * Article.MINIMUM_TEXT_LENGTH})

        articles = system.list_of_articles()
        self.assertEqual(len(articles), 1)

    def test03(self):
        system = System()
        article_to_publish = {"title": "x" * Article.MINIMUM_TITLE_LENGTH, "text": "x" * Article.MINIMUM_TEXT_LENGTH}

        system.publish(article_to_publish)

        published_article = system.list_of_articles()[0]
        self.assertTrue(published_article["title"] == article_to_publish["title"])
        self.assertFalse(published_article["title"] == "xxx")



if __name__ == '__main__':
    unittest.main()
