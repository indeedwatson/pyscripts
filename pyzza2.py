#!/usr/bin/python3
import json
from cli import Cli, printTable
from bakerMath import *

try:
    with open('./recipes.json', 'r') as f:
        recipes = json.load(f)
except IOError:
    print("There should be a `recipes.json` file in the same folder\nthis ", \
            "script was executed from.")

cli = Cli(recipes)

def main():
    choice = ""
    choice = cli.makeChoice(cli.printRecipes(), [lambda choice: choice.isdigit(), 
        lambda choice: choice in recipes])
    if choice.isdigit():
        flour = choice
        choice = "dopny"
    elif choice in recipes:
        flour = ''
        flour = cli.makeChoice(cli.getFlour(), [lambda flour: flour.isdigit()])
    print("\n================================================")
    print("#### %s\n"% choice.upper())
    if "starter" in recipes[choice]:
        print("##### Starter")
        printTable(bakerCalc(flour, recipes[choice]["starter"]))
        print("##### Final Dough")
    recipe = bakerCalc(flour, recipes[choice])
    total = totalWeight(recipe)
    printTable(recipe)
    cli.printPies(total)

    print("================================================\n")
    main()

if __name__ == "__main__":
    main()
