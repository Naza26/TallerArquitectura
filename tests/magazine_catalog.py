from business.model.article import Article
from business.model.magazine import Magazine


class MagazineCatalog:
    def __init__(self):
        self.standard_title = self.standard_article_title()
        self.standard_text = self.standard_article_text()

    def empty_magazine(self):
        return Magazine()

    def magazine_with_articles(self, articles):
        magazine = self.empty_magazine()
        for article in articles:
            magazine.publish(article)
        return magazine


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

    def summarized_article_list(self, articles):
        summarized_articles = []
        for article in articles:
            summarized_articles.append(article.summarized())
        return summarized_articles
