#!/usr/bin/python3
from typing import Union, Dict
FlatRecipe = Dict[str, Union[float, int]]
Recipe = Dict[str, Union[float, int, FlatRecipe]]

def bakerCalc(flour: int, style: Recipe) -> FlatRecipe:
    workingRecipe = {'flour': float(flour)}
    for i in style.keys():
        if i == "starter":
            mult = int(totalWeight(style["starter"]))
            i = "preferment"
        else:
            mult = style[i]
        workingRecipe[i] = float(flour) * mult / 100
    return workingRecipe


def dividePies(totalWeight: float, pieWeight: int) -> (float, float):
    pies = round(totalWeight / (pieWeight if pieWeight else 260))
    eachPie = round(totalWeight / pies)
    return pies, eachPie


def totalWeight(recipe: FlatRecipe) -> float:
    return sum(recipe.values())
