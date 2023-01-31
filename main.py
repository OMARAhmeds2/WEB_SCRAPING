import requests  # to get the website OR to make a request to the website
from bs4 import BeautifulSoup
import csv

date = input("Please enter a Date in the following format MM/DD/YY: ")

page = requests.get(f"https://www.yallakora.com/Match-Center/?date={date}")


def main(page):
    src = page.content  # `content` method is return the content of the page in `byte code`
    soup = BeautifulSoup(src, "lxml")

    matches_details = []

    championships = soup.find_all(
        "div", {"class": "matchCard"})  # it will return list

    def get_match_info(championships):
        championship_title = championships.contents[1].find("h2").text.strip()  # it will return `كأس العالم`
        # in the following code `*.find_all` -> it's an list that contains alot of values and each value is a code
        all_matches = championships.contents[3].find_all("li")
        number_of_matches = len(all_matches)

        for i in range(number_of_matches):
            # get teams names
            team_A = all_matches[i].find("div", {"class": "teamA"}).text.strip()
            print(team_A)

    # championships is a list
    get_match_info(championships[0])


main(page)
