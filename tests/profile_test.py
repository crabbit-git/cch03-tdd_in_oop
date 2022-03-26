import unittest
from src.profile import *
from src.movie import *

class TestProfile(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.movie_1 = Movie("The Fugitive", "Andrew Daivs", 9)
        self.movie_2 = Movie("Hunger Games", "Gary Ross", 7)

        self.profile_1 = Profile("harrisonF", "myP@assword")

    # Test a Profile can add a favourite Movie
    def profile_can_add_fav(self):
        self.assertEqual(0, len(self.profile_1.favourites))
        self.profile_1.add_favourite(self.movie_1)
        self.assertEqual([self.movie_1], self.profile_1.favourites)

    # Test a Profile can remove a given Movie from favourites
    def profile_can_remove_fav(self):
        self.assertEqual(0, len(self.profile_1.favourites))
        self.profile_1.add_favourite(self.movie_1)
        self.profile_1.add_favourite(self.movie_2)
        self.profile_1.remove_favourite(self.movie_1)
        self.assertEqual([self.movie_2], self.profile_1.favourites)

    # Test a Profile can return a list of Favourites
    def profile_returns_favs(self):
        if self.profile_1.get_favourites() != None:
            self.assertEqual(0, len(self.profile_1.get_favourites()))
            self.profile_1.add_favourite(self.movie_1)
            self.profile_1.add_favourite(self.movie_2)
            self.assertEqual(2, len(self.profile_1.get_favourites()))
