from random import choice
import string

def random_weighted_choice(arr, weights):
    weighted_arr = []
    for i in range(len(arr)):
        to_append = arr[i]
        for j in range(weights[i]):
            weighted_arr.append(to_append)
    return choice(weighted_arr)

class MarkovChain:
    def __init__(self):
        self.graph = {"": {}}
        
    def populate_chain(self, inFile, n):
        previous_word = ""
        with open(inFile, "r") as f:
            lines = f.readlines()
            for line in lines:
                words = line.strip().split(" ")
                words = [" ".join(words[i: i + n]) for i in range(len(words) - (n - 1))]
                for word in words:
                    word = word.lower()
                    word = word.translate(str.maketrans('', '', string.punctuation))
                    if word not in self.graph.keys():
                        self.graph[word.lower()] = {}
                    if word not in self.graph[previous_word].keys():
                        self.graph[previous_word][word] = 0
                    self.graph[previous_word][word] += 1
                    previous_word = word


    def next_word(self, seed_word):
        return random_weighted_choice(list(self.graph[seed_word].keys()), list(self.graph[seed_word].values()))

