import unittest
from src.account import *
from src.profile import *

class TestAccount(unittest.TestCase):

    def setUp(self):

        # Creating some objects to use in the tests
        self.profile_1 = Profile("harrisonF", "myP@assword")
        self.profile_2 = Profile("markH", "anotherP@ssword")

        self.account_1 = Account("Jane", "Smith", "janes@email.com")

    # Test an Account can add a Profile
    def acct_can_add_profile(self):
        self.assertEqual(0, len(self.profiles))
        self.account_1.add_profile(self.profile_1)
        self.assertEqual([self.profile_1], self.account_1.profiles)

    # Test an Account can remove a given Profile
    def acct_can_remove_profile(self):
        self.assertEqual(0, len(self.profiles))
        self.account_1.add_profile(self.profile_1)
        self.account_1.add_profile(self.profile_2)
        self.account_1.remove_profile(self.profile_2)
        self.assertEqual([self.profile_1], self.account_1.profiles)

    # Test an Account can return a list of Profiles
    def acct_can_return_profiles(self):
        if self.account_1.get_profiles() != None:
            self.assertEqual(0, len(self.profiles))
            self.account_1.add_profile(self.profile_1)
            self.account_1.add_profile(self.profile_2)
            self.assertEqual(2, len(self.account_1.get_profiles()))
