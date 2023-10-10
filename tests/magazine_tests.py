import unittest

from business.model.article import Article
from tests.magazine_catalog import MagazineCatalog


class MagazineTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(MagazineTests, self).__init__(*args, **kwargs)
        self.catalog = MagazineCatalog()

    def test_01_list_of_articles_can_be_seen(self):
        magazine = self.catalog.empty_magazine()

        articles = magazine.list_of_articles()

        self.assertEqual(len(articles), 0)

    def test_02_an_article_can_be_published(self):
        magazine = self.catalog.empty_magazine()
        standard_article_text = self.catalog.standard_article_text()
        article = self.catalog.create_article(text=standard_article_text)

        magazine.publish(article)

        articles = magazine.list_of_articles()
        self.assertEqual(len(articles), 1)

    def test_03_when_published_an_article_has_a_title(self):
        magazine = self.catalog.empty_magazine()
        standard_article_title = self.catalog.standard_article_title()
        article = self.catalog.create_article(title=standard_article_title)

        magazine.publish(article)

        an_article = self.catalog.sample_article_from(magazine.list_of_articles())
        an_article = list(an_article.values())[0]
        self._assert_proper_article_is_contained_in_magazine(an_article.has_title, an_article.has_title,
                                                             standard_article_title)

    def test_04_when_published_an_article_has_a_text(self):
        magazine = self.catalog.empty_magazine()
        standard_article_text = self.catalog.standard_article_text()
        article = self.catalog.create_article(text=standard_article_text)

        magazine.publish(article)

        an_article = self.catalog.sample_article_from(magazine.list_of_articles())
        an_article = list(an_article.values())[0]
        self._assert_proper_article_is_contained_in_magazine(an_article.has_text, an_article.has_text,
                                                             standard_article_text)

    def test_05_title_of_article_cannot_be_too_short(self):
        magazine = self.catalog.empty_magazine()
        short_article_title = self.catalog.short_article_title()
        invalid_article = self.catalog.create_article(title=short_article_title)

        result = self._assert_magazine_cannot_publish_invalid_article(invalid_article, magazine)

        error_message = f"Title must be within {Article.MINIMUM_TITLE_LENGTH}-{Article.MAXIMUM_TITLE_LENGTH}" \
                        f" characters long"
        self.assertEqual(error_message, str(result.exception))

    def test_06_title_of_article_cannot_be_too_long(self):
        magazine = self.catalog.empty_magazine()
        long_article_title = self.catalog.long_article_title()
        invalid_article = self.catalog.create_article(title=long_article_title)

        result = self._assert_magazine_cannot_publish_invalid_article(invalid_article, magazine)

        error_message = f"Title must be within {Article.MINIMUM_TITLE_LENGTH}-{Article.MAXIMUM_TITLE_LENGTH}" \
                        f" characters long"
        self.assertEqual(error_message, str(result.exception))

    def test_07_text_of_article_cannot_be_too_short(self):
        magazine = self.catalog.empty_magazine()
        short_article_text = self.catalog.short_article_text()
        invalid_article = self.catalog.create_article(text=short_article_text)

        result = self._assert_magazine_cannot_publish_invalid_article(invalid_article, magazine)

        error_message = f"Text must be within {Article.MINIMUM_TEXT_LENGTH}-{Article.MAXIMUM_TEXT_LENGTH}" \
                        f" characters long"
        self.assertEqual(error_message, str(result.exception))

    def test_08_text_of_article_cannot_be_too_long(self):
        magazine = self.catalog.empty_magazine()
        long_article_text = self.catalog.long_article_text()
        invalid_article = self.catalog.create_article(text=long_article_text)

        result = self._assert_magazine_cannot_publish_invalid_article(invalid_article, magazine)

        error_message = f"Text must be within {Article.MINIMUM_TEXT_LENGTH}-{Article.MAXIMUM_TEXT_LENGTH}" \
                        f" characters long"
        self.assertEqual(error_message, str(result.exception))

    def _assert_magazine_cannot_publish_invalid_article(self, article, magazine):
        with self.assertRaises(Exception) as result:
            magazine.publish(article)
        return result

    def _assert_proper_article_is_contained_in_magazine(self, has_invalid_content, has_valid_content, content):
        self.assertTrue(has_valid_content(content))
        self.assertFalse(has_invalid_content("xxx"))


if __name__ == '__main__':
    unittest.main()
