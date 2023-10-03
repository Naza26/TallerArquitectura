class Magazine:

    def __init__(self):
        self._articles = []

    def list_of_articles(self):
        return self._articles

    def publish(self, article):
        if len(article.title()) < 2:
            raise Exception("Title cannot have less than two characters")
        if len(article.title()) > 50:
            raise Exception("Title cannot have more than fifty characters")
        if len(article.text()) < 1800:
            raise Exception("Text cannot have less than 1800 characters")
        if len(article.text()) > 5200:
            raise Exception("Text cannot have more than 5200 characters")
        self._articles.append(article)
