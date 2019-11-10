import pytest
from checker.gather import Segment
import checker.capitals

'''
Need to create a fixture of a list
of Segment objects, each object including
some Japanese and English text.
'''


@pytest.fixture
def segment():
    return Segment('', '', [], [], False, {}, {},
                   False, False, False, False, False, False,
                   [], False, [], [], [], {}, {}, False, False, [])


def test_leading_capital_check(segment):
    pass
