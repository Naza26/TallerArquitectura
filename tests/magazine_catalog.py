from business.model.article import Article
from business.model.magazine import Magazine


class MagazineCatalog:
    def __init__(self):
        self.standard_title = self.standard_article_title()
        self.standard_text = self.standard_article_text()

    def empty_magazine(self):
        return Magazine()

    def long_article_title(self):
        return "x" * (max(Article.VALID_TITLE_LENGTH) + 1)

    def short_article_title(self):
        return "x" * (min(Article.VALID_TEXT_LENGTH) - 1)

    def long_article_text(self):
        return "x" * (max(Article.VALID_TEXT_LENGTH) + 1)

    def short_article_text(self):
        return "x" * (min(Article.VALID_TEXT_LENGTH) - 1)

    def standard_article_text(self):
        return "x" * min(Article.VALID_TEXT_LENGTH)

    def standard_article_title(self):
        return "x" * min(Article.VALID_TITLE_LENGTH)

    def create_article(self, title=None, text=None):
        if title is None:
            title = self.standard_title
        if text is None:
            text = self.standard_text
        return Article(title, text)

    def sample_article_from(self, articles):
        return articles[0]

    def generate_summarized_article_list(self, articles):
        summarized_articles = []
        for article in articles:
            summarized_articles.append(article.summarized())
        return summarized_articles

    def articles_to_serialize(self):
        return [
            {"title": "Title A", "text": "x" * Article.MINIMUM_TEXT_LENGTH},
            {"title": "Title B", "text": "y" * Article.MINIMUM_TEXT_LENGTH},
            {"title": "Title C", "text": "z" * Article.MINIMUM_TEXT_LENGTH}
        ]

    def articles_to_publish(self, system, articles_to_serialize):
        articles_to_publish = []
        for article in articles_to_serialize:
            articles_to_publish.append(system.create_serialized_article(article))
        return articles_to_publish

    def publish_articles(self, system, articles_to_publish):
        [system.publish(article) for article in articles_to_publish]
