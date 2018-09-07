#!/usr/bin/python3
import sys
import json
import readline

with open('./recipes.json', 'r') as f:
    recipes = json.load(f)


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


def bakerCalc(flour, style=recipes['dopny']):
    """ Take an amount of flour and calculate the rest of the ingredients
    Defaults to dopny if no recipe is specified
    """
    workingRecipe = {}
    for i in style.keys():
        ingredient = float(flour) * float(style[i]) / 100
        workingRecipe[i] = ingredient
    return workingRecipe


def printTable(style):
    """ Make a neat table to print the ingredients """

    lWidth = 12
    rWidth = 7
    totalIngredients = 0
    # was trying to print the title of the recipe but I can't figure it out
    # print(str(style.keys).upper().center(lWidth + rWidth, '-'))
    print('\n')
    print('flour'.title().ljust(lWidth, '.') + flour.rjust(rWidth))
    for i, amount in style.items():
        print(i.title().ljust(lWidth, '.') + str(style[i]).rjust(rWidth))
        totalIngredients = totalIngredients + amount
    print('\n')
    totalIngredients = totalIngredients + int(flour)
    
    pies = round(totalIngredients / 260)
    print('That should be enough for ' + str(pies) + ' pies (' +
            str(round(totalIngredients / pies)) + ' each)')

completer = autoComplete(recipes.keys())
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

choice = ''
while not choice.isdigit() or choice not in recipes:
    print("Choose a recipe:\n")
    indx = 1
    while indx < len(recipes):
        for r in recipes.keys():
            if indx % 3 == 0:
                print(str(indx) + '.', r)
            else:
                print(str(indx) + '.', r.title().ljust(18, ' '), end=' ')
            indx = indx + 1
    print("\nOr enter the desired amount of flour:\n")
    choice = input('> ').lower()
    if choice.isdigit():
        flour = choice
        printTable(bakerCalc(flour))
    elif choice in recipes:
        flour = ''
        while not flour.isdigit():
            flour = input('Type the desired amount of flour: ')
        workingRecipe = bakerCalc(flour, recipes[choice])
        printTable(workingRecipe)
    elif choice == 'exit' or choice == 'quit':
        print('Bye!')
        continue
    sys.exit()

# TODO
# tab autocompletion
# add recipes
# print recipes in columns
