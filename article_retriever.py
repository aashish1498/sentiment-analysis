import re
from urllib.parse import urlparse
from soup_methods import *

_bbc_url = 'https://www.bbc.co.uk'
_pink_url = 'https://www.thepinknews.com'
_filter_dict = {
    _bbc_url: {'data-component': 'text-block'},
    _pink_url: {'class': 'article__content'}
}

def get_articles_for_topic(topic_url):
    base_url = _get_base_url(topic_url)
    if base_url == _bbc_url:
        return _get_articles_for_bbc_topic(topic_url)
    elif base_url == _pink_url:
        return _get_articles_for_pink_topic(topic_url)
    else:
        print(topic_url + ' is not a supported url')

def get_info_from_article(article_url):
    filter = _get_filter(article_url)
    soup = get_soup_from_url(article_url)
    heading = get_header_from_soup(soup)
    text = get_div_text_from_soup(soup, filter)
    return [heading, text]

def _get_articles_for_bbc_topic(topic_url):
    prefix = _get_base_url(topic_url)
    soup = get_soup_from_url(topic_url)   
    li_tags = soup.find_all('li')
    url_list = []
    for li_tag in li_tags:
        article_div = li_tag.find('div', {'type': 'article'})
        if article_div:
            url_list.append(prefix + get_href_from_element(article_div))
    return url_list

def _get_articles_for_pink_topic(topic_url):
    soup = get_soup_from_url(topic_url)
    article_divs = soup.find_all('div', class_=re.compile('article-.*__container'))
    url_list = []
    for article_div in article_divs:
        url_list.append(get_href_from_element(article_div))
    return url_list

def _get_filter(url):
    base_url = _get_base_url(url)
    if base_url in _filter_dict:
        return _filter_dict[base_url]
    else:
        print(url + ' is not a supported url')

def _get_base_url(url):
    parsed_uri = urlparse(url)
    return '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
