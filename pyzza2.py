#!/usr/bin/python3
import sys
import json

with open('recipes.json', 'r') as f:
    recipes = json.load(f)


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


def gen_nav_list(recipes_dict, reserved_words_list):
    return list(recipes_dict.keys()) + reserved_words_list


def calc_autocomp(auto_list, choice_str):
    if len(choice_str) > 0:
        return list(filter(lambda auto_str: auto_str.startswith(choice_str), auto_list))
    return []


autocomp_list = gen_nav_list(recipes, ['recipes', 'exit', 'quit'])

choice = ''
while not choice.isdigit() or choice not in recipes:
    print("Type a number or 'recipes':")
    choice = input('> ').lower()
    
    # if autocomplete is triggered
    auto_choices = calc_autocomp(autocomp_list, choice)
    if len(auto_choices) == 1:
        choice = auto_choices[0]
    
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
