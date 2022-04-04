from bs4 import BeautifulSoup
import requests, openpyxl
import csv
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'PRODUCT'

product_list = []

def get_products():
    types_list = []
    source = requests.get('https://www.nilfisk.com/en-au/products')
    source.raise_for_status()
    soup = BeautifulSoup(source.text, 'html.parser')
    gird = soup.find('div', class_="row border-bottom-0")
    links = gird.find_all('a', class_='col hero__frontpage__tabs__item', href=True)

    for link in links:
        endpoint = link.get('href')
        href = f'https://www.nilfisk.com/{endpoint}'
        types_list.append(href)
    return types_list

def types_of_cleaners():
    types_list = []
    for x in get_products():
        source = requests.get(x)
        soup = BeautifulSoup(source.text, 'html.parser')
        gird = soup.find('div', class_="row pt-md-5 justify-content-center")
        try:
            links = gird.find_all('a', class_='category-card-identifier-class col-12 col-lg-4 product_category py-3 mb-3')
        except:
            pass
        for link in links:
            endpoint = link.get('href')
            href = f'https://www.nilfisk.com/{endpoint}'
            types_list.append(href)
    return types_list

def try_udercategories():
    types_list = []
    for x in types_of_cleaners():
        source = requests.get(x)
        soup = BeautifulSoup(source.text, 'html.parser')
        gird = soup.find('div', class_='row pt-md-5 justify-content-center')
        try:
            links = gird.find_all('a', class_='category-card-identifier-class col-12 col-lg-4 product_category py-3 mb-3')
            for link in links:
                endpoint = link.get('href')
                try:
                    requests.get(endpoint)
                    product_list.append(endpoint)
                except:
                    href = f'https://www.nilfisk.com/{endpoint}'
                    types_list.append(href)
        except:
            pass
    return types_list

def get_product_links():
    more_categories = []
    for x in try_udercategories():
        source = requests.get(x)
        soup = BeautifulSoup(source.text, 'html.parser')
        gird = soup.find('div', class_='row pt-md-5 justify-content-center')
        try:
            links = gird.find_all('a', class_='category-card-identifier-class col-12 col-lg-4 product_category py-3 mb-3')
            for link in links:
                endpoint = link.get('href')
                try:
                    requests.get(endpoint)
                    product_list.append(endpoint)
                except:
                    href = f'https://www.nilfisk.com/{endpoint}'
                    more_categories.append(href)
        except:
            pass
    return more_categories

def get_all_urls():
    must_be_empty = []
    plplP
def get_info():
    for x in product_list:
        titles = []
        lst = []
        doc = []
        source = requests.get(x)
        soup = BeautifulSoup(source.text, 'html.parser')
        gird = soup.find('div', class_='col-12 container product__specifications__placeholder')
        datas = gird.find('ul', class_='list-unstyled').find_all('li')
        for data in datas:
            lsd = data.find('div').text
            titles.append(lsd)
            try:
                lsdd = data.find_all('div')
                lst.append((lsdd[1]).text)
            except:
                lst.append("Empty")
        #docgird = soup.find('div', class_='container')
        #linkz = docgird.find('div', class_='sl}ck-track')
        #linkz.find_all('a', href = True)
        #for link in docgird:
        #    endpoint = link.get('href')
        #    doc.append(endpoint)
        sheet.append(titles)
        #print(titles)
        sheet.append(lst)
        #print(lst)
        #sheet.append(doc)
        #print(doc)
get_info()
print('!!!')
excel.save('website_data.xlsx')
