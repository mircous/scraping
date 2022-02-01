from bs4 import BeautifulSoup
import requests, openpyxl
import csv

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



result_list = []

for venu_url in get_urls():
    #print(venu_url)
    source = requests.get(venu_url)
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    info = soup.find_all('div', class_ = 'venue-details')
    for div in info:
        name_span = div.find('span', class_ = 'contact-item-contact')
        name = name_span.text.replace('Contact: ', '').strip() if name_span else 'Name Not found'
        email_span = div.find('a', class_ = 'contact-item-email')
        email = email_span.text.split(' ')[-1].strip() if email_span else 'Email Not found'
        phone_span = div.find('span', class_ = 'contact-item-phone')
        phone = phone_span.text.strip() if phone_span else 'Phone Not found'


        data = {
            "name": name,
            "email": email,
            "phone": phone,
            "link": venu_url
        }
        result_list.append(data)


with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'email', 'phone', 'link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(result_list)
