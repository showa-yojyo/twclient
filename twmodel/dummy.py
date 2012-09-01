# -*- coding: utf-8 -*-
# Copyright (c) 2012 プレハブ小屋 <yojyo@hotmail.com>
# All Rights Reserved.  NO WARRANTY.

from twmodel.timeline import TimeLine

class DummyTimeLine(TimeLine):
    def __init__(self, parent=None, *args, **kwargs):
        super(DummyTimeLine, self).__init__(parent)

    def do_request(self, max_id, min_id):
        return [{u'user': {u'follow_request_sent': None, 
                           u'profile_use_background_image': True,
                           u'default_profile_image': False,
                           u'id': 461058152,
                           u'verified': False,
                           u'profile_image_url_https': u'https://si0.twimg.com/profile_images/1815197062/g5268_normal.png',
                           u'profile_sidebar_fill_color': u'DDEEF6',
                           u'profile_text_color': u'333333',
                           u'followers_count': 7,
                           u'profile_sidebar_border_color': u'C0DEED',
                           u'id_str': u'461058152',
                           u'profile_background_color': u'000000',
                           u'listed_count': 1,
                           u'profile_background_image_url_https': u'https://si0.twimg.com/profile_background_images/428817436/illvelo-wallpaper.png',
                           u'utc_offset': 32400,
                           u'statuses_count': 1219,
                           u'description': u'\u5b9f\u306f\u96fb\u5b50\u306e\u4e16\u754c\u306e\u4eba\u3067\u73fe\u5b9f\u306b\u306f\u5b58\u5728\u3057\u306a\u3044\u3002',
                           u'friends_count': 0,
                           u'location': u'\u6771\u4eac\u90fd\u533a\u5185',
                           u'profile_link_color': u'000080',
                           u'profile_image_url': u'http://a0.twimg.com/profile_images/1815197062/g5268_normal.png',
                           u'following': None,
                           u'show_all_inline_media': False,
                           u'geo_enabled': False,
                           u'profile_background_image_url': u'http://a0.twimg.com/profile_background_images/428817436/illvelo-wallpaper.png',
                           u'screen_name': u'showa_yojyo',
                           u'lang': u'ja',
                           u'profile_background_tile': True,
                           u'favourites_count': 484,
                           u'name': u'\u30d7\u30ec\u30cf\u30d6\u5c0f\u5c4b',
                           u'notifications': None,
                           u'url': u'http://www.geocities.jp/showa_yojyo/',
                           u'created_at': u'Wed Jan 11 12:01:03 +0000 2012',
                           u'contributors_enabled': False,
                           u'time_zone': u'Tokyo',
                           u'protected': False,
                           u'default_profile': False,
                           u'is_translator': False},
                u'favorited': False,
                u'entities': {u'user_mentions': [], 
                              u'hashtags': [{u'indices': [0, 7], u'text': u'gunosy'}],
                              u'urls': [{u'url': u'http://t.co/x5C2iJaG', u'indices': [86, 106], u'expanded_url': u'http://gunosy.com/showa_yojyo/2012/06/29', u'display_url': u'gunosy.com/showa_yojyo/20\u2026'}]
                              },
                u'contributors': None, 
                u'truncated': False, 
                u'text': u'#gunosy 6.29 \u611f\u60f3\u3002\u793e\u4f1a\u30fb\u653f\u6cbb\u30cb\u30e5\u30fc\u30b9\u591a\u3081\u3067\u5177\u5408\u826f\u3057\u3002\u79c1\u306f\u30de\u30a4\u30a2\u30df\u306e\u9854\u98df\u3044\u3061\u304e\u308a\u4e8b\u4ef6\u3068\u30e1\u30c0\u30ab\u30dc\u30c3\u30af\u30b9\u306e\u8aad\u66f8\u611f\u60f3\u6587\u306e\u4e21\u65b9\u306b\u8208\u5473\u306e\u3042\u308b\u4eba\u7269\u3060\u3068\u601d\u308f\u308c\u3066\u3044\u308b\u306e\u3060\u306a\uff1f http://t.co/x5C2iJaG',
                u'created_at': u'Fri Jun 29 15:40:23 +0000 2012',
                u'retweeted': False,
                u'in_reply_to_status_id_str': None,
                u'coordinates': None,
                u'in_reply_to_user_id_str': None,
                u'source': u'<a href="http://www.echofon.com/" rel="nofollow">Echofon</a>',
                u'in_reply_to_status_id': None,
                u'in_reply_to_screen_name': None,
                u'id_str': u'218730640038830083',
                u'place': None,
                u'retweet_count': 0,
                u'geo': None,
                u'id': 218730640038830083L,
                u'possibly_sensitive': False,
                u'in_reply_to_user_id': None
                }] * 20
