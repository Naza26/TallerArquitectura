import unittest

from business.model.article import Article
from magazine_system import MagazineSystem


class MagazineSystemTests(unittest.TestCase):
    def test01_system_can_see_list_of_articles(self):
        system = MagazineSystem()

        articles = system.list_of_articles()

        self.assertEqual(len(articles), 0)

    def test02_system_can_publish_an_article(self):
        system = MagazineSystem()
        article_to_serialize = {"title": "x" * Article.MINIMUM_TITLE_LENGTH, "text": "x" * Article.MINIMUM_TEXT_LENGTH}
        article_to_publish = system.create_serialized_article(article_to_serialize)

        system.publish(article_to_publish)

        articles = system.list_of_articles()
        self.assertEqual(len(articles), 1)

    def test03_system_can_publish_articles_with_valid_titles(self):
        system = MagazineSystem()
        article_to_serialize = {"title": "x" * Article.MINIMUM_TITLE_LENGTH, "text": "x" * Article.MINIMUM_TEXT_LENGTH}
        article_to_publish = system.create_serialized_article(article_to_serialize)

        system.publish(article_to_publish)

        published_article = system.list_of_articles()[0]
        self.assertTrue(published_article.has_title(article_to_serialize["title"]))
        self.assertFalse(published_article.has_title("xxx"))  # Delete me

    def test04_system_can_publish_articles_with_valid_texts(self):
        system = MagazineSystem()
        article_to_serialize = {"title": "x" * Article.MINIMUM_TITLE_LENGTH, "text": "x" * Article.MINIMUM_TEXT_LENGTH}
        article_to_publish = system.create_serialized_article(article_to_serialize)

        system.publish(article_to_publish)

        published_article = system.list_of_articles()[0]
        self.assertTrue(published_article.has_text(article_to_serialize["text"]))
        self.assertFalse(published_article.has_text("xxx"))

    def test05_system_cannot_publish_articles_with_too_short_titles(self):
        system = MagazineSystem()
        article_to_serialize = {"title": "x" * (Article.MINIMUM_TITLE_LENGTH - 1),
                                "text": "x" * Article.MINIMUM_TEXT_LENGTH}
        invalid_article_to_publish = system.create_serialized_article(article_to_serialize)

        with self.assertRaises(Exception) as result:
            system.publish(invalid_article_to_publish)

        error_message = f"Title must be within {Article.MINIMUM_TITLE_LENGTH}-{Article.MAXIMUM_TITLE_LENGTH}" \
                        f" characters long"
        self.assertEqual(error_message, str(result.exception))

    def test06_system_cannot_publish_articles_with_too_short_texts(self):
        system = MagazineSystem()
        article_to_serialize = {"title": "x" * Article.MINIMUM_TITLE_LENGTH,
                                "text": "x" * (Article.MINIMUM_TEXT_LENGTH - 1)}
        invalid_article_to_publish = system.create_serialized_article(article_to_serialize)

        with self.assertRaises(Exception) as result:
            system.publish(invalid_article_to_publish)

        error_message = f"Text must be within {Article.MINIMUM_TEXT_LENGTH}-{Article.MAXIMUM_TEXT_LENGTH}" \
                        f" characters long"
        self.assertEqual(error_message, str(result.exception))

    def test07_system_cannot_publish_articles_with_too_long_titles(self):
        system = MagazineSystem()
        article_to_serialize = {"title": "x" * (Article.MAXIMUM_TITLE_LENGTH + 1),
                                "text": "x" * Article.MINIMUM_TEXT_LENGTH}
        invalid_article_to_publish = system.create_serialized_article(article_to_serialize)

        with self.assertRaises(Exception) as result:
            system.publish(invalid_article_to_publish)

        error_message = f"Title must be within {Article.MINIMUM_TITLE_LENGTH}-{Article.MAXIMUM_TITLE_LENGTH}" \
                        f" characters long"
        self.assertEqual(error_message, str(result.exception))

    def test08_system_cannot_publish_articles_with_too_long_texts(self):
        system = MagazineSystem()
        article_to_serialize = {"title": "x" * Article.MINIMUM_TITLE_LENGTH,
                                "text": "x" * (Article.MAXIMUM_TEXT_LENGTH + 1)}
        invalid_article_to_publish = system.create_serialized_article(article_to_serialize)

        with self.assertRaises(Exception) as result:
            system.publish(invalid_article_to_publish)

        error_message = f"Text must be within {Article.MINIMUM_TEXT_LENGTH}-{Article.MAXIMUM_TEXT_LENGTH}" \
                        f" characters long"
        self.assertEqual(error_message, str(result.exception))

    def test09_system_cannot_be_corrupted_from_outside(self):
        system = MagazineSystem()
        articles = system.list_of_articles()

        articles.append("xxx")

        articles = system.list_of_articles()
        self.assertEqual(len(articles), 0)

    def test10_system_can_obtain_summarized_articles_list(self):
        system = MagazineSystem()
        articles_to_serialize = self._articles_to_serialize()
        articles_to_publish = self._articles_to_publish(system, articles_to_serialize)
        self._publish_articles(system, articles_to_publish)

        summarized_articles = system.list_of_summarized_articles()

        expected_articles_list = self._generate_summarized_article_list(articles_to_publish)
        self.assertEqual(summarized_articles, expected_articles_list)

    def test11_system_can_obtain_article_by_title(self):
        system = MagazineSystem()
        articles_to_serialize = self._articles_to_serialize()
        articles_to_publish = self._articles_to_publish(system, articles_to_serialize)
        self._publish_articles(system, articles_to_publish)
        title_of_article_to_obtain = "Title A"

        obtained_article = system.article_by_title(title_of_article_to_obtain)

        self.assertTrue(obtained_article.has_title(title_of_article_to_obtain))

    def test12_system_cannot_obtain_article_if_title_is_not_found(self):
        system = MagazineSystem()
        articles_to_serialize = self._articles_to_serialize()
        articles_to_publish = self._articles_to_publish(system, articles_to_serialize)
        self._publish_articles(system, articles_to_publish)
        title_of_article_to_obtain = "Title D"

        obtained_article = system.article_by_title(title_of_article_to_obtain)

        self.assertTrue(obtained_article is None)

    def _generate_summarized_article_list(self, articles):
        summarized_articles = []
        for article in articles:
            summarized_articles.append(article.summarized())
        return summarized_articles

    def _articles_to_serialize(self):
        return [
            {"title": "Title A", "text": "x" * Article.MINIMUM_TEXT_LENGTH},
            {"title": "Title B", "text": "y" * Article.MINIMUM_TEXT_LENGTH},
            {"title": "Title C", "text": "z" * Article.MINIMUM_TEXT_LENGTH}
        ]

    def _articles_to_publish(self, system, articles_to_serialize):
        articles_to_publish = []
        for article in articles_to_serialize:
            articles_to_publish.append(system.create_serialized_article(article))
        return articles_to_publish

    def _publish_articles(self, system, articles_to_publish):
        [system.publish(article) for article in articles_to_publish]


if __name__ == '__main__':
    unittest.main()
