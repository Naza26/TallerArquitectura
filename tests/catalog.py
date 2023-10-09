from business.article import Article
from business.magazine import Magazine


class Catalog:
    def __init__(self):
        self.standard_title = self.standard_article_title()
        self.standard_text = self.standard_article_text()

    def empty_magazine(self):
        return Magazine()

    def long_article_title(self):
        return "x" * Article.TOO_LONG_TITLE_LENGTH

    def short_article_title(self):
        return "x" * Article.TOO_SHORT_TITLE_LENGTH

    def long_article_text(self):
        return "x" * Article.TOO_LONG_TEXT_LENGTH

    def short_article_text(self):
        return "x" * Article.TOO_SHORT_TEXT_LENGTH

    def standard_article_text(self):
        return "x" * Article.MINIMUM_TEXT_LENGTH

    def standard_article_title(self):
        return "x" * Article.MINIMUM_TITLE_LENGTH

    def create_article(self, title=None, text=None):
        if title is None:
            title = self.standard_title
        if text is None:
            text = self.standard_text
        return Article(title, text)

    def get_an_article_from(self, articles):
        return articles[0]