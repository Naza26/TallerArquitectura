class Magazine:

    def __init__(self):
        self._articles = []

    def list_of_articles(self):
        return self._articles

    def publish(self, article):
        self._validate_article_to_publish(article)
        self._articles.append(article)

    def _validate_article_to_publish(self, article):
        if article.contains_too_short_title() or article.contains_too_long_title():
            raise Exception(f"Title must be within {article.MINIMUM_TITLE_LENGTH}-{article.MAXIMUM_TITLE_LENGTH} "
                            f"characters long")
        if article.contains_too_short_text() or article.contains_too_long_text():
            raise Exception(f"Text must be within {article.MINIMUM_TEXT_LENGTH}-{article.MAXIMUM_TEXT_LENGTH} "
                            f"characters long")
