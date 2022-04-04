from bs4 import BeautifulSoup
import requests
import csv

data_list = []

def get_urls():
    source = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
    source.raise_for_status()
    soup = BeautifulSoup(source.text, 'html.parser')
    body = soup.find('tbody')
    lst = body.find_all('tr')
    for i in lst:
        title = i.find('td', class_='titleColumn').a.text
        year = i.find('td', class_= "titleColumn").span.text.strip('()')
        rating = i.find('td', class_= "ratingColumn imdbRating").strong.text
        data = {
            "title" : title,
            "year" : year,
            "rating" : rating
        }

        data_list.append(data)
get_urls()

field_names = ['title', 'year', 'rating']
# name of csv file
filename = "IMDb.csv"



with open(filename, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    #writing data rows!
    writer.writerows(data_list)
