import pytest
from sample import reverse_string  
def test_reverse_string():
    s = list("Divya Chauhan") 
    reverse_string(s)
    assert s == list("nahuahC ayviD") 
