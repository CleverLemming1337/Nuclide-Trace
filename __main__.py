import json
from Interactions import *

with open("data.json", "r") as f:
    data = json.load(f)

chart = dict(dict())
for i in data:
    i.update( { 'm': i['z'] + i['n'] } ) # TODO: Put this into data file
    i['life'] = float(i['life']) if i['life'].strip() else 0.0
    if i['z'] not in chart:
        chart.update( { i['z']: { i['n']: i } } )
    else:
        chart[i['z']].update( { i['n']: i } )

z = IntInput("Enter number of protons")
n = IntInput("Enter number of neutrons: ") if TextInput("Search by number of neutrons (N) or by mass number (M)").lower() == "n" else IntInput("Enter mass number")-z 

isotope = chart[z][n]

COLORS = {
    "A": "3",
    "B-": "4",
    "B+": "1",
    "EC+B+": "1",
    "P": "6",
    "N": "5",
    "SF": "2",    
    "S": "9",
}

def print_nuclide(nuclide: dict) -> str:
    color = COLORS[nuclide['mode']] if nuclide['mode'] in COLORS else "9"

    result = f"\033[9{color}m"
    
    result += f"{nuclide['name']:<2} {nuclide['m']:>3} {nuclide['z']:>3} {nuclide['mode']:<5}" + (f"{nuclide['life']:30,.10f}" if nuclide['life'] else "")+"\033[0m"
    return result

def trace_nuclide(nuclide: dict) -> list[str]:
    if nuclide['mode'] == "S":
        return [print_nuclide(nuclide)]
    if nuclide['mode'] == "A":
        x = -2
        y = -2
    elif nuclide['mode'] == "B-":
        x = -1
        y = 1
    elif nuclide['mode'] == "EC+B+":
        x = 1
        y = -1
    elif nuclide['mode'] == "N":
        x = -1
        y = 0
    elif nuclide['mode'] == "P":
        x = 0
        y = -1
    else:
        return [print_nuclide(nuclide)]
    new_nuclide = chart[nuclide['z']+y][nuclide['n']+x]
    return [print_nuclide(nuclide), *trace_nuclide(new_nuclide)]    

nuclide = chart[z][n]

trace = trace_nuclide(nuclide)
print(f"{len(trace)} Steps:")

for index, step in enumerate(trace):
    print(f"{index+1:>3}. {step}")
