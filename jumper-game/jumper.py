import random
class Jumper:
    
    def __init__(self):
        self.word = words
        self.guess = []
        #self.word = [self.words.word(self)]
        self.lives = 4
        self.won = False
        self.lose = False
        #letter = input("Guess a letter [a - z]: ")
        #print(f"[][][][][]")
        #print([])
        #print([])
        #print([])
        #print([])
        #print([])
        #From 9 to 14 is the part of the body.
        #we can create an empty list containing 
    def letter_check(self):
        '''Verify's the word contains the letter'''
        for i in range (0, len(self.word)):
            letter = self.word[i]
            if self.guess == letter:
                self.reveal[i] = self.guess 
        if '_' not in self.reveal:
            return True
        else:
            return False
    #body_list = ["----", "/     \", " ------"]
    #body_list.pop
    def show(self):
        '''Shows the picture and it changes it depending on the lives count'''
        pass
    
    def process(self):
        '''Guessing the Logic of the game'''
        pass