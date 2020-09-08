import urllib.request


def is_user_online():
    host = 'http://google.com'
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


def is_valid_topic(topic):
    if topic.isalnum():
        return True
    else:
        return False


def has_caption(post):
    try:
        caption = post['caption']
        return True
    except:
        return False


def has_data(thing):
    try:
        data = thing['data']
        return True
    except:
        return False
