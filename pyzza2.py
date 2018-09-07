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
    totalWeight = 0
    print('flour'.title().ljust(lWidth, '.') + flour.rjust(rWidth))
    for i, amount in style.items():
        print(i.title().ljust(lWidth, '.') + str(style[i]).rjust(rWidth))
        totalWeight = totalWeight + amount
    print('\n')

    # sum the total weight of the ingredients and divide by 260g
    # to get the amount of pies
    totalWeight = totalWeight + int(flour)
    pies = round(totalWeight / 260)
    print('That should be enough for ' + str(pies) + ' pies (' +
            str(round(totalWeight / pies)) + 'g each)')

completer = autoComplete(recipes.keys())
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

choice = ''
while not choice.isdigit() or choice not in recipes:
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
    choice = input('> ').lower()
    if choice.isdigit():
        flour = choice
        print("\n")
        print("DOPNY".center(19, '_'))
        printTable(bakerCalc(flour))
    elif choice in recipes:
        flour = ''
        while not flour.isdigit():
            flour = input('Type the desired amount of flour: ')
        print("\n")
        print((choice.upper().center(19, '_')))
        printTable(bakerCalc(flour, recipes[choice]))
    elif choice == 'exit' or choice in 'quit':
        print('Bye!')
    sys.exit()

# TODO
# implement biga, poolish and starter
