from video import Video

class Movie(Video):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)