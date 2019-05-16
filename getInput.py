#!/usr/bin/python3
import sys
from pyzza2 import *


def printPies(total):
    print("Weight of each pie: ")
    pieWeight = float(initChoice(printPies))
    while total < pieWeight:
        print(f"Math is not my strong suit either,\n\
but if the recipe makes {int(total)}g of total dough\n\
you can't make a pie that's {int(pieWeight)}g!\n")
        pieWeight = float(initChoice(printPies))
    while pieWeight < 151:
        print(str(pieWeight) + "g is too small for a pizza! If you're on a diet take the \
                meal off and enjoy a good pizza of at least 150g dough") 
        pieWeight = float(initChoice(printPies))
    pies, eachPie = dividePies(total, pieWeight)
    print(f'That should be enough for {str(pies)} pies, {str(eachPie)}g each.\n')


def printRecipes():
    print("Choose a recipe")
    indx = 1
    # print recipes in 3 columns
    while indx < len(recipes):
        for r in recipes.keys():
            if indx % 3 == 0:
                print(str(indx) + '.', r)
            else:
                print(str(indx) + '.', r.title().ljust(18, ' '), end=' ')
            indx = indx + 1
    print("\nOr enter an amount of flour:")


def initChoice(func):
    invalidInput = condition()
    while invalidInput:
        func
        choice = input('> ').lower()
        if choice == 'exit' or choice == 'quit' or choice == 'q':
            print('Bye, enjoy the pizza!\n')
            sys.exit()
        invalidInput = condition(choice)
    return choice


def condition(param='') -> bool:
    if not param.isdigit() and param not in recipes:
        return True
    else:
        return False
