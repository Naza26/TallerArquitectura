class Article:
    SHORT_TITLE_LENGTH = 2
    LONG_TITLE_LENGTH = 50
    SHORT_TEXT_LENGTH = 1800
    LONG_TEXT_LENGTH = 5200
    def __init__(self, title, text):  # You will be valid and complete one day...
        self._title = title
        self._text = text

    def has_title(self, title):
        return self._title == title

    def has_text(self, text):
        return self._text == text

    def contains_too_short_title(self):
        return len(self._title) < self.SHORT_TITLE_LENGTH

    def contains_too_long_title(self):
        return len(self._title) > self.LONG_TITLE_LENGTH

    def contains_too_short_text(self):
        return len(self._text) < self.SHORT_TEXT_LENGTH

    def contains_too_long_text(self):
        return len(self._text) > self.LONG_TEXT_LENGTH
