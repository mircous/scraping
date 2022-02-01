from bs4 import BeautifulSoup
import requests
import csv

def get_urls():

    venu_list = []
    venu_list1 = []
    source = requests.get("https://edu.ge.ch/moodle/course/index.php?fbclid=IwAR2EcCIKG8Iho3r9V39Bf1L4zofZxvOYUy9Nsx4nALcriqye5C2iRAgnH5E")
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    sup = soup.find('div', class_ = 'subcategories')
    links = sup.find_all('a', href = True)
    for link in links:
        href = link.get('href')
        venu_list.append(href)
    for x in venu_list:
        source1 = requests.get(x)
        soup1 = BeautifulSoup(source.text, 'html.parser')
        sup1 = soup1.find('div', class_ = 'content')
        links1 = sup1.find_all('a', href = True)
        for link1 in links1:
            href1 = link1.get('href')
            venu_list1.append(href1)
    for x in venu_list:
        venu_list1.append(x)
    return venu_list1

names = []
names1 = []
for x in get_urls():
    try:
        source = requests.get(x)
        soup = BeautifulSoup(source.text, 'html.parser')
        sup = soup.find_all('ul', class_ = 'teachers')
        for x in sup:
            links = x.find_all('li')
            for x in links:
                if x not in names:
                    names.append(x.text)
    except:
        pass

for x in names:
    try:
        names1.append(x.replace('Teacher: ', ''))
    except:

        names1.append(x.replace('Professeur: ', ''))

print(names1)
