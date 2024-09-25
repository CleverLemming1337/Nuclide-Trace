import json

with open("data.json", "r") as f:
    data = json.load(f)

chart = dict(dict())
for i in data:
    i.update( { 'm': i['z'] + i['n'] } ) # TODO: Put this into data file
    if i['z'] not in chart:
        chart.update( { i['z']: { i['n']: i } } )
    else:
        chart[i['z']].update( { i['n']: i } )

z = int(input("Enter number of protons: "))
n = int(input("Enter number of neutrons: ")) if input("Search by number of neutrons (N) or by mass number (M)? ").lower() == "n" else int(input("Enter mass number: "))-z 

isotope = chart[z][n]

COLORS = {
    "A": "3",
    "B-": "4",
    "B+": "1",
    
    "S": "9",
}

def print_nuclide(nucilde: dict) -> None:
    color = COLORS[nuclide['mode']] if nuclide['mode'] in COLORS else "9"

    print("\033[1;3"+color+"m", end="")
    print(f"{nuclide['name']} {nuclide['m']} ({nuclide['mode']})"+"\033[0m")

print("You selected:")
nuclide = chart[z][n]
print_nuclide(nuclide)
