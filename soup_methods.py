from bs4 import BeautifulSoup
import requests


def get_soup_from_url(page_url):
    response = requests.get(page_url)
    return BeautifulSoup(response.text, features="html.parser")


def get_div_text_from_soup(soup, filter):
    text_blocks = soup.find_all(['div', 'span', 'p'], filter)
    text_list = [text_block.get_text(strip=True) for text_block in text_blocks]
    return ' '.join(text_list)


def get_header_from_soup(soup):
    header = soup.find('h1')
    return header.text


def get_href_from_element(element):
    return element.find('a')['href']
