#!/usr/bin/python3
import sys

# dough recipes in baker's percentage
recipes = {'neapolitan': {'water': 70, 'salt': 3, 'yeast': 1},
           'masterdough': {'water': 68, 'salt': 3, 'yeast': 1.5, 'oil': 2,
           'sugar': 1},
           'chicago': {'water': 60, 'salt': 2, 'yeast': 0.1, 'lard': 1,
                       'butter': 1},
           'sicilian': {'water': 70, 'salt': 2, 'yeast': 1, 'malt': 2,
                        'oil': 1},
           'refrigerated': {'water': 70, 'salt': 2.6, 'yeast': 0.3},
           'tortilla': {'lard': 20, 'water': 70, 'salt': 2},
           'serious eats neapolitan': {'water': 65, 'salt': 2, 'IDY': 1.5},
           'serious eats NY': {'water': 67, 'sugar': 2, 'salt': 1.5,
           'olive oil': 5}}



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

choice = ''

while not choice.isdigit() or choice not in recipes:
    print("Type a number or 'recipes':")
    choice = input('> ').lower()
    if choice.isdigit():
        workingRecipe = bakerCalc(choice)
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
