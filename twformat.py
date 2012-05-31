# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
import datetime
from dateutil.parser import parse
#from dateutil.tz import gettz
#JST = gettz('Asia/Tokyo')

# Borrowed from http://mitc.xrea.jp/diary/096
class UTC(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(0)
    def tzname(self, dt):
        return "UTC"
    def dst(self, dt):
        return datetime.timedelta(0)

# Borrowed from http://mitc.xrea.jp/diary/096
class JST(datetime.tzinfo):
    def utcoffset(self,dt):
        return datetime.timedelta(hours=9)
    def dst(self,dt):
        return datetime.timedelta(0)
    def tzname(self,dt):
        return "JST"

CSS = u'''
p.f{ color:lightslategrey; }
'''

HTML_PART = u'''
<table width="100%">
  <tr>
    <td valign="top" width="34">
      <img src="{4}" width="32" height="32" />
    </td>
    <td>
      <b><a href="chrome://user_mention/{0}">{0}</a></b> 
      {1}
      <p class="f">{2} {3} で {5}</p>
    </td>
    {6}
  </tr>
</table>
<hr />
'''

REPLY_FORMAT = u'''<a href="https://twitter.com/{0}/statuses/{1}">{0} への返信</a>'''

def get_user(item):
    if 'user' in item:
        return item['user']['screen_name']
    elif 'from_user' in item:
        return item['from_user']

def get_profile_image_url(item):
    if 'user' in item:
        return item['user']['profile_image_url']
    elif 'from_user' in item:
        return item['profile_image_url']

def get_source(item):
    source = item['source']
    if 'user' in item:
        return source

    # opposite of cgi.escape()
    parser = HTMLParser()
    return parser.unescape(source)

def get_timestamp(item):
    dt = parse(item['created_at'])
    #return dt.astimezone(JST).strftime(u'%Y/%m/%d (%a) %H:%M:%S %Z')
    return dt.astimezone(JST()).strftime(u'%Y/%m/%d (%a) %H:%M:%S %Z')
    #return dt.replace(tzinfo=UTC()).astimezone(JST()).strftime(u'%Y/%m/%d (%a) %H:%M:%S %Z')

def format_status(item):
    return HTML_PART.format(
        get_user(item), 
        format_text(item),
        get_timestamp(item),
        get_source(item),
        get_profile_image_url(item),
        format_in_reply(item),
        format_media(item))

def format_text(status_item):
    text = status_item['text']
    replacements = []

    entities = status_item['entities']

    for tag in entities['hashtags']:
        rep = dict(indices=tag['indices'],
                   pattern=u'<a href="chrome://hashtag/{0}">#{0}</a>'.format(tag['text']))
        replacements.append(rep)

    # [{u'display_url': u'search.twitter.com',
    #   u'expanded_url': u'http://search.twitter.com',
    #   u'indices': [0, 20],
    #   u'url': u'http://t.co/zi4sB8iv'}]
    for url in entities['urls']:
        rep = dict(indices=url['indices'],
                   pattern=u'<a href="{0[url]}">{0[display_url]}</a>'.format(url))
        replacements.append(rep)

    #pprint.pprint(entities['user_mentions'])
    # [{u'id': 461058152,
    #   u'id_str': u'461058152',
    #   u'indices': [0, 12],
    #   u'name': u'\u30d7\u30ec\u30cf\u30d6\u5c0f\u5c4b',
    #   u'screen_name': u'showa_yojyo'}]
    for user in entities['user_mentions']:
        rep = dict(indices=user['indices'],
                   pattern=u'<a href="chrome://user_mention/{0[screen_name]}">@{0[screen_name]}</a>'.format(user))
        replacements.append(rep)

    # sort by 'indices'
    replacements.sort()

    processed_text = text
    for rep in reversed(replacements):
        first, last = rep['indices']
        pattern = rep['pattern']
        processed_text = processed_text[:first] + pattern + processed_text[last:]

    return processed_text

def format_in_reply(status):

    if 'in_reply_to_status_id' in status:
        if 'to_user' in status and status['to_user']:
            return REPLY_FORMAT.format(status['to_user'],
                                       status['in_reply_to_status_id'])
        elif 'in_reply_to_screen_name' in status and status['in_reply_to_screen_name']:
            return REPLY_FORMAT.format(status['in_reply_to_screen_name'], 
                                       status['in_reply_to_status_id'])

    return u''


THUMB_PART = u'''
    <td valign="top" width="52">
      <a href="{media_url}"><img src="{thumb_url}" width="50" height="50" /></a>
    </td>
'''

def format_media(status_item):
    # See https://dev.twitter.com/docs/tweet-entities

    text = u''
    if not 'entities' in status_item:
        return text

    entities = status_item['entities']
    if not 'media' in entities:
        return text

    media = entities['media']

    # e.g. "http://p.twimg.com/AQ9JtQsCEAA7dEN.jpg"
    media_url = media[0]['media_url']

    # get thumbnail 
    thumb_url = media_url + ':thumb'

    return THUMB_PART.format(media_url=media_url,
                             thumb_url=thumb_url)
