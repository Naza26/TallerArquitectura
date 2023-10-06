class Magazine:

    def __init__(self):
        self._articles = []

    def list_of_articles(self):
        return self._articles

    def publish(self, article):
        self._validate_article_to_publish(article)
        self._articles.append(article)

    def _validate_article_to_publish(self, article):
        if article.contains_too_short_title():
            raise Exception(f"Title cannot have less than {article.SHORT_TITLE_LENGTH} characters")
        if article.contains_too_long_title():
            raise Exception(f"Title cannot have more than {article.LONG_TITLE_LENGTH} characters")
        if article.contains_too_short_text():
            raise Exception(f"Text cannot have less than {article.SHORT_TEXT_LENGTH} characters")
        if article.contains_too_long_text():
            raise Exception(f"Text cannot have more than {article.LONG_TEXT_LENGTH} characters")
