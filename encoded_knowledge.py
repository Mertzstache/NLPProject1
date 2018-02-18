
from util import remove_stopwords

STOP_WORDS = [
'for',
'in',
'-',
'–',
'or',
'a'
]

NON_CAPPED = [
'at', 'by', 'for', 'from', 'in', 'into', 
'of', 'off', 'on', 'onto', 'to', 'with',
'and', 'as', 'but', 'for', 'if', 'nor', 'once', 
'or', 'so', 'than', 'that', 'till', 'when', 'yet'
]

AWARD_NAMES_MOTION_PICTURE = [
'Best Motion Picture – Drama', 
'Best Motion Picture – Musical or Comedy',
'Best Director',
'Best Actor – Motion Picture Drama',
'Best Actor – Motion Picture Musical or Comedy',
'Best Actress – Motion Picture Drama',
'Best Actress – Motion Picture Musical or Comedy',
'Best Supporting Actor – Motion Picture',
'Best Supporting Actress – Motion Picture',
'Best Screenplay',
'Best Original Score',
'Best Original Song',
'Best Foreign Language Film',
'Best Animated Feature Film',
'Cecil DeMille Award for Lifetime Achievement in Motion Pictures'
]


AWARD_NAMES_TELEVISION = [
'Best Drama Series',
'Best Comedy Series',
'Best Actor in a Television Drama Series',
'Best Actor in a Television Comedy Series',
'Best Actress in a Television Drama Series',
'Best Actress in a Television Comedy Series',
'Best Limited Series or Motion Picture made for Television',
'Best Actor in a Limited Series or Motion Picture made for Television',
'Best Actress in a Limited Series or Motion Picture made for Television',
'Best Supporting Actor in a Series, Limited Series or Motion Picture made for Television',
'Best Supporting Actress in a Series Limited Series or Motion Picture made for Television'
]


ALL_AWARDS = AWARD_NAMES_MOTION_PICTURE + AWARD_NAMES_TELEVISION
ALL_AWARDS_LOWER = [award_name.lower().split() for award_name in ALL_AWARDS]
ALL_AWARDS_LOWER_FILTERED = [remove_stopwords(award_name, STOP_WORDS) for award_name in ALL_AWARDS_LOWER]

