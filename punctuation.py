# -*- coding: utf-8 -*-


def ending_punctuation_check(segments):
    '''
    Function for checking if the source and target text
    end with the same punctuation.
    '''

    # List of Japanese punctuation marks
    jap_punc = ['\u3001', '\u002C', '\uFF0C', '\uFF64', '\u3002',
                '\u002E', '\uFF0E', '\uFF61', '\uFF09', '\uFF60',
                '\uFF3D', '\uFF5D', '\u3015', '\u3017', '\u3011',
                '\u3019', '\u301B', '\u3009', '\u300B', '\u300D',
                '\u300F', '\u301C', '\uFF5E', '\u2026', '\u0029',
                '\u005D', '\u003E', '\u0022']

    # Dict of Japanese punctuation marks and
    # the corresponding English punctuation marks
    corresponding_punc = {'\u3001': '\u002C', '\u002C': '\u002C',
                          '\uFF0C': '\u002C', '\uFF64': '\u002C',
                          '\u3002': '\u002E', '\u002E': '\u002E',
                          '\uFF0E': '\u002E', '\uFF61': '\u002E',
                          '\uFF09': '\u0029', '\uFF60': '\u0029',
                          '\u0029': '\u0029', '\uFF3D': '\u005D',
                          '\uFF5D': '\u005D', '\u3015': '\u005D',
                          '\u3017': '\u005D', '\u3011': '\u005D',
                          '\u3019': '\u005D', '\u301B': '\u005D',
                          '\u005D': '\u005D', '\u3009': '\u003E',
                          '\u003E': '\u003E', '\u300B': '\u003E',
                          '\u300D': '\u0022', '\u0022': '\u0022',
                          '\u300F': '\u0022', '\u301C': '\u2026',
                          '\uFF5E': '\u2026', '\u2026': '\u2026'}

    for segment in segments:

        # Only proceed if there is target text.
        if segment.target_text:

            # Only proceed if there is text to check (REQUIRED?)
            if not segment.source_text.isspace() and \
               not segment.target_text.isspace():

                source_text = segment.source_text.strip()
                target_text = segment.target_text.strip()
                last_source_char = source_text[-1]

                if last_source_char in jap_punc:
                    last_target_char = target_text[-1]

                    # Compare trailing punctuation between Jap and Eng
                    # (these should correspond)
                    corresponding_eng = corresponding_punc[last_source_char]
                    if last_target_char != corresponding_eng:
                        segment.trailing_punctuation_error = True

    return segments
