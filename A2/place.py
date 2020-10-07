"""..."""


class Place:

    def __init__(self, name="", country="", priority=0, is_visited=False):
        """set the place vaules"""
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        """__str__ method"""
        return_str = "%s%s%d" % (self.name, self.country, self.priority) + str(self.is_visited)
        print(return_str)
        return return_str

    def mark_place_unvisited(self):
        """mark place unvisited method"""
        self.is_visited = False

    def mark_place_visited(self):
        """mark place visited method"""
        self.is_visited = True

    def check_visited(self):
        """check place is visited method"""
        return self.is_visited

    def check_importance(self):
        """mark place importance method"""
        if self.priority <= 2:
            return "important"
        else:
            return "unimportant"
