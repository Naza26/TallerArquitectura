from business.article import Article
from business.magazine import Magazine


class MagazineSystem:
    def __init__(self):
        self._magazine = Magazine()

    def list_of_articles(self):
        return self._magazine.list_of_articles()

    def publish(self, article):
        self._magazine.publish(article)

    def create_serialized_article(self, article):
        return Article(article["title"], article["text"])
