class Account:
    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.profiles = []

    def add_profile(self, profile):
        self.profiles.append(profile)

    def remove_profile(self, profile):
        self.profiles.remove(profile)

    def get_profiles(self):
        return self.profiles
