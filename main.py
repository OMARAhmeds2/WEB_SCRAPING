import requests  # to get the website OR to make a request to the website
from bs4 import BeautifulSoup
import csv

date = input("Please enter a Date in the following format MM/DD/YY: ")

page = requests.get(f"https://www.yallakora.com/Match-Center/?date={date}")

def main(page):
    src = page.content  #`content` method is return the content of the page in `byte code` 
    print(src)

main(page)