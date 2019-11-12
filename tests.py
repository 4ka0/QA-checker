# -*- coding: utf-8 -*-

import pytest
from gather import Segment
import capitals
import characters
import digits


@pytest.fixture
def segments():
    segments = []
    segment = Segment('なお、正孔輸送層12は、NiO、またはMoO3等の無機材料を含む。',
                      'Moreover, the positive MoO3 transport layers 12.',
                      [], [], False, {}, {}, False, False, False, False,
                      False, False, [], False, [], [], [], {}, {}, False,
                      False, [])
    segments.append(segment)
    segment = Segment('アレイ基板4上の第1電極8aの上層には、正孔注入層10と。',
                      'the positive 8 injection layers 10, the positive.',
                      [], [], False, {}, {}, False, False, False, False,
                      False, False, [], False, [], [], [], {}, {}, False,
                      False, [])
    segments.append(segment)
    segment = Segment('アレイ基板5上の第5電極9の上層には、正孔注入層9と。',
                      '5ひらがなthe カタカナ ｶﾀｶﾅ7with 漢字 １０test ｔｅｓｔ9',
                      [], [], False, {}, {}, False, False, False, False,
                      False, False, [], False, [], [], [], {}, {}, False,
                      False, [])
    segments.append(segment)
    segment = Segment('すなわち、電子注入層上に感光性材料14aを塗布し(S36)、\
                      マスクパターンMを設置し(S38)、感光性材料14aを露光し(S40)、\
                      感光性材料14aの一部を除去(S42)してもよい。',
                      'In other words, a photosensitive material 15a may be \
                      applied onto an electron injection layer (S36), a mask \
                      pattern M may be placed (S36), the photosensitive \
                      material 14a may be exposed (S40), and a portion of \
                      the photosensitive material 16a may be removed (S42).',
                      [], [], False, {}, {}, False, False, False, False,
                      False, False, [], False, [], [], [], {}, {}, False,
                      False, [])
    segments.append(segment)
    return segments


def test_leading_capital_check(segments):
    assert len(segments) == 4
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
    assert segments[2].asian_chars == ['ひ', 'ら', 'が', 'な', 'カ', 'タ', 'カ',
                                       'ナ', 'ｶ', 'ﾀ', 'ｶ', 'ﾅ', '漢', '字',
                                       '１', '０', 'ｔ', 'ｅ', 'ｓ', 'ｔ']


def test_digit_check(segments):

    digits.digit_check(segments)

    assert segments[0].jap_nums == ['12', '3']
    assert segments[0].eng_nums == ['3', '12']
    assert segments[0].error_found is False

    assert segments[1].jap_nums == ['4', '1', '8', '10']
    assert segments[1].eng_nums == ['8', '10']
    assert segments[1].missing_nums == {'4': 1, '1': 1}
    assert segments[1].extra_nums == {}
    assert segments[1].error_found is True

    assert segments[2].jap_nums == ['5', '5', '9', '9']
    assert segments[2].eng_nums == ['5', '7', '１０', '9']
    assert segments[2].missing_nums == {'5': 1, '9': 1}
    assert segments[2].extra_nums == {'7': 1, '１０': 1}
    assert segments[2].error_found is True

    assert segments[3].jap_nums == ['14', '36', '38', '14', '40', '14', '42']
    assert segments[3].eng_nums == ['15', '36', '36', '14', '40', '16', '42']
    assert segments[3].missing_nums == {'14': 2, '38': 1}
    assert segments[3].extra_nums == {'15': 1, '36': 1, '16': 1}
    assert segments[3].error_found is True
