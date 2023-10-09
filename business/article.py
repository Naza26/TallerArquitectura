class Article:
    MINIMUM_TITLE_LENGTH = 2
    MAXIMUM_TITLE_LENGTH = 50
    MINIMUM_TEXT_LENGTH = 1800
    MAXIMUM_TEXT_LENGTH = 5200

    TOO_SHORT_TITLE_LENGTH = MINIMUM_TITLE_LENGTH - 1
    TOO_LONG_TITLE_LENGTH = MAXIMUM_TITLE_LENGTH + 1
    TOO_SHORT_TEXT_LENGTH = MINIMUM_TEXT_LENGTH - 1
    TOO_LONG_TEXT_LENGTH = MAXIMUM_TEXT_LENGTH + 1

    def __init__(self, title, text):  # You will be valid and complete one day...
        self._title = title
        self._text = text

    def has_title(self, title):
        return self._title == title

    def has_text(self, text):
        return self._text == text

    def contains_too_short_title(self):
        return len(self._title) <= self.TOO_SHORT_TITLE_LENGTH

    def contains_too_long_title(self):
        return len(self._title) >= self.TOO_LONG_TITLE_LENGTH

    def contains_too_short_text(self):
        return len(self._text) <= self.TOO_SHORT_TEXT_LENGTH

    def contains_too_long_text(self):
        return len(self._text) >= self.TOO_LONG_TEXT_LENGTH
