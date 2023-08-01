import requests
from pick import pick
from colorama import Fore, Style

r = requests.get("https://api.publicapis.org/entries").json()
pubapis = r["entries"]
categories = list()
for pubapi in pubapis:
    categories.append(pubapi["Category"])

categories = list(dict.fromkeys(categories))
category, index = pick(categories, "Select category: ")

for pubapi in pubapis:
    if category == pubapi["Category"]:
        print(
            f"{Style.DIM}Name:{Style.RESET_ALL} {Fore.LIGHTGREEN_EX}{pubapi['API']}{Style.RESET_ALL}\n"
            f"{Style.DIM}Discription:{Style.RESET_ALL} {Fore.LIGHTYELLOW_EX}{pubapi['Description']}{Style.RESET_ALL}\n"
            f"{Style.DIM}Link:{Style.RESET_ALL} {Fore.LIGHTBLUE_EX}{pubapi['Link']}{Style.RESET_ALL}\n"
            f"{Style.DIM}Category:{Style.RESET_ALL} {pubapi['Category']}{Style.RESET_ALL}"
            )
        print(Style.RESET_ALL)