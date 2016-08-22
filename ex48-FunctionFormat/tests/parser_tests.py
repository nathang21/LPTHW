from nose.tools import *
from py.test import *
from ex48 import parser

def test_peek():
    #assert_raises(PareserError, peek, ['direction', ''])
    pass

def test_match():
    pass
def test_skipt():
    pass
def test_parse_verb():
    pass

def test_parse_object():
    pass
def test_parse_subject():
    pass

def test_parse_sentence():
    assert_raises(parser.PareserError, parser.parse_sentence, [('stop', 'yo'), ('direction', 'sup',), ('noun', 'north'), ('direction' 'north'), ('sdhaf', 'sdfhsd'), ('stop', 'sfgfd'), ('noun', 'Nate'), ('sdf', 'stop'),
    ('verb', 'hunt'), ('dsf', 'sfds'), ('stop', 'sdfgsf'), ('noun', 'south'), ('stop', 'nbd'), ('sefg', 'dsfsdfg')])

    parser.parse_sentence([('stop', 'yo'), ('verb', 'hunt'), ('stop', 'sdfgsf'), ('noun', 'south'), ('stop', 'nbd'), ('sefg', 'dsfsdfg')])
