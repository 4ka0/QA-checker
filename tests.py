import pytest
from gather import Segment
import capitals
import characters
import numbers

'''
Run with
pytest --pyargs tests.py
'''


@pytest.fixture
def segments():
    segments = []
    segment1 = Segment('なお、正孔輸送層12は、NiO、またはMoO3等の無機材料を含む。',
                       'Moreover, the positive Mo03 transport layers 12.',
                       [], [], False, {}, {}, False, False, False, False,
                       False, False, [], False, [], [], [], {}, {}, False,
                       False, [])
    segments.append(segment1)
    segment2 = Segment('アレイ基板4上の第1電極8aの上層には、正孔注入層10と。',
                       'the positive hole injection layers 10, the positive.',
                       [], [], False, {}, {}, False, False, False, False,
                       False, False, [], False, [], [], [], {}, {}, False,
                       False, [])
    segments.append(segment2)
    segment3 = Segment('アレイ基板4上の第1電極8aの上層には、正孔注入層10と。',
                       'ひらがなthe カタカナ ｶﾀｶﾅwith 漢字 １０test ｔｅｓｔ',
                       [], [], False, {}, {}, False, False, False, False,
                       False, False, [], False, [], [], [], {}, {}, False,
                       False, [])
    segments.append(segment3)
    return segments


def test_leading_capital_check(segments):
    capitals.leading_capital_check(segments)
    assert segments[0].capitalization_error_found is False
    assert segments[0].error_found is False
    assert segments[1].capitalization_error_found is True
    assert segments[1].error_found is True


def test_asian_character_check(segments):
    characters.asian_character_check(segments)
    assert segments[0].asian_char_found is False
    assert segments[0].error_found is False
    assert segments[2].asian_char_found is True
    assert segments[2].error_found is True
    assert segments[2].asian_chars == ['ひ', 'ら', 'が', 'な', 'カ', 'タ', 'カ', 'ナ', 'ｶ', 'ﾀ', 'ｶ', 'ﾅ', '漢', '字', '１', '０', 'ｔ', 'ｅ', 'ｓ', 'ｔ']


'''
Error message
AttributeError: module 'numbers' has no attribute 'number_check'
'''
def test_number_check(segments):
    numbers.number_check(segments)
    assert segments[0].error_found is False
    assert segments[0].jap_nums == [12, 3]
    assert segments[0].eng_nums == [12, 3]
    assert segments[1].missing_nums == {}
    assert segments[1].extra_nums == {}
    assert segments[1].error_found is True
    assert segments[1].jap_nums == [4, 1, 8, 10]
    assert segments[1].eng_nums == [10]
    assert segments[1].missing_nums == {4: 1, 1: 1, 8: 1, 10: 1}
    assert segments[1].extra_nums == {10: 1}
