import random

class Game:
    zoo = """Today I went to the zoo. I saw a (adjective) (noun) jumping up and down in its tree. He (verb: past tense)(adverb) through the large tunnel that led to its (adjective) (noun). I got some peanuts and passed them through the cage to a gigantic gray(noun) towering above my head. Feeding that animal made me hungry. I went to get a (adjective) scoop of ice cream. It filled my stomach. Afterwards I had to(verb) (adverb) to catch our bus. When I got home I (verb past tense) my mom for a (adjective) day at the zoo."""

    valid = ["(adjective)", "(noun)", "(verb)", "(adverb)"]
    sentence = [zoo]

    def __init__(self):
        print("Welcome to the fun world of Mad Lib Madness :) \n")
        idx = random.randint(0, 2)
        temp = self.sentence[0]
        new = self.prepare(temp)
        print(new)
    
    def play(self):
        print("The game has started...")

    def prepare(self, sent):
        renewedSentence = sent.split(" ")
        return renewedSentence


instance = Game()