class Video:
    def __init__(self, title, year, genre, views):
        self.title = title
        self.year = year
        self.genre = genre

        self._views = views
    @property
    def play(self):
        self._views = int(self._views) + 1

    def __str__(self):
        return f"{self.title} {self.year} Views: {self._views}"