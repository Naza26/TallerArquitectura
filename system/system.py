from business.magazine import Magazine


class System:
    def __init__(self):
        self._magazine = Magazine()

    def list_of_articles(self):
        return self._magazine.list_of_articles()

    def publish(self, article):
        self._magazine.publish(article)
