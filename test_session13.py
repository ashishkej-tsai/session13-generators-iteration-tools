import pytest
import session13
from session13 import *
 

def test_odd_secs():
    assert count_violations_by_make()['FORD'] == 104, "Something is wrong"

