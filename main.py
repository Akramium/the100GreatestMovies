import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.senscritique.com/films/tops/top100-des-top10")
em_web_page = response.text

soup = BeautifulSoup(em_web_page, 'html.parser')
#

movies = [title.getText() for title in soup.find_all(name="a", class_="elco-anchor")]

with open(file="movies.txt", mode="w") as file:
    for movie in movies:
        print(movie)
        file.write(f"{movie}\n")
