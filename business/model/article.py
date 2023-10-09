class Article:
    MINIMUM_TITLE_LENGTH = 2
    MAXIMUM_TITLE_LENGTH = 50
    MINIMUM_TEXT_LENGTH = 1800
    MAXIMUM_TEXT_LENGTH = 5200

    VALID_TITLE_RANGE = range(MINIMUM_TITLE_LENGTH, MAXIMUM_TITLE_LENGTH)
    VALID_TEXT_RANGE = range(MINIMUM_TEXT_LENGTH, MAXIMUM_TEXT_LENGTH)

    def __init__(self, title, text):  # You will be valid and complete one day...
        self._title = title
        self._text = text

    def has_title(self, title):
        return self._title == title

    def has_text(self, text):
        return self._text == text

    def contains_invalid_text_length(self):
        return len(self._text) not in self.VALID_TEXT_RANGE

    def contains_invalid_title_length(self):
        return len(self._title) not in self.VALID_TITLE_RANGE
