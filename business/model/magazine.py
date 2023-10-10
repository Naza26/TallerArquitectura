class Magazine:

    def __init__(self):
        self._articles = []

    def list_of_articles(self):
        return self._articles

    def publish(self, article):
        self._validate_article_to_publish(article)
        self._articles.append({len(self._articles) + 1: article})

    def _validate_article_to_publish(self, article):
        if article.contains_invalid_title_length():
            raise Exception(f"Title must be within {article.MINIMUM_TITLE_LENGTH}-{article.MAXIMUM_TITLE_LENGTH} "
                            f"characters long")
        if article.contains_invalid_text_length():
            raise Exception(f"Text must be within {article.MINIMUM_TEXT_LENGTH}-{article.MAXIMUM_TEXT_LENGTH} "
                            f"characters long")
