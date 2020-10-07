"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
from operator import itemgetter
from place import Place
from placecollection import PlaceCollection
from place import Place


def main():
    """main method"""
    """load the file"""
    filename = "places.csv"
    """create a places object and load a csv file"""
    places_obj = PlaceCollection()
    places_obj.load_places(filename)
    places = places_obj.places
    # print info
    print("Travel Tracker 1.0 - by Tong Wenlin")
    print("%d places loaded from places.csv" % len(places))

    """run the choice option"""
    loop = True
    while loop:
        display_main_menu()
        choice = input(">>> ").upper()

        if choice == "L":
            print(places)

        elif choice == "A":
            name = input("Name: ")
            country = input("Country: ")
            priority = int(input("Priority: "))
            place_obj = Place(name=name, country=country, priority=priority)
            places.append((place_obj.name, place_obj.country, place_obj.priority, place_obj.is_visited))

        elif choice == "M":
            name = input("Input a place name:")
            for place in places:
                if place[0] == name:
                    place_obj = Place(name=place[0], country=place[1], priority=place[2], is_visited=place[3])
                    place_obj.mark_place_visited()
                    places.remove(place)
                    new_place = (place_obj.name, place_obj.country, place_obj.priority, place_obj.is_visited)
                    places.append(new_place)
                    print("add success")
                    break

        elif choice == "Q":
            places_obj.save_places()
            loop = False
            print("%d places saved to places.csv" % len(places))
            print("Have a nice day :)")

        else:
            print("Invalid menu choice")


def display_main_menu():
    """print main menu"""
    print("Menu:")
    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("S - Save")
    print("Q - Quit")


if __name__ == '__main__':
    main()
