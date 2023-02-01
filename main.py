import requests  # to get the website OR to make a request to the website
from bs4 import BeautifulSoup
import csv

date = input("Please enter a Date in the following format MM/DD/YY: ")

page = requests.get(f"https://www.yallakora.com/Match-Center/?date={date}")


def main(page):
    src = page.content  # `content` method is return the content of the page in `byte code`
    soup = BeautifulSoup(src, "lxml")
    matches_details = []

    championships = soup.find_all("div", {"class": "matchCard"})  # it will return list

    def get_match_info(championships):
        championship_title = championships.contents[1].find("h2").text.strip()  # it will return `كأس العالم`
        # in the following code `*.find_all` -> it's an list that contains alot of values and each value is a code
        all_matches = championships.contents[3].find_all("li")
        number_of_matches = len(all_matches)

        for i in range(number_of_matches):
            # get teams names
            team_A = all_matches[i].find("div", {"class": "teamA"}).text.strip()
            team_B = all_matches[i].find("div", {"class": "teamB"}).text.strip()
            
            # get the score
            match_result = all_matches[i].find("div", {"class": "MResult"}).find_all("span", {"class": "score"})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            match_time = all_matches[i].find("div", {"class": "MResult"}).find("span", {"class": "time"}).text.strip()

            # add matches info into `match_details` "Variable"
            matches_details.append({ "Champion Type": championship_title, "TeamA": team_A, "TeamB": team_B, "Time": match_time, "Result": score})


    # championships is a list
    # here we can get all the championships
    for i in range(len(championships)):
        get_match_info(championships[i])
    
    keys = matches_details[0].keys()
    
    with open("matches-details.csv", "w") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        
        print("file created.")



main(page)
