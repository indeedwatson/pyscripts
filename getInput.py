#!/usr/bin/python3
import sys
from pyzza2 import *


def printPies(ingredients):
    print("Weight of each pie: ")
    pieWeight = initChoice(printPies)
    #totalWeight = eachPie(totalCalc(recipe))
    totalWeight = totalCalc(ingredients)
    pies = eachPie(ingredients)
    #im so confused what's happening here and eachPie pls start over tomorrowsd
    sd
    sdf
    sdfsdfs
    print('That should be enough for ' + str(pies) + ' pies (' +
          str(round(totalWeight / pies)) + 'g each)\n')


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


def condition(param=''):
    if not param.isdigit() and param not in recipes:
        return True
    else:
        return False
