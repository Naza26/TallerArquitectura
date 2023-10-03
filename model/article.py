class Article:
    def __init__(self, title, text):  # You will be valid and complete one day...
        self._title = title
        self._text = text

    def has_title(self, title):
        return self._title == title

    def has_text(self, text):
        return self._text == text

    def contains_too_short_title(self):
        return len(self._title) < 2

    def contains_too_long_title(self):
        return len(self._title) > 50

    def contains_too_short_text(self):
        return len(self._text) < 1800

    def contains_too_long_text(self):
        return len(self._text) > 5200