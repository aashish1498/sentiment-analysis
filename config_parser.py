import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def retrieve_topic_url(source, topic_name):
    topic_url = config.get(source, topic_name)
