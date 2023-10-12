from business.model.article import Article
from business.model.magazine import Magazine


class MagazineSystem:
    def __init__(self):
        self._magazine = Magazine()

    def list_of_articles(self):
        return self._magazine.list_of_articles().copy()

    def publish(self, article):
        self._magazine.publish(article)

    def create_serialized_article(self, article):
        return Article(article["title"], article["text"])

    def list_of_summarized_articles(self):
        summarized_articles = []
        for article in self.list_of_articles():
            article = list(article.values())[0]
            summarized_articles.append(article.summarized())
        return summarized_articles

    def article_by_id(self, id_of_article_to_obtain):
        for article in self.list_of_articles():
            print("ITEMS: ", list(article.items())[0])
            _id, article = list(article.items())[0]
            if int(_id) == id_of_article_to_obtain:
                return article
        return None