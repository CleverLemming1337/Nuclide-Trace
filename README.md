# Nuclide Trace
This is a simple python program which tracks the decay of nuclides using the nuclide chart ([Orciument/nuclide-data](https://github.com/Orciument/nuclide-data/tree/main)).

Start the program by typing `python3 .`.

You will be asked for the number of protons. That's the same as the element number.
For instance, if you want to see the decay of **Uranium 232**, enter `92` because uranium has 92 protons.

Then you will be asked if you want to enter the number of neutrons of the mass number. If you type `M` for the mass number, enter `232` for U 232 because it has 232 neutrons+protons.
If you type `N` for the number of neutrons, you would enter `140` for U 232 because it has 140 neutrons.

Then you'll see the decay. It shows the element symbol, the mass number, the decay type and the half-life.

> [!WARNING]
> This script is still being developed so there may be errors.
> If you find one, please help me by reporting it creating an issue.

> [!WARNING]
> **Disclaimer**: I'm using [Orciumen's nuclide-data](https://github.com/Orciument/nuclide-data/tree/main), which uses the iaea.org API.
> The data may be out of date, wrong or incomplete.
> Use it at your own risk!
