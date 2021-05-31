
from xavier.lib import try_me

def test_try():

    name = try_me()
    assert len(name) != 0
