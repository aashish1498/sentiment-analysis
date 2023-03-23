import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def retrieve_topic_url(source, topic_name):
    if not config.has_option(source, topic_name):
        raise ValueError(f'Topic: "{topic_name}" not defined under "{source}" in config.ini')
    return config.get(source, topic_name)
