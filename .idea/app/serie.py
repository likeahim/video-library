from video import Video

class Serie(Video):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def calculate_number(self, number):
        if int(number) > 9:
            return number
        else:
            return number.zfill(2)

    def __str__(self):
        return f"{self.title} S{self.calculate_number(self.season)}E{self.calculate_number(self.episode)}"