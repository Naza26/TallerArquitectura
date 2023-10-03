import unittest


class Magazine:

    def __init__(self):
        self._articles = []

    def list_of_articles(self):
        return self._articles

    def publish(self, article):
        if len(article.title()) < 2:
            raise Exception("Title cannot have less than two characters")
        if len(article.title()) > 50:
            raise Exception("Title cannot have more than fifty characters")
        if len(article.text()) < 1800:
            raise Exception("Text cannot have less than 1800 characters")
        if len(article.text()) > 5200:
            raise Exception("Text cannot have more than 5200 characters")
        self._articles.append(article)


class Article:
    def __init__(self, title, text):  # You will be valid and complete one day...
        self._title = title
        self._text = text

    def has_title(self, title):
        return self._title == title

    def has_text(self, text):
        return self._text == text

    def title(self):
        return self._title

    def text(self):
        return self._text


class MagazineTests(unittest.TestCase):
    def test_01_list_of_articles_can_be_seen(self):
        magazine = Magazine()

        articles = magazine.list_of_articles()

        self.assertEqual(len(articles), 0)

    def test_02_an_article_can_be_published(self):
        magazine = Magazine()
        article_text = "a" * 1800
        article = Article("article's title", article_text)

        magazine.publish(article)
        articles = magazine.list_of_articles()

        self.assertEqual(len(articles), 1)

    def test_03_when_published_an_article_has_a_title(self):
        magazine = Magazine()
        article_text = "a" * 1800
        article = Article("article's title", article_text)

        magazine.publish(article)

        articles = magazine.list_of_articles()
        an_article = articles[0]
        self.assertTrue(an_article.has_title("article's title"))
        self.assertFalse(an_article.has_title("xxx"))

    def test_04_when_published_an_article_has_a_text(self):
        magazine = Magazine()
        article_text = "a" * 1800
        article = Article("article's title", article_text)

        magazine.publish(article)

        articles = magazine.list_of_articles()
        an_article = articles[0]
        self.assertTrue(an_article.has_text(article_text))
        self.assertFalse(an_article.has_text("xxx"))

    def test_05_title_of_article_cannot_be_too_short(self):
        magazine = Magazine()
        article = Article("a", "article's text")

        with self.assertRaises(Exception) as result:
            magazine.publish(article)

        self.assertEqual("Title cannot have less than two characters", str(result.exception))

    def test_06_title_of_article_cannot_be_too_long(self):
        magazine = Magazine()
        article_title = "a" * 51
        article = Article(article_title, "article's text")

        with self.assertRaises(Exception) as result:
            magazine.publish(article)

        self.assertEqual("Title cannot have more than fifty characters", str(result.exception))

    def test_07_text_of_article_cannot_be_too_short(self):
        magazine = Magazine()
        article_text = "a" * 1799
        article = Article("article's title", article_text)

        with self.assertRaises(Exception) as result:
            magazine.publish(article)

        self.assertEqual("Text cannot have less than 1800 characters", str(result.exception))

    def test_08_text_of_article_cannot_be_too_long(self):
        magazine = Magazine()
        article_text = "a" * 5201
        article = Article("article's title", article_text)

        with self.assertRaises(Exception) as result:
            magazine.publish(article)

        self.assertEqual("Text cannot have more than 5200 characters", str(result.exception))



if __name__ == '__main__':
    unittest.main()