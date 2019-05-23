#!/usr/bin/python3
from bakerMath import dividePies, totalWeight
from tabulate import tabulate
from typing import List, Dict, Union, Callable
import readline
import sys

FlatRecipe = Dict[str, Union[float, int]]
Recipe = Dict[str, Union[float, int, FlatRecipe]]

class Cli:
    def __init__(self, recipes: Recipe):
        self.recipes = recipes

    def printPies(self, total: float) -> str:
        completer = autoComplete(self.recipes.keys())
        readline.set_completer(completer.complete)
        readline.parse_and_bind('tab: complete')

        print("Weight of each pie or loaf: ")
        pieWeight = float(self.makeChoice(self.getWeight(), [lambda pieWeight: 
            pieWeight.isdigit() and total > int(pieWeight)]))
        pies, eachPie = dividePies(total, float(pieWeight))
        print(f"That should be enough for {str(pies)} pies, " \
                f"{str(eachPie)}g each.\n")

    def getWeight(self):
        "You're trying to make more dough than you make!"

    def getFlour(self):
        print("Type the desired amount of flour: ")

    def printRecipes(self) -> str:
        print("Choose a recipe")
        indx = 1
        # print recipes in 3 columns
        while indx < len(self.recipes):
            for r in self.recipes.keys():
                if indx % 3 == 0:
                    print(str(indx) + '.', r)
                else:
                    print(str(indx) + '.', r.title().ljust(18, ' '), end=' ')
                indx = indx + 1
        print("\nOr enter an amount of flour:")

    def makeChoice(self, func, conditions: List[Callable[[str], bool]]) -> str:
        validInput = False
        while not validInput:
            func
            choice = input('> ').lower()
            if choice == 'exit' or choice == 'quit' or choice == 'q':
                print('Bye, enjoy the pizza!\n')
                sys.exit()
            validInput = any(cond(choice) for cond in conditions)
        return choice


class autoComplete(object):

    def __init__(self, options):
        self.options = sorted(options)
        return

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches
                self.matches = [s for s in self.options
                                    if text in s]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try:
            return self.matches[state]
        except IndexError:
            return None


def printTable(ingredients: FlatRecipe) -> str:
    total = int(sum(ingredients.values()))
    table = []
    headers = ["Ingredient", "Amount", "%"]
    for k,v in ingredients.items():
        # re-calculate the % of each ingredient so it can be printed, truncating
        # at 2 decimal places
        percent = v * 100.0 / float(ingredients['flour'])
        percent = '{:.2f}'.format(percent)
        v = '{:.2f}'.format(v)
        table.append([k, v, percent])
    table.append(["TOTAL", total, None])
    print(tabulate(table, headers, numalign='right', tablefmt="github"))
    print('\n')
