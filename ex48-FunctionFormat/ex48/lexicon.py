direction = ('north', 'south', 'east', 'west', 'up', 'down', 'left', 'right')
verb = ('go', 'stop', 'kill', 'eat')
stop = ('the', 'of', 'in', 'from', 'at', 'it')
noun = ('door', 'bear', 'princess', 'cabinet')

def scan(sentence):
    # Take in string, and match to dictionary commands in
    words = sentence.split()
    return [get_tuple(word) for word in words]

def get_tuple(word):
    input = word.lower()
    if input in direction:
        return ('direction', word)
    elif input in verb:
        return ('verb', word)
    elif input in stop:
        return ('stop', word)
    elif input in noun:
        return ('noun', word)
    elif input.isdigit():
        try:
            return ('number', int(word))
        except ValueError:
            return None
    else:
        return ('error', word)
