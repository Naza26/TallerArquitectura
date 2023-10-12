import unittest

from business.model.article import Article
from magazine_system import MagazineSystem
from tests.magazine_catalog import MagazineCatalog


class MagazineSystemTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(MagazineSystemTests, self).__init__(*args, **kwargs)
        self.catalog = MagazineCatalog()

    def test01_system_can_see_list_of_articles(self):
        system = MagazineSystem(self.catalog.empty_magazine())

        articles = system.list_of_articles()

        self.assertEqual(len(articles), 0)

    def test02_system_can_publish_an_article(self):
        system = MagazineSystem(self.catalog.empty_magazine())

        for article_to_serialize in system.unserialized_sample_articles():
            article_to_publish = system.create_serialized_article(article_to_serialize)
            system.publish(article_to_publish)

        articles = system.list_of_articles()
        self.assertEqual(len(articles), 3)

    def test03_system_can_publish_articles_with_valid_titles(self):
        system = MagazineSystem(self.catalog.empty_magazine())

        for article_to_serialize in system.unserialized_sample_articles():
            article_to_publish = system.create_serialized_article(article_to_serialize)
            system.publish(article_to_publish)

        published_article = system.list_of_articles()[0]
        published_article = list(published_article.values())[0]
        self.assertTrue(published_article.has_title(system.unserialized_sample_articles()[0]["title"]))

    def test04_system_can_publish_articles_with_valid_texts(self):
        system = MagazineSystem(self.catalog.empty_magazine())

        for article_to_serialize in system.unserialized_sample_articles():
            article_to_publish = system.create_serialized_article(article_to_serialize)
            system.publish(article_to_publish)

        published_article = system.list_of_articles()[0]
        published_article = list(published_article.values())[0]
        self.assertTrue(published_article.has_text(system.unserialized_sample_articles()[0]["text"]))

    def test05_system_cannot_publish_articles_with_too_short_titles(self):
        system = MagazineSystem(self.catalog.empty_magazine())
        article_to_serialize = {"title": "x" * (Article.MINIMUM_TITLE_LENGTH - 1),
                                "text": "x" * Article.MINIMUM_TEXT_LENGTH}
        invalid_article_to_publish = system.create_serialized_article(article_to_serialize)

        with self.assertRaises(Exception) as result:
            system.publish(invalid_article_to_publish)

        error_message = f"Title must be within {Article.MINIMUM_TITLE_LENGTH}-{Article.MAXIMUM_TITLE_LENGTH}" \
                        f" characters long"
        self.assertEqual(error_message, str(result.exception))

    def test06_system_cannot_publish_articles_with_too_short_texts(self):
        system = MagazineSystem(self.catalog.empty_magazine())
        article_to_serialize = {"title": "x" * Article.MINIMUM_TITLE_LENGTH,
                                "text": "x" * (Article.MINIMUM_TEXT_LENGTH - 1)}
        invalid_article_to_publish = system.create_serialized_article(article_to_serialize)

        with self.assertRaises(Exception) as result:
            system.publish(invalid_article_to_publish)

        error_message = f"Text must be within {Article.MINIMUM_TEXT_LENGTH}-{Article.MAXIMUM_TEXT_LENGTH}" \
                        f" characters long"
        self.assertEqual(error_message, str(result.exception))

    def test07_system_cannot_publish_articles_with_too_long_titles(self):
        system = MagazineSystem(self.catalog.empty_magazine())
        article_to_serialize = {"title": "x" * (Article.MAXIMUM_TITLE_LENGTH + 1),
                                "text": "x" * Article.MINIMUM_TEXT_LENGTH}
        invalid_article_to_publish = system.create_serialized_article(article_to_serialize)

        with self.assertRaises(Exception) as result:
            system.publish(invalid_article_to_publish)

        error_message = f"Title must be within {Article.MINIMUM_TITLE_LENGTH}-{Article.MAXIMUM_TITLE_LENGTH}" \
                        f" characters long"
        self.assertEqual(error_message, str(result.exception))

    def test08_system_cannot_publish_articles_with_too_long_texts(self):
        system = MagazineSystem(self.catalog.empty_magazine())
        article_to_serialize = {"title": "x" * Article.MINIMUM_TITLE_LENGTH,
                                "text": "x" * (Article.MAXIMUM_TEXT_LENGTH + 1)}
        invalid_article_to_publish = system.create_serialized_article(article_to_serialize)

        with self.assertRaises(Exception) as result:
            system.publish(invalid_article_to_publish)

        error_message = f"Text must be within {Article.MINIMUM_TEXT_LENGTH}-{Article.MAXIMUM_TEXT_LENGTH}" \
                        f" characters long"
        self.assertEqual(error_message, str(result.exception))

    def test09_system_cannot_be_corrupted_from_outside(self):
        system = MagazineSystem(self.catalog.empty_magazine())
        articles = system.list_of_articles()

        articles.append("xxx")

        articles = system.list_of_articles()
        self.assertEqual(len(articles), 0)

    def test10_system_can_obtain_summarized_articles_list(self):
        system = MagazineSystem(self.catalog.magazine_with_articles())
        articles_to_publish = [list(article.values())[0] for article in system.list_of_articles()]

        summarized_articles = system.list_of_summarized_articles()

        expected_articles_list = self.catalog.summarized_article_list(articles_to_publish)
        self.assertEqual(summarized_articles, expected_articles_list)

    def test11_system_can_obtain_article_by_title(self):
        system = MagazineSystem(self.catalog.magazine_with_articles())
        title_of_article_to_obtain = "Title A"

        obtained_article = system.article_by_id(1)

        self.assertTrue(obtained_article.has_title(title_of_article_to_obtain))

    def test12_system_cannot_obtain_article_if_title_is_not_found(self):
        system = MagazineSystem(self.catalog.empty_magazine())
        articles_to_serialize = system.unserialized_sample_articles()
        articles_to_publish = self.articles_to_publish(system, articles_to_serialize)
        self.publish_articles(system, articles_to_publish)

        obtained_article = system.article_by_id(4)

        self.assertTrue(obtained_article is None)

    def test13_system_can_unequivocally_obtain_article(self):
        system = MagazineSystem(self.catalog.empty_magazine())
        articles_to_serialize = system.unserialized_sample_articles()
        articles_to_publish = self.articles_to_publish(system, articles_to_serialize)
        self.publish_articles(system, articles_to_publish)
        system.publish(system.create_serialized_article(
            {"title": "Title A", "text": "a" * Article.MINIMUM_TEXT_LENGTH})
        )
        title_of_article_to_obtain = "Title A"

        obtained_article = system.article_by_id(1)
        self.assertTrue(obtained_article.has_title(title_of_article_to_obtain))
        self.assertTrue(obtained_article.has_text("x" * Article.MINIMUM_TEXT_LENGTH))

    def articles_to_publish(self, system, articles_to_serialize):
        articles_to_publish = []
        for article in articles_to_serialize:
            articles_to_publish.append(system.create_serialized_article(article))
        return articles_to_publish

    def publish_articles(self, system, articles_to_publish):
        [system.publish(article) for article in articles_to_publish]


if __name__ == '__main__':
    unittest.main()
