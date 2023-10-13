import unittest
from tests.magazine_catalog import MagazineCatalog


class MagazineTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(MagazineTests, self).__init__(*args, **kwargs)
        self.catalog = MagazineCatalog()

    def setUp(self):
        self.magazine = self.catalog.empty_magazine()

    def test_01_list_of_articles_can_be_seen(self):
        articles = self.magazine.list_of_articles()

        self.assertEqual(len(articles), 0)

    def test_02_an_article_can_be_published(self):
        article = self.catalog.create_article()

        self.magazine.publish(article)

        articles = self.magazine.list_of_articles()
        self.assertEqual(len(articles), 1)

    def test_03_when_published_an_article_has_a_title(self):
        article = self.catalog.create_article()

        self.magazine.publish(article)

        an_article = list(self.catalog.sample_article_from(self.magazine.list_of_articles()).values())[0]
        self._assert_proper_article_is_contained_in_magazine(an_article.contains_title_named, an_article.contains_title_named,
                                                             self.catalog.standard_article_title())

    def test_04_when_published_an_article_has_a_text(self):
        article = self.catalog.create_article()

        self.magazine.publish(article)

        an_article = list(self.catalog.sample_article_from(self.magazine.list_of_articles()).values())[0]
        self._assert_proper_article_is_contained_in_magazine(an_article.contains_text_named,
                                                             an_article.contains_text_named,
                                                             self.catalog.standard_article_text())

    def test_05_title_of_article_cannot_be_too_short(self):
        invalid_article = self.catalog.create_article(title=self.catalog.short_article_title())

        result = self._assert_magazine_cannot_publish_invalid_article(invalid_article, self.magazine)

        self.assertEqual(self.catalog.title_length_error(), str(result.exception))

    def test_06_title_of_article_cannot_be_too_long(self):
        invalid_article = self.catalog.create_article(title=self.catalog.long_article_title())

        result = self._assert_magazine_cannot_publish_invalid_article(invalid_article, self.magazine)

        self.assertEqual(self.catalog.title_length_error(), str(result.exception))

    def test_07_text_of_article_cannot_be_too_short(self):
        invalid_article = self.catalog.create_article(text=self.catalog.short_article_text())

        result = self._assert_magazine_cannot_publish_invalid_article(invalid_article, self.magazine)

        self.assertEqual(self.catalog.text_length_error(), str(result.exception))

    def test_08_text_of_article_cannot_be_too_long(self):
        invalid_article = self.catalog.create_article(text=self.catalog.long_article_text())

        result = self._assert_magazine_cannot_publish_invalid_article(invalid_article, self.magazine)

        self.assertEqual(self.catalog.text_length_error(), str(result.exception))

    def _assert_magazine_cannot_publish_invalid_article(self, article, magazine):
        with self.assertRaises(Exception) as result:
            magazine.publish(article)
        return result

    def _assert_proper_article_is_contained_in_magazine(self, has_invalid_content, has_valid_content, content):
        self.assertTrue(has_valid_content(content))
        self.assertFalse(has_invalid_content("xxx"))


if __name__ == '__main__':
    unittest.main()
