from bs4 import BeautifulSoup
import lxml
import os



def get_fb2():
    with open('123.fb2', 'lxml.parser', encoding='utf-8',) as file:
        src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        print(soup.read('p'))



    # if soup.find('date', {'value': True}):
    #     return soup.find('date', {'value': True})
    # 'value'[:4]
    # elif soup.find('date'):
    # return soup.find('date').text[:4]

