from src.user_profile import UserProfile
import re

from datetime import datetime
from src.location import Location

def test_is_password_valid():
    assert UserProfile.valid_password("andrewGBamm2024!") == True
