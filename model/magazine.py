class Magazine:

    def __init__(self):
        self._articles = []

    def list_of_articles(self):
        return self._articles

    def publish(self, article):
        if article.contains_too_short_title():
            raise Exception("Title cannot have less than two characters")
        if article.contains_too_long_title():
            raise Exception("Title cannot have more than fifty characters")
        if article.contains_too_short_text():
            raise Exception("Text cannot have less than 1800 characters")
        if article.contains_too_long_text():
            raise Exception("Text cannot have more than 5200 characters")
        self._articles.append(article)
