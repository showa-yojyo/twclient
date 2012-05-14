# -*- coding: utf-8 -*-

from dateutil.parser import parse
from dateutil.tz import gettz, tzlocal, tzutc

JST = gettz('Asia/Tokyo')

CSS = u'''
p.f{ color:lightslategrey; }
'''

HTML_PART = u'''
<table>
  <tr>
    <td valign="top" height="34">
      <img src="{4}" width="32" height="32" />
    </td>
    <td>
      <b><a href="chrome:://user_mention/{0}">{0}</a></b> 
      {1}
      <p class="f">{2} {3[source]} で</p>
    </td>
  </tr>
</table>
<hr />
'''

def get_profile_image_url(item):
    if 'user' in item:
        return item['user']['profile_image_url']
    elif 'from_user' in item:
        return item['profile_image_url']

def format_status(item):
    return HTML_PART.format(
        format_user(item), 
        format_text(item),
        format_timestamp(item),
        item,
        get_profile_image_url(item))

def format_text(status_item):
    text = status_item['text']
    replacements = []

    entities = status_item['entities']

    for tag in entities['hashtags']:
        rep = dict(indices=tag['indices'],
                   pattern=u'<a href="chrome:://hashtag/{0}">#{0}</a>'.format(tag['text']))
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
                   pattern=u'<a href="chrome:://user_mention/{0[screen_name]}">@{0[screen_name]}</a>'.format(user))
        replacements.append(rep)

    # sort by 'indices'
    replacements.sort()

    processed_text = text
    for rep in reversed(replacements):
        first, last = rep['indices']
        pattern = rep['pattern']
        processed_text = processed_text[:first] + pattern + processed_text[last:]

    return processed_text

def format_user(item):
    if 'user' in item:
        return item['user']['screen_name']
    elif 'from_user' in item:
        return item['from_user']

def format_timestamp(item):
    dt = parse(item['created_at'])
    return dt.astimezone(JST).strftime(u'%Y/%m/%d (%a) %H:%M:%S %Z')

def format_search_result(item):
    return HTML_PART.format(
        format_user(item),
        format_text(item),
        format_timestamp(item),
        item, # TODO: workaround for Twitter API's bug
        get_profile_image_url(item))
