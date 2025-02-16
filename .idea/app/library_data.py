import csv

from movie import Movie
from serie import Serie

class LibraryData:
    def __init__(self, videos=None):
        if videos is None:
            videos = []
        self.videos = videos

    def load_videos_from_csv(self):
        with open("movies.csv", mode="r", newline='') as moviefile:
            reader = csv.DictReader(moviefile)
            for row in reader:
                movie = Movie(
                    row['title'].strip(),
                    row['year'].strip(),
                    row['genre'].strip(),
                    row['views'].strip()
                )
                self.videos.append(movie)
        with open("series.csv", mode="r", newline='') as seriefile:
            reader = csv.DictReader(seriefile)
            for row in reader:
                serie = Serie(
                    row['season'].strip(),
                    row['episode'].strip(),
                    row['title'].strip(),
                    row['year'].strip(),
                    row['genre'].strip(),
                    row['views'].strip()
                )
                self.videos.append(serie)

    def open_library(self):
        print("Videos library")
        self.load_videos_from_csv()
        for row in self.videos:
            if isinstance(row, Serie):
                print(row)
                row.play
                print(row)
