"""
You are given a class called Sentence , which takes a string such as 'hello world'. 
You need to provide an interface such that the indexer returns a flyweight that can be used to capitalize a particular word in 
the sentence.

Typical use would be something like:

sentence = Sentence('hello world')
sentence[1].capitalize = True
print(sentence)  # writes "hello WORLD"

"""

class Sentence:
    def __init__(self, plain_text:str):       
        self.words = plain_text.split(' ')
        self.tokens = {}

    def __getitem__(self, idx):
        if idx not in self.tokens:
            self.tokens[idx] = self.WordToken()
        return self.tokens[idx]

    def __str__(self):
        result = []
        for idx, word in enumerate(self.words):
            if idx  in self.tokens and self.tokens[idx].capitalize:
                result.append(word.upper())
            else:
                result.append(word)
        return ' '.join(result)    


        

    class WordToken:
        def __init__(self):
            self.capitalize = False
        

    


if __name__ == "__main__":
    sentence = Sentence('hello world')
    sentence[1].capitalize = True
    print(sentence) # res: 'hello WORLD'

