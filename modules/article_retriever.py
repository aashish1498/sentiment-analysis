import re
from common.enum import NewsSource
from modules.config_parser import retrieve_topic_url
from .soup_methods import *
from urllib.parse import urlparse


_filter_dict = {
    NewsSource.BBC: {'data-component': 'text-block'},
    NewsSource.VICE: {'data-component': 'TextBlock'},
    NewsSource.PINK: {'class': 'article__content'},
    NewsSource.INDEPENDENT: {}
}


def get_articles_for_topic(source, topic):
    topic_url = retrieve_topic_url(source.name, topic.value)
    soup = get_soup_from_url(topic_url)
    article_components = _get_topic_components(soup, source)
    return _get_urls_from_components(article_components, source)


def extract_article_info(article_url, source):
    soup = get_soup_from_url(article_url)
    heading = get_header_from_soup(soup)
    text = get_div_text_from_soup(soup, _filter_dict[source])
    return [heading, text]


def _get_urls_from_components(article_components, source):
    url_list = []
    for component in article_components:
        element_url = get_href_from_element(component)
        if not urlparse(element_url).scheme:
            element_url = source.value + element_url
        url_list.append(element_url)
    return url_list


def _get_topic_components(soup, source):
    if(source == NewsSource.BBC):
        li_tags = soup.find_all('li')
        return [tag for tag in li_tags if tag.find('div', {'type': 'article'})]
    elif(source == NewsSource.PINK):
        return soup.find_all('div', class_=re.compile('article-.*__container'))
    elif(source == NewsSource.INDEPENDENT):
        return soup.find_all('h2')
    elif(source == NewsSource.VICE):
        return soup.find_all('h3', class_='vice-card-hed')
