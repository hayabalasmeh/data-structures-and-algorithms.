from data_structures_algorth.challenge_brackets.stack_brackets import brackets_checker

## 1- checking one pair closing
def test_one_pair():
     actual = brackets_checker('{}')
     expected = True

     assert actual == expected


## 2- checking three pairs

def test_three_pair():
     actual = brackets_checker('{}()[]')
     expected = True

     assert actual == expected


## 3- Checking extra characters:

def test_extra_pair():
     actual = brackets_checker('()[[Extra Characters]]')
     expected = True

     assert actual == expected


## 4- checking multiple pairs inside each other

def test_multiple_pair():
     actual = brackets_checker('(){}[[]]')
     expected = True

     assert actual == expected
     


## 5- checking multiple strings inside

def test_string_pair():
     actual = brackets_checker('{}{Code}[Fellows](())')
     expected = True

     assert actual == expected


## 6- checking one missing closing

def test_missing_closing():
     actual = brackets_checker('[({}]')
     expected = False

     assert actual == expected


def test_missing():
     actual = brackets_checker('(]()')
     expected = False

     assert actual == expected

def test_missing_opening():
     actual = brackets_checker('{(})')
     expected = False

     assert actual == expected
   