from bs4 import BeautifulSoup
import requests, openpyxl


excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = "Fair Play Music Venues"
print(excel.sheetnames)
sheet.append(["name", "email", "phone number"])



BASE_URL = 'https://musiciansunion.org.uk'

def get_urls():
    venu_list = []
    source = requests.get("https://musiciansunion.org.uk/fair-play-music-venues")
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    links = soup.find_all('a', class_="arrow-link coverlink", href=True)
    for link in links:
        endpoint = link.get('href')
        href = f'https://musiciansunion.org.uk{endpoint}'
        venu_list.append(href)
    return venu_list
    
print(get_urls())
