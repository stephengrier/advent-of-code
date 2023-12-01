from solution import replace_number_words_with_digits

def test_replace_number_words_with_digits():
    assert replace_number_words_with_digits('one4twothree9fourfive') == 'o1e4t2ot3e9f4rf5e'
    assert replace_number_words_with_digits('six8seven3eightnine') == 's6x8s7n3e8tn9e'

def test_overlapping_number_words():
    assert replace_number_words_with_digits('eightwo') == 'e8t2o'
    assert replace_number_words_with_digits('twone') == 't2o1e'
