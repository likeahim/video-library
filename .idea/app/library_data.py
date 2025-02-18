import csv
import random
from datetime import datetime
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

    def save_data(self):
        with open("movies.csv", "w", newline='') as csvfile:
            fieldnames = ["title", "year", "genre", "views"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for video in self.videos:
                if isinstance(video, Movie):
                    writer.writerow({
                        "title": video.title,
                        "year": video.year,
                        "genre": video.genre,
                        "views": video._views
                    })

        with open("series.csv", "w", newline='') as csvfile:
            fieldnames = ["title", "year", "season", "episode", "genre", "views"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for video in self.videos:
                if isinstance(video, Serie):
                    writer.writerow({
                        "title": video.title,
                        "year": video.year,
                        "season": video.season,
                        "episode": video.episode,
                        "genre": video.genre,
                        "views": video._views
                    })

    def exit_program(self):
        self.save_data()
        print("Data saved\nExiting program\nGoodbye")

    def get_movies(self):
        movies = []
        for row in self.videos:
            if isinstance(row, Movie):
                movies.append(row)
        return sorted(movies, key=lambda movie: movie.title)

    def get_series(self):
        series = []
        for row in self.videos:
            if isinstance(row, Serie):
                series.append(row)
        return sorted(series, key=lambda serie: serie.title)

    def show_videos(self, videos):
        for video in videos:
            print(video)

    def search(self):
        title_to_search = input("Type the title you look for:\n->")
        results = [video for video in self.videos if title_to_search.lower() in video.title.lower()]
        if results:
            for video in results:
                print(video)
            return
        else:
            print("No such a movie in database")
            return []

    def generate_views(self):
        random_video = random.choice(self.videos)
        new_views = random.randint(1, 100)
        random_video._views = int(random_video._views) + new_views

    def change(self):
        for x in range(10):
            self.generate_views()

    def top_titles(self):
        videos_to_show = 3
        filtered_videos = sorted(self.videos, key=lambda video: int(video._views), reverse=True)
        today = datetime.today().strftime("%d.%m.%Y")
        print(f"Most popular movies and series for {today}")
        return filtered_videos[:videos_to_show]

    def open_library(self):
        print("Videos library")
        try:
            self.load_videos_from_csv()
        except FileNotFoundError:
            print("File not found")
        except csv.Error:
            print("Loading file failed. Check files forma")
        message = ""
        while message != "exit":
            message = input("""
            What would you like to do?
            exit - exit the program
            m - show all movies
            s - show all series
            search - search by title
            change - change number of views
            top - top titles today
            save - save data
            """).lower()
            if message == "m":
                self.show_videos(self.get_movies())
            elif message == "s":
                self.show_videos(self.get_series())
            elif message == "search":
                self.search()
            elif message == "save":
                self.save_data()
            elif message == "change":
                self.change()
            elif message == "top":
                self.show_videos(self.top_titles())
        self.exit_program()
