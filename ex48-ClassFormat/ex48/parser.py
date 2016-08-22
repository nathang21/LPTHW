class Sentence(object):
    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

class PareserError(Exception):
    pass


class Parse(object):
    def __init__(self):
        pass

    def peek(self, word_list):
        if word_list:
            word = word_list[0]

            #if word[0] != 'stop' or 'noun' or 'verb' or 'direction':
            ##    return temp[0]

            return word[0]
        else:
            return None

    def match(self, word_list, expecting):
        if word_list:
            word = word_list.pop(0)

            if word[0] == expecting:
                return word
            else:
                return None

        else:
            return None

    def skip(self, word_list, word_type):
        #word = word_list[0]

        if self.peek(word_list) not in ('stop', 'noun', 'verb', 'direction'):
            self.match(word_list, word_list[0])

        while self.peek(word_list) == word_type:
            self.match(word_list, word_type)

    def parse_verb(self, word_list):
        #self.skip(word_list, 'stop')
        #next_word = self.peek(word_list)
        #while next_word != 'verb':
        self.skip(word_list, 'stop')


        while len(word_list) > 0 and self.peek(word_list) != 'verb':
                self.match(word_list, word_list[0])

        return self.match(word_list, 'verb')

    def parse_object(self, word_list):
        self.skip(word_list, 'stop')
        #   next_word = self.peek(word_list)
        #while next_word != 'noun' or 'direction':
        #self.skip(word_list, 'stop')
        next_word = self.peek(word_list)

        while len(word_list) > 0 and self.peek(word_list) not in ('noun', 'direction'):
                self.match(word_list, word_list[0])

        if next_word == 'noun':
            return self.match(word_list, 'noun')
        elif next_word == 'direction':
            return self.match(word_list, 'direction')
        else:
            raise PareserError("Expected a noun or direction next.")
            #return self.skip(word_list, 'stop')

    def parse_subject(self, word_list):
        self.skip(word_list, 'stop')
        next_word = self.peek(word_list)

        if next_word == 'noun':
            return self.match(word_list, 'noun')
        elif next_word in ('verb', 'noun', 'direction'):
            return ('noun', 'player')
        else:
            raise PareserError("Expected a verb next.")
            #return self.skip(word_list, 'stop')

    def parse_sentence(self, word_list):
        subj = self.parse_subject(word_list)

        verb = self.parse_verb(word_list)

        obj = self.parse_object(word_list)

        print subj, verb, obj
        return Sentence(subj, verb, obj)
