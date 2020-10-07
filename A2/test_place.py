"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)

    # TODO: Write tests to show this initialisation works
    # Test the name
    print("Test the name:", new_place.name)
    # Test the country
    print("Test the country:", new_place.country)
    # Test the priority
    print("Test the priority:", new_place.priority)
    # Test is visited
    print("Test is visited:", new_place.is_visited)

    # TODO: Add more tests, as appropriate, for each method
    # Test method mark_place_visited
    print("Test method mark_place_visited:", new_place.mark_place_visited())
    # Test method check_visited
    print("Test method check_visited:", new_place.check_visited())
    # Test method mark_place_unvisited
    print("Test method mark_place_unvisited:", new_place.mark_place_unvisited())
    # Test method check_visited
    print("Test method check_visited:", new_place.check_visited())
    # Test method check_importance
    print("Test method check_importance:", new_place.check_importance())


run_tests()
