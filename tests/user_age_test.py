from src.user_profile import UserProfile
import re

from datetime import datetime
from src.location import Location


def test_year_first_in_dob_input():
    #ERROR FOUND HERE: WHEN MONTH == MONTH from current DATE, it AUTO SUBTRACTS 1
    test_user = UserProfile("Mike", "mike@gmail.com", "pass123", "05/04/2000", Location("Los Angeles", "CA", "U.S"))
    assert test_user.get_age() == 26
    test_user_2 = UserProfile("Mike", "mike@gmail.com", "pass123", "05/01/2000", Location("Los Angeles", "CA", "U.S"))
    assert test_user_2.get_age() == 26