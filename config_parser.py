import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def retrieve_topic_url(source, topic_name):
    return config.get(source, topic_name)
