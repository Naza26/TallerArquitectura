class Article:
    MINIMUM_TITLE_LENGTH = 2
    MAXIMUM_TITLE_LENGTH = 50
    MINIMUM_TEXT_LENGTH = 1800
    MAXIMUM_TEXT_LENGTH = 5200

    VALID_TITLE_LENGTH = range(MINIMUM_TITLE_LENGTH, MAXIMUM_TITLE_LENGTH)
    VALID_TEXT_LENGTH = range(MINIMUM_TEXT_LENGTH, MAXIMUM_TEXT_LENGTH)

    def __init__(self, title, text):  # You will be valid and complete one day...
        self._title = title
        self._text = text

    def contains_title_named(self, title):
        return self._title == title

    def contains_text_named(self, text):
        return self._text == text

    def contains_invalid_text_length(self):
        return len(self._text) not in self.VALID_TEXT_LENGTH

    def contains_invalid_title_length(self):
        return len(self._title) not in self.VALID_TITLE_LENGTH

    def summarized(self):
        return {self._title: self._text[:100]}
