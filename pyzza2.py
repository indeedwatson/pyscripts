#!/usr/bin/python3
import sys
import json
import readline

with open('recipes.json', 'r') as f:
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


def bakerCalc(flour, style=recipes['masterdough']):
    """ Take an amount of flour and calculate the rest of the ingredients
    Defaults to masterdough if no recipe is specified
    """
    workingRecipe = {}
    for i in style.keys():
        ingredient = int(flour) * int(style[i]) / 100
        workingRecipe[i] = ingredient
    return workingRecipe


def printTable(style):
    """ Make a neat table to print the ingredients """

    lWidth = 12
    rWidth = 7
    # was trying to print the title of the recipe but I can't figure it out
    # print(str(style.keys).upper().center(lWidth + rWidth, '-'))
    print('\n')
    print('flour'.title().ljust(lWidth, '.') + flour.rjust(rWidth))
    for i in style.keys():
        print(i.title().ljust(lWidth, '.') + str(style[i]).rjust(rWidth))
    print('\n')


completer = autoComplete(recipes.keys())
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

choice = ''
while not choice.isdigit() or choice not in recipes:
    for r in recipes:
        alignedRows = "{:^15} {:^15} {:^15}".format(*r)
        print(alignedRows)
    print("Type a number or 'recipes':")
    choice = input('> ').lower()
    if choice.isdigit():
        flour = choice
        workingRecipe = bakerCalc(flour)
        printTable(workingRecipe)
    elif choice in recipes:
        flour = ''
        while not flour.isdigit():
            flour = input('Type the desired amount of flour: ')
        workingRecipe = bakerCalc(flour, recipes[choice])
        printTable(workingRecipe)
    elif choice == 'recipes':
        print('\n')
        for r in recipes.keys():
            print(r)
        print('\n')
    elif choice == 'exit' or choice == 'quit':
        print('Bye!')
        sys.exit()

# TODO
# tab autocompletion
# add recipes
# print recipes in columns
