# Autocomplete, given a word you're predicting the next wod that comes after it.
# predict function, train function ( array of string ) [['I', 'am', 'michael'], ['I', 'am', 'razzaq'], ['I', 'love', 'london']]
# example:
# corposu = {"I": {"am": 2, "love": 1}, "am": {"michael": 1, "razzaq": 1}, "love": {"london": 1}}
import heapq


class Autocomplete:
    def __init__(self):
        self.weights = {}

    def predict(self, word):
        if word not in self.weights:
            return ""
        else:
            return self.weights[word]

    def train(self, training_data_set):
        for data in training_data_set:
            for index, word in enumerate(data):
                if index + 1 == len(data):
                    break
                next_word = data[index + 1]
                if word in self.weights:
                    value = self.weights[word]
                    value = value.get(next_word, 0) + 1
                    self.weights[word] = value
                else:
                    self.weights[word] = {next_word: 1}

        for key, val in self.weights:
            predictions = self.weights[key]
            most_freq = 0
            result = ""
            for key1, val1 in predictions:
                if val1 > most_freq:
                    most_freq = val1
                    result = key
            self.weights[key] = result

# weights = {'I': {'am': 1}, 'am': {'michael': 1}}
# data = ['I', 'am', 'michael']
# index = 1
# word = am
# len = 3
# next_word = 'michael'
