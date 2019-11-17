# -*- coding: utf-8 -*-


def ending_punctuation_check(segments):
    '''
    Function for checking if the source and target text
    end with the same punctuation.
    '''

    '''
    Dict of ending punctuation marks that could appear in Japanese text.
    Key: Japanese punctuation mark
    Value: Corresponding English punctuation mark
    '''
    punc_marks = {'\u3001': '\u002C',  # 、 ideographic comma
                  '\u002C': '\u002C',  # , comma
                  '\uFF0C': '\u002C',  # ， fullwidth comma
                  '\uFF64': '\u002C',  # ､ halfwidth ideographic comma
                  '\u3002': '\u002E',  # 。 ideographic full stop
                  '\u002E': '\u002E',  # . full stop
                  '\uFF0E': '\u002E',  # ． fullwidth full stop
                  '\uFF61': '\u002E',  # ｡ halfwidth ideographic full stop
                  '\uFF09': '\u0029',  # ） fullwidth right parenthesis
                  '\uFF60': '\u0029',  # ｠ fullwidth right white parenthesis
                  '\u0029': '\u0029',  # ) right parenthesis
                  '\uFF3D': '\u005D',  # ］ fullwidth right square bracket
                  '\u3015': '\u005D',  # 〕 right tortoise shell bracket
                  '\u3017': '\u005D',  # 〗 right white lenticular bracket
                  '\u3011': '\u005D',  # 】 right black lenticular bracket
                  '\u3019': '\u005D',  # 〙 right white tortoise shell bracket
                  '\u301B': '\u005D',  # 〛 right white square bracket
                  '\u005D': '\u005D',  # ] right square bracket
                  '\uFF5D': '\u7D00',  # ｝ fullwidth right curly bracket
                  '\u3009': '\u3E00',  # 〉 right angle bracket
                  '\u300B': '\u3E00',  # 》 right double angle bracket
                  '\u300D': '\u0022',  # 」 right corner bracket
                  '\u300F': '\u0022',  # 』 right white corner bracket
                  '\u301C': '\u2620',  # 〜  wave dash
                  '\uFF5E': '\u2620',  # ～ fullwidth tilde
                  '\u2026': '\u2620',  # … horizontal ellipsis
                  '\u003E': '\u3E00',  # > greater-than sign
                  '\u0022': '\u0022',  # " quotation mark
                  '\u0027': '\u0027'}  # ' apostraphe mark

    for segment in segments:

        # Only proceed if there is source and target text.
        if segment.source_text and segment.target_text:

            # Strip trailing whitespace if any
            source_text = segment.source_text.rstrip()
            target_text = segment.target_text.rstrip()

            last_source_char = source_text[-1]

            if last_source_char in punc_marks:

                # Compare trailing punctuation between Jap and Eng
                last_target_char = target_text[-1]
                corresponding_mark = punc_marks[last_source_char]

                if last_target_char != corresponding_mark:
                    segment.trailing_punctuation_error = True

    return segments
