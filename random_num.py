import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

number1 = random.randint(low, high) #randint vrne random število med ( , )
number2 = random.random() # random decimalo število
option = random.choice(options) # izbere element iz options
random.shuffle(cards) # premeša list

print(cards)