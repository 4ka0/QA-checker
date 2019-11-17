# -*- coding: utf-8 -*-

import pytest

from gather import Segment
import gather
import verify
import capitals
import characters
import digits
import punctuation
import repeaters
import unpaired
import spaces
import untranslated


def test_constructor():
    s = Segment('なお、正孔輸送層12は、NiO、（またはMoO3）等の無機材料を含んでいてもよい。',
                'moreover, the positive  hole transport layers 12 may include an inorganic material such as NiO (or MoO3].',
                '', '', [], [], False, {}, {}, False, False, False, False, False, False, [], False, [], False, False, [])
    assert isinstance(s, Segment)


@pytest.fixture
def tmxfile():
    tmxfile = '/Volumes/Untitled/test1.tmx'
    return tmxfile


def test_gather_segments(tmxfile):
    gather.gather_segments(tmxfile)




@pytest.mark.parametrize('user_input,expected',
                         [(['checker.py', 'test.tmx'], True),
                          (['checker.py'], False),
                          (['checker.py', 'test1.tmx', 'test2.tmx'], False),
                          (['checker.py', 'test1.txt'], False)])
def test_user_input_check(user_input, expected):
    assert verify.user_input_check(user_input) == expected


@pytest.fixture
def segments():
    segments = []
    segment0 = Segment('なお、正孔輸送層12は、NiO、（またはMoO3）等の無機材料を含んでいてもよい。',
                       'moreover, the positive  hole transport layers 12 may include an inorganic material such as NiO (or MoO3].',
                       '', '', [], [], False, {}, {}, False, False, False, False, False, False, [], False, [], False, False, [])
    segments.append(segment0)
    segment1 = Segment('具体的には、感光性材料14aに対する量子ドットの濃度は、1～50wt%の範囲であることが好ましく、10～40wt%の範囲であることがより好ましい。',
                       'Specifically, ひらがなthe concentration   of the quantumdots with with カタカナrespect to the photosensitive ｶﾀｶﾅ material 14a is preferably in the in the 漢字 range of 1 to １０ wt%, and more preferably in the range of 10 to 40 wt%.ｔｅｓｔ',
                       '', '', [], [], False, {}, {}, False, False, False, False, False, False, [], False, [], False, False, [])
    segments.append(segment1)
    segment2 = Segment('電子輸送層16と第2電極18aとの形成は、上述の印刷法の他に、スパッタ法、または真空蒸着法等を使用して実施してもよい。',
                       'The formation of the electron transport layer 18 and the 2nd electrode 18a may be carried out using a a sputtering {method, a vacuum deposition method, or the like other than the aforementioned printing method; ',
                       '', '', [], [], False, {}, {}, False, False, False, False, False, False, [], False, [], False, False, [])
    segments.append(segment2)
    segment3 = Segment('すなわち、電子注入層上に感光性材料14aを塗布し(S36)、マスクパターンMを設置し(S38)、感光性材料14aを露光し(S40)、感光性材料14aの一部を除去(S42)してもよい。',
                       ' In other words, a photosensitive material 15a may be applied onto an electron injection layer (S36), a mask pattern M may be placed ((S36), the photosensitive material 14a may be exposed (S40), and a portion of the photosensitive material 16a may be removed (S42).   ',
                       '', '', [], [], False, {}, {}, False, False, False, False, False, False, [], False, [], False, False, [])
    segments.append(segment3)
    segment4 = Segment('量子ドットが分散する感光性材料の基材への塗布と、前記基材上の前記感光性材料における露光領域および非露光領域の形成と、前記露光領域の少なくとも一部、あるいは前記非露光領域の少なくとも一部における前記感光性材料の除去とを行う発光層の製造装置。',
                       ' A manufacturing apparatus for a light-emitting layer that carries out: application of a photosensitive material in which quantum dots are dispersed, onto a base material; formation of an exposed region and a non-exposed region in the the photosensitive material on the base material; and removal of the of the photosensitive material in at least a portion of the exposed region or at least a portion of the non-exposed region',
                       '', '', [], [], False, {}, {}, False, False, False, False, False, False, [], False, [], False, False, [])
    segments.append(segment4)
    segment5 = Segment('量子ドットが分散する感光性材料の基材への塗布と、前記基材上の前記感光性材料における露光領域および非露光領域の形成と、前記露光領域の少なくとも一部、あるいは前記非露光領域の少なくとも一部における前記感光性材料の除去とを行う発光層の製造装置。',
                       '    ',
                       '', '', [], [], False, {}, {}, False, False, False, False, False, False, [], False, [], False, False, [])
    segments.append(segment5)
    return segments


def test_leading_capital_check(segments):
    assert len(segments) == 6
    capitals.leading_capital_check(segments)
    assert segments[0].capitalization_error_found is True
    assert segments[0].error_found is True
    assert segments[1].capitalization_error_found is False
    assert segments[1].error_found is False
    assert segments[2].capitalization_error_found is False
    assert segments[2].error_found is False
    assert segments[3].capitalization_error_found is False
    assert segments[3].error_found is False
    assert segments[4].capitalization_error_found is False
    assert segments[4].error_found is False


def test_asian_character_check(segments):
    characters.asian_character_check(segments)
    assert segments[0].asian_char_found is False
    assert segments[0].error_found is False
    assert segments[0].asian_chars == []
    assert segments[1].asian_char_found is True
    assert segments[1].error_found is True
    assert segments[1].asian_chars == ['ひ', 'ら', 'が', 'な', 'カ', 'タ', 'カ', 'ナ', 'ｶ', 'ﾀ', 'ｶ', 'ﾅ', '漢', '字', '１', '０', 'ｔ', 'ｅ', 'ｓ', 'ｔ']
    assert segments[2].asian_char_found is False
    assert segments[2].error_found is False
    assert segments[2].asian_chars == []
    assert segments[3].asian_char_found is False
    assert segments[3].error_found is False
    assert segments[3].asian_chars == []
    assert segments[4].asian_char_found is False
    assert segments[4].error_found is False
    assert segments[4].asian_chars == []


def test_digit_check(segments):
    digits.digit_check(segments)
    assert segments[0].jap_nums == ['12', '3']
    assert segments[0].eng_nums == ['12', '3']
    assert segments[0].missing_nums == {}
    assert segments[0].extra_nums == {}
    assert segments[0].error_found is False
    assert segments[1].jap_nums == ['14', '1', '50', '10', '40']
    assert segments[1].eng_nums == ['14', '1', '１０', '10', '40']
    assert segments[1].missing_nums == {'50': 1}
    assert segments[1].extra_nums == {'１０': 1}
    assert segments[1].error_found is True
    assert segments[2].jap_nums == ['16', '2', '18']
    assert segments[2].eng_nums == ['18', '2', '18']
    assert segments[2].missing_nums == {'16': 1}
    assert segments[2].extra_nums == {'18': 1}
    assert segments[2].error_found is True
    assert segments[3].jap_nums == ['14', '36', '38', '14', '40', '14', '42']
    assert segments[3].eng_nums == ['15', '36', '36', '14', '40', '16', '42']
    assert segments[3].missing_nums == {'38': 1, '14': 2}
    assert segments[3].extra_nums == {'15': 1, '36': 1, '16': 1}
    assert segments[3].error_found is True
    assert segments[4].jap_nums == []
    assert segments[4].eng_nums == []
    assert segments[4].missing_nums == {}
    assert segments[4].extra_nums == {}
    assert segments[4].error_found is False


def test_ending_punctuation_check(segments):
    punctuation.ending_punctuation_check(segments)
    assert segments[0].trailing_punctuation_error is False
    assert segments[1].trailing_punctuation_error is True
    assert segments[2].trailing_punctuation_error is True
    assert segments[3].trailing_punctuation_error is False
    assert segments[4].trailing_punctuation_error is True


def test_unpaired_symbol_check(segments):
    unpaired.unpaired_symbol_check(segments)
    assert segments[0].unpaired_symbols == ['()', '[]']
    assert segments[0].unpaired_symbol_found is True
    assert segments[0].error_found is True
    assert segments[1].unpaired_symbols == []
    assert segments[1].unpaired_symbol_found is False
    assert segments[1].error_found is False
    assert segments[2].unpaired_symbols == ['{}']
    assert segments[2].unpaired_symbol_found is True
    assert segments[2].error_found is True
    assert segments[3].unpaired_symbols == ['()']
    assert segments[3].unpaired_symbol_found is True
    assert segments[3].error_found is True
    assert segments[4].unpaired_symbols == []
    assert segments[4].unpaired_symbol_found is False
    assert segments[4].error_found is False


def test_single_word_check(segments):
    repeaters.single_word_check(segments)
    assert segments[0].error_found is False
    assert segments[0].repeated_word_found is False
    assert segments[0].repeated_words == []
    assert segments[1].error_found is True
    assert segments[1].repeated_word_found is True
    assert segments[1].repeated_words == ['with with']
    assert segments[2].error_found is True
    assert segments[2].repeated_word_found is True
    assert segments[2].repeated_words == ['a a']
    assert segments[3].error_found is False
    assert segments[3].repeated_word_found is False
    assert segments[3].repeated_words == []
    assert segments[4].error_found is True
    assert segments[4].repeated_word_found is True
    assert segments[4].repeated_words == ['the the']


def test_double_word_check(segments):
    repeaters.double_word_check(segments)
    assert segments[0].error_found is False
    assert segments[0].repeated_word_found is False
    assert segments[0].repeated_words == []
    assert segments[1].error_found is True
    assert segments[1].repeated_word_found is True
    assert segments[1].repeated_words == ['in the in the']
    assert segments[2].error_found is False
    assert segments[2].repeated_word_found is False
    assert segments[2].repeated_words == []
    assert segments[3].error_found is False
    assert segments[3].repeated_word_found is False
    assert segments[3].repeated_words == []
    assert segments[4].error_found is True
    assert segments[4].repeated_word_found is True
    assert segments[4].repeated_words == ['of the of the']


def test_consecutive_space_check(segments):
    spaces.consecutive_space_check(segments)
    spaces.leading_space_check(segments)
    spaces.trailing_space_check(segments)
    assert segments[0].consecutive_space_found is True
    assert segments[0].leading_space_found is False
    assert segments[0].trailing_space_found is False
    assert segments[0].error_found is True
    assert segments[1].consecutive_space_found is True
    assert segments[1].leading_space_found is False
    assert segments[1].trailing_space_found is False
    assert segments[1].error_found is True
    assert segments[2].consecutive_space_found is False
    assert segments[2].leading_space_found is False
    assert segments[2].trailing_space_found is True
    assert segments[2].error_found is True
    assert segments[3].consecutive_space_found is False
    assert segments[3].leading_space_found is True
    assert segments[3].trailing_space_found is True
    assert segments[3].error_found is True
    assert segments[4].consecutive_space_found is False
    assert segments[4].leading_space_found is True
    assert segments[4].trailing_space_found is False
    assert segments[4].error_found is True


def test_untranslated_check(segments):
    untranslated.untranslated_check(segments)
    assert segments[5].untranslated_seg is True
    assert segments[5].error_found is True
