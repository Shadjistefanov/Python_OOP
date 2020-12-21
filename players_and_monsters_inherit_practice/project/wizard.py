from project.hero import Hero


class Wizard(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

    def __repr__(self):
        return f"{self.username} of type {self.__class__.__name__} has level {self.level}"