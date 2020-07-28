# Expert Evs

## Introduction
This is a program that can maximize the total bulk of a pokemon given a specific number of EVs. The program uses webscraper to get the base stats of a certain pokemon if it cannot find in the attached dictionary. 

## Usage
python main.py 

usage: main.py [-h] [-p POKEMON] [-d DISPOSABLE] [-n NATURE] [-pw PHYS_WEIGHT]
[-pm PHYS_MODIFIER] [-sm SPEC_MODIFIER] [-m METHOD]

| argument | full argument   | explanation                                  | optional               |
|----------|-----------------|----------------------------------------------|------------------------|
| -h       | --help          | show this help message and exit              | No                     |
| -p       | --pokemon       | Select the pokemon you want to EV            | Yes                    |
| -d       | --disposable    | The EVs to be used in the optimisation       | No, default to be 510  |
| -n       | --nature        | whether or not to allow nature modifier      | No, default to be true |
| -pw      | --phys_weight   | physical weight of the bulk of the pokemon   | No, default to be 0.5  |
| -pm      | --phys_modifier | modifier of the physical bulk of the pokemon | No, default to be 1.0  |
| -sm      | --spec_modifier | modifier of the special bulk of the pokemon  | No, default to be 1.0  |
| -m       | --method        | either Chinese method or smogon method       | No, default to be "c"  |

## Requirement
* Python3
* BeautifulSoup4
 
