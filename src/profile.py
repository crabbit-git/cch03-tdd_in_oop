class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.favourites = []
    
    def add_favourite(self, movie):
        self.favourites.append(movie)

    def remove_favourite(self, movie):
        self.favourites.remove(movie)

    def get_favourites(self):
        return self.favourites
