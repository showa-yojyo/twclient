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
      <img src="{profile_image_url}" width="32" height="32" />
    </td>
    <td>
      <b><a href="chrome://user_mention/{screen_name}">{screen_name}</a></b> 
      {text}
      <p class="f">{created_at} {source} で {in_reply}</p>
    </td>
    {media}
  </tr>
</table>
<hr />
'''

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
    kwargs = dict(
        screen_name=get_user(item),
        text=format_text(item),
        created_at=get_timestamp(item),
        source=get_source(item),
        profile_image_url=get_profile_image_url(item),
        in_reply=format_in_reply(item),
        media=format_media(item))

    return HTML_PART.format(**kwargs)

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

REPLY_FORMAT = u'''<a href="https://twitter.com/{screen_name}/statuses/{id}">{screen_name} への返信</a>'''

def format_in_reply(status):

    if 'in_reply_to_status_id' in status:
        kwargs = dict(id=status['in_reply_to_status_id'])
        if 'to_user' in status and status['to_user']:
            kwargs['screen_name'] = status['to_user']
            return REPLY_FORMAT.format(**kwargs)
        elif 'in_reply_to_screen_name' in status and status['in_reply_to_screen_name']:
            kwargs['screen_name'] = status['in_reply_to_screen_name']
            return REPLY_FORMAT.format(**kwargs)

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
