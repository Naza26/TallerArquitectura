from model.article import Article
from model.magazine import Magazine


class Catalog:
    def __init__(self):
        self.default_title = self.standard_article_title()
        self.default_text = self.standard_article_text()

    def empty_magazine(self):
        return Magazine()

    def long_article_title(self):
        return "x" * 51

    def short_article_title(self):
        return "x"

    def long_article_text(self):
        return "x" * 5201

    def short_article_text(self):
        return "x" * 1799

    def standard_article_text(self):
        return "x" * 1800

    def standard_article_title(self):
            return "x" * 2

    def create_article(self, title=None, text=None):
        if title is None:
            title = self.default_title
        if text is None:
            text = self.default_text
        return Article(title, text)
