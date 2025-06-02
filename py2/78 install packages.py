import termcolor
import pyfiglet


# print(pyfiglet.figlet_format("Andrew Safwat"))
print(termcolor.colored(pyfiglet.figlet_format(
    "Andrew Safwat"), "red", attrs=["bold"]))
