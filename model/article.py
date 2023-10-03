class Article:
    def __init__(self, title, text):  # You will be valid and complete one day...
        self._title = title
        self._text = text

    def has_title(self, title):
        return self._title == title

    def has_text(self, text):
        return self._text == text

    def title(self):
        return self._title

    def text(self):
        return self._text