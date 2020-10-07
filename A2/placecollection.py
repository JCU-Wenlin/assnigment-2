"""..."""
import operator

"""define PlaceCollection class"""


class PlaceCollection:
    """set the places list"""
    def __init__(self):
        self.places = []

    def load_places(self, file_path):
        """load the file_path as a list"""
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line_content_list = line.replace("\n", "").split(",")
                place_dir = (
                    line_content_list[0], line_content_list[1], int(line_content_list[2]), bool(line_content_list[3]))
                self.places.append(place_dir)
        f.close()
        print("load places success")

    def save_places(self):
        """save the list to csv file"""
        place_file_path = "./places.csv"
        places_file = open(place_file_path, "w", encoding="utf-8")
        for place_dir in self.places:
            save_str = place_dir[0] + "," + place_dir[1] + "," + str(place_dir[2]) + "," + str(place_dir[3]) + "\n"
            places_file.writelines(save_str)
        places_file.close()
        print("save places success")

    def add_place(self, place):
        """add the place to places list"""
        self.places.append(place)
        print("add place success")

    def get_unvisited_number(self):
        """get the number of place unvisited"""
        unvisited_places_number = 0
        for place in self.places:
            if not place[3]:
                unvisited_places_number += 1
        return unvisited_places_number

    def sort(self, sort_way):
        """sort the places list"""
        if sort_way == "name":
            def my_key2(x):
                return x[0]

        elif sort_way == "country":
            def my_key2(x):
                return x[1]
        elif sort_way == "priority":
            def my_key2(x):
                return x[2]
        elif sort_way == "is_visited":
            def my_key2(x):
                return x[3]
            # return sorted(self.places, key=lambda x: (x[0], x[2].lower()))
        return self.places.sort(key=my_key2)
