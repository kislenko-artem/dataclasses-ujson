from datetime import datetime
import enum
from typing import List, Dict, Union, Optional, TypeAlias

from dataclasses import dataclass
from dataclasses_ujson.dataclasses_ujson import UJsonMixin

JSON_SIMPLE = '{"x": 1}'
JSON_SIMPLE_STR = '{"x": "one"}'
JSON_SIMPLE_OPTIONAL = '{"x": 1, "y": null}'
JSON_LIST = '{"x": [1]}'
JSON_DICT = '{"x": {"d": 1}}'
JSON_NESTED = '{{"a": {simple}, "b": {list}, "c": {dict}}}'.format(
    simple=JSON_SIMPLE, list=JSON_LIST, dict=JSON_DICT)
JSON_UNION_V1 = '{{"a": 1, "b": {list}, "c": {list}}}'.format(list=JSON_LIST)
JSON_UNION_V2 = '{{"a": "s", "b": {dict}, "c": {dict}}}'.format(dict=JSON_DICT)

JSON_SIMPLE_LIST = '[{"x": 1}]'
JSON_NESTED_LIST = '{{"a": {simple}, "b": [{list}], "c": [{dict}]}}'.format(
    simple=JSON_SIMPLE, list=JSON_LIST, dict=JSON_DICT)
JSON_VK = '''
{"count": 578, "items": [{"id": 45668, "from_id": -61006621, "owner_id": -61006621, "date": 1531139873, "marked_as_ads": 0, "post_type": "post", "text": "\u0424\u0438\u0448\u043a\u0438 \u0432 \u041b\u0435\u043d\u0442\u0443 \u0434\u043e 15.07\uff0c\u0448\u043a\u0430\u0444 \u0441\u0430\u043c\u043e\u0432\u044b\u0432\u043e\u0437 \u0441 \u0441\u0430\u0434\u043e\u0432, \u043f\u0430\u0440\u0430 \u043c\u0443\u0436 \u0434\u0436\u0438\u043d\u0441 \u043d\u0430 \u043f\u043e\u0434\u0435\u043b\u043a\u0438.", "signer_id": 216078137, "attachments": [{"type": "photo", "photo": {"id": 456250864, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c845421/v845421539/9e5fa/NQewHCexzHk.jpg", "photo_130": "https://pp.userapi.com/c845421/v845421539/9e5fb/WrUWkOz_XDM.jpg", "photo_604": "https://pp.userapi.com/c845421/v845421539/9e5fc/h5mBywiKzAk.jpg", "photo_807": "https://pp.userapi.com/c845421/v845421539/9e5fd/NJbEm_B-zdY.jpg", "photo_1280": "https://pp.userapi.com/c845421/v845421539/9e5fe/VGlxZk972sQ.jpg", "photo_2560": "https://pp.userapi.com/c845421/v845421539/9e5ff/UW2jTjG24RI.jpg", "width": 2560, "height": 1898, "text": "", "date": 1531135427, "lat": 56.224976, "long": 93.507524, "access_key": "6fce7dad27ffab5f22"}}, {"type": "photo", "photo": {"id": 456250865, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c845421/v845421539/9e604/xzlP-Qnp6Sc.jpg", "photo_130": "https://pp.userapi.com/c845421/v845421539/9e605/LVIv8pKjhPI.jpg", "photo_604": "https://pp.userapi.com/c845421/v845421539/9e606/BtqsTukMQl0.jpg", "photo_807": "https://pp.userapi.com/c845421/v845421539/9e607/Zun4wBSvxc4.jpg", "photo_1280": "https://pp.userapi.com/c845421/v845421539/9e608/8usdAi-iyeI.jpg", "photo_2560": "https://pp.userapi.com/c845421/v845421539/9e609/ByhtbHifBUI.jpg", "width": 2560, "height": 1898, "text": "", "date": 1531135427, "access_key": "c08a351f8692724df8"}}, {"type": "photo", "photo": {"id": 456250866, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c845421/v845421539/9e60e/WHs4Rdu2_2g.jpg", "photo_130": "https://pp.userapi.com/c845421/v845421539/9e60f/gsZ3UAMC9SM.jpg", "photo_604": "https://pp.userapi.com/c845421/v845421539/9e610/OrBiRn7R0Rg.jpg", "photo_807": "https://pp.userapi.com/c845421/v845421539/9e611/jHbOoChmYEA.jpg", "photo_1280": "https://pp.userapi.com/c845421/v845421539/9e612/8SPi8ucKbC4.jpg", "photo_2560": "https://pp.userapi.com/c845421/v845421539/9e613/S8i6busxOhU.jpg", "width": 1602, "height": 2160, "text": "", "date": 1531135427, "lat": 56.194023, "long": 93.546361, "access_key": "d623ce300e8afa0afe"}}, {"type": "photo", "photo": {"id": 456250867, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c845421/v845421539/9e618/22Jztd-SO_Q.jpg", "photo_130": "https://pp.userapi.com/c845421/v845421539/9e619/ebwSW_pcR4M.jpg", "photo_604": "https://pp.userapi.com/c845421/v845421539/9e61a/BMkUdxJkZkQ.jpg", "photo_807": "https://pp.userapi.com/c845421/v845421539/9e61b/5oUOSAyty3Q.jpg", "photo_1280": "https://pp.userapi.com/c845421/v845421539/9e61c/mYyUd0TrzUM.jpg", "photo_2560": "https://pp.userapi.com/c845421/v845421539/9e61d/WgYzxnsKlLU.jpg", "width": 2560, "height": 1898, "text": "", "date": 1531135427, "access_key": "fac24d55138e807a74"}}], "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 0, "groups_can_post": true, "can_post": 1}, "likes": {"count": 0, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 369}}, {"id": 45666, "from_id": -61006621, "owner_id": -61006621, "date": 1531139850, "marked_as_ads": 0, "post_type": "post", "text": "\u043e\u0442\u0434\u0430\u043c \u0434\u0432\u0430 \u043f\u0430\u043a\u0435\u0442\u0430..\u043e\u0434\u0435\u0436\u0434\u0430 \u043d\u0430 \u0434\u0435\u0432\u043e\u0447\u043a\u0443..\u043e\u0442 8\u043c\u0435\u0441-1.6 \u043b\u0435\u0442. \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0440\u0430\u0437\u043d\u043e\u0435.. \u0441\u0440\u0435\u0434\u043d\u0435\u0435..\u0431\u043e\u043b\u044c\u0448\u0430\u044f \u0447\u0430\u0441\u0442\u044c \u0434\u043b\u044f \u0434\u043e\u043c\u0430..\u0444\u0443\u0442\u0431\u043e\u043b\u043e\u0447\u043a\u0438 .\u043a\u043e\u0444\u0442\u043e\u0447\u043a\u0438 \u0438 \u0442.\u0434..\u043f\u0438\u0441\u0430\u0442\u044c \u0432 \u043b.\u0441.", "signer_id": 84611251, "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 0, "groups_can_post": true, "can_post": 1}, "likes": {"count": 0, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 371}}, {"id": 45661, "from_id": -61006621, "owner_id": -61006621, "date": 1531135087, "marked_as_ads": 0, "post_type": "post", "text": "\u041e\u0442\u0434\u0430\u043c!\u043e\u0442 3-6 \u043c\u0435\u0441\u044f\u0446\u0435\u0432,\u0440.68-74!\u0428\u043e\u043a\u043e\u043b\u0430\u0434\u043a\u0430 \u043f\u0440\u0438\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u0442\u0441\u044f!)", "signer_id": 47838728, "attachments": [{"type": "photo", "photo": {"id": 456250861, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c845020/v845020910/98d3b/N8Z_5QTFGk0.jpg", "photo_130": "https://pp.userapi.com/c845020/v845020910/98d3c/gnawEjCLYI8.jpg", "photo_604": "https://pp.userapi.com/c845020/v845020910/98d3d/RAwo94rKjio.jpg", "photo_807": "https://pp.userapi.com/c845020/v845020910/98d3e/onqAOVtw_7o.jpg", "photo_1280": "https://pp.userapi.com/c845020/v845020910/98d3f/tbTD7hNiT94.jpg", "photo_2560": "https://pp.userapi.com/c845020/v845020910/98d40/Ldt2bZXpb38.jpg", "width": 2560, "height": 1920, "text": "", "date": 1531128438, "post_id": 45653, "access_key": "c5d0a0016dcb6abc20"}}], "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 0, "groups_can_post": true, "can_post": 1}, "likes": {"count": 3, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 496}}, {"id": 45660, "from_id": -61006621, "owner_id": -61006621, "date": 1531135084, "marked_as_ads": 0, "post_type": "post", "text": "\u041e\u0442\u0434\u0430\u043c \u043a\u043e\u0441\u0442\u044e\u043c \u0432\u0435\u0441\u043d\u0430-\u043e\u0441\u0435\u043d\u044c,\u0440.74!", "signer_id": 47838728, "attachments": [{"type": "photo", "photo": {"id": 456250862, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://sun9-9.userapi.com/c834403/v834403910/182b70/SB0MCQoPIqQ.jpg", "photo_130": "https://sun9-5.userapi.com/c834403/v834403910/182b71/y5O5CH64hg4.jpg", "photo_604": "https://sun9-6.userapi.com/c834403/v834403910/182b72/IEaWYrxg9DU.jpg", "photo_807": "https://sun9-8.userapi.com/c834403/v834403910/182b73/APO1C-FSej4.jpg", "photo_1280": "https://sun9-8.userapi.com/c834403/v834403910/182b74/-36jOR5Wpkw.jpg", "photo_2560": "https://sun9-4.userapi.com/c834403/v834403910/182b75/3ZIuny8Dy1k.jpg", "width": 1620, "height": 2160, "text": "", "date": 1531128515, "post_id": 45654, "access_key": "a5f71d5c162231ed55"}}], "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 0, "groups_can_post": true, "can_post": 1}, "likes": {"count": 1, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 428}}, {"id": 45659, "from_id": -61006621, "owner_id": -61006621, "date": 1531135078, "marked_as_ads": 0, "post_type": "post", "text": "\u0421\u043f\u043e\u0440\u0442\u0438\u0432\u043d\u044b\u0439 \u043a\u0443\u043f\u0430\u043b\u044c\u043d\u0438\u043a \u043d\u0430 \u0440\u043e\u0441\u0442 146 \u0444\u0438\u0440\u043c\u044b Demix.", "signer_id": 37549991, "attachments": [{"type": "photo", "photo": {"id": 456250863, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c834304/v834304814/ce6c9/LtkZdzGoyeA.jpg", "photo_130": "https://pp.userapi.com/c834304/v834304814/ce6ca/nCl25-FGgDQ.jpg", "photo_604": "https://pp.userapi.com/c834304/v834304814/ce6cb/Zy-R9JjWw_4.jpg", "photo_807": "https://pp.userapi.com/c834304/v834304814/ce6cc/aBrliiTmKFk.jpg", "photo_1280": "https://pp.userapi.com/c834304/v834304814/ce6cd/W50ecv28sgA.jpg", "photo_2560": "https://pp.userapi.com/c834304/v834304814/ce6ce/XygDn1mDs9I.jpg", "width": 1620, "height": 2160, "text": "", "date": 1531134738, "access_key": "554cfe1fc2b3eaa3ab"}}], "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 1, "groups_can_post": true, "can_post": 1}, "likes": {"count": 0, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 399}}, {"id": 45645, "from_id": -61006621, "owner_id": -61006621, "date": 1531116940, "marked_as_ads": 0, "post_type": "post", "text": "\u041e\u0442\u0434\u0430\u043c \u0443\u0447\u0435\u0431\u043d\u0438\u043a\u0438, \u0436\u0443\u0440\u043d\u0430\u043b\u044b \u0430\u043d\u0433\u043b.", "signer_id": 6356076, "attachments": [{"type": "photo", "photo": {"id": 456250854, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c834202/v834202371/14297c/EH9E6jjDWas.jpg", "photo_130": "https://pp.userapi.com/c834202/v834202371/14297d/g-V-N4Qjt1o.jpg", "photo_604": "https://pp.userapi.com/c834202/v834202371/14297e/ZO2QMPYVBQ8.jpg", "photo_807": "https://pp.userapi.com/c834202/v834202371/14297f/cfBEUQYdnrY.jpg", "photo_1280": "https://pp.userapi.com/c834202/v834202371/142980/cMLlD7GnY1g.jpg", "photo_2560": "https://pp.userapi.com/c834202/v834202371/142981/620fwmsQ4K8.jpg", "width": 1632, "height": 1224, "text": "", "date": 1531105397, "access_key": "bade112b8e2b47f16d"}}, {"type": "photo", "photo": {"id": 456250855, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c850036/v850036371/22e3d/hk-lrMGShJg.jpg", "photo_130": "https://pp.userapi.com/c850036/v850036371/22e3e/OcJ2AVaFnvA.jpg", "photo_604": "https://pp.userapi.com/c850036/v850036371/22e3f/TeiFgYG_WzI.jpg", "photo_807": "https://pp.userapi.com/c850036/v850036371/22e40/DjClsiFkq7g.jpg", "photo_1280": "https://pp.userapi.com/c850036/v850036371/22e41/hPrmGsctPZc.jpg", "photo_2560": "https://pp.userapi.com/c850036/v850036371/22e42/koNBQdjAldc.jpg", "width": 1632, "height": 1224, "text": "", "date": 1531105397, "access_key": "b5a56d3d997bc65c91"}}], "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 0, "groups_can_post": true, "can_post": 1}, "likes": {"count": 0, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 698}}, {"id": 45642, "from_id": -61006621, "owner_id": -61006621, "date": 1531116929, "marked_as_ads": 0, "post_type": "post", "text": "\u0411\u043e\u0442\u0438\u043d\u043a\u0438 \u0434\u043b\u044f \u0434\u0435\u0432\u043e\u0447\u043a\u0438, 35 \u0440\u0430\u0437\u043c\u0435\u0440", "signer_id": 37549991, "attachments": [{"type": "photo", "photo": {"id": 456250856, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c830308/v830308680/13effe/_YAKCI49lic.jpg", "photo_130": "https://pp.userapi.com/c830308/v830308680/13efff/Af9PmtokkV8.jpg", "photo_604": "https://pp.userapi.com/c830308/v830308680/13f000/zkRe0ZyqhJ8.jpg", "photo_807": "https://pp.userapi.com/c830308/v830308680/13f001/h_809C5-6Xc.jpg", "photo_1280": "https://pp.userapi.com/c830308/v830308680/13f002/q5okz0hoK0Y.jpg", "photo_2560": "https://pp.userapi.com/c830308/v830308680/13f003/g2N-vpugcIE.jpg", "width": 1620, "height": 2160, "text": "", "date": 1531110685, "lat": 56.229736, "long": 93.538349, "access_key": "5777cd0f6964f4965f"}}], "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 2, "groups_can_post": true, "can_post": 1}, "likes": {"count": 1, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 619}}, {"id": 45640, "from_id": -61006621, "owner_id": -61006621, "date": 1531116923, "marked_as_ads": 0, "post_type": "post", "text": "\u041e\u0442\u0434\u0430\u043c \u043d\u0435\u043c\u043d\u043e\u0433\u043e \u0432\u0435\u0449\u0435\u0439 \u043d\u0430 \u043c\u0430\u043b\u044c\u0447\u0438\u043a\u0430 1,5-3 \u0433\u043e\u0434\u0430. \u0414\u043b\u044f \u0434\u043e\u043c\u0430 \u0438 \u0434\u0430\u0447\u0438. \u0417\u0430\u0431\u0438\u0440\u0430\u0442\u044c \u0436\u0435\u043b\u0430\u0442\u0435\u043b\u044c\u043d\u043e \u0441\u0435\u0433\u043e\u0434\u043d\u044f", "signer_id": 67389960, "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 0, "groups_can_post": true, "can_post": 1}, "likes": {"count": 1, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 591}}, {"id": 45639, "from_id": -61006621, "owner_id": -61006621, "date": 1531116918, "marked_as_ads": 0, "post_type": "post", "text": "\u041e\u0442\u0434\u0430\u043c \u0441\u0430\u043d\u0434\u0430\u043b\u0438,\u0441\u043e\u0432\u0435\u0442\u0441\u043a\u0438\u0435 12 \u0441\u043c \u043f\u043e \u0441\u0442\u0435\u043b\u044c\u043a\u0435,\u0441\u043e\u0432\u0435\u043d\u043e\u043a \u0440.14", "signer_id": 47838728, "attachments": [{"type": "photo", "photo": {"id": 456250858, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c846017/v846017897/919fb/mEUn60_V7nI.jpg", "photo_130": "https://pp.userapi.com/c846017/v846017897/919fc/8DUS3WLw-Ik.jpg", "photo_604": "https://pp.userapi.com/c846017/v846017897/919fd/-rd4iujfRTc.jpg", "photo_807": "https://pp.userapi.com/c846017/v846017897/919fe/2XD5uYjmmhU.jpg", "photo_1280": "https://pp.userapi.com/c846017/v846017897/919ff/rhLk44hJ_Fc.jpg", "photo_2560": "https://pp.userapi.com/c846017/v846017897/91a00/M4v92nH-C5M.jpg", "width": 1620, "height": 2160, "text": "", "date": 1531116622, "access_key": "56a533234b8547be0e"}}, {"type": "photo", "photo": {"id": 456250859, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c846218/v846218897/972f2/A1G2JkzmKcg.jpg", "photo_130": "https://pp.userapi.com/c846218/v846218897/972f3/hgo7roXETSM.jpg", "photo_604": "https://pp.userapi.com/c846218/v846218897/972f4/XCujFkniwdk.jpg", "photo_807": "https://pp.userapi.com/c846218/v846218897/972f5/TiXoQMJ7xq4.jpg", "photo_1280": "https://pp.userapi.com/c846218/v846218897/972f6/dZRg7WG4m6Y.jpg", "photo_2560": "https://pp.userapi.com/c846218/v846218897/972f7/rdlO368kqnM.jpg", "width": 1620, "height": 2160, "text": "", "date": 1531116622, "access_key": "ae0917d26fcf558fa0"}}, {"type": "photo", "photo": {"id": 456250860, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c845420/v845420897/97a17/Yb5JTTSfpbo.jpg", "photo_130": "https://pp.userapi.com/c845420/v845420897/97a18/QCtOTSw2U1c.jpg", "photo_604": "https://pp.userapi.com/c845420/v845420897/97a19/ENoVrWzFPf4.jpg", "photo_807": "https://pp.userapi.com/c845420/v845420897/97a1a/mw1dNAHMct8.jpg", "photo_1280": "https://pp.userapi.com/c845420/v845420897/97a1b/cqx2gkTvGjQ.jpg", "photo_2560": "https://pp.userapi.com/c845420/v845420897/97a1c/m9dKL5ocGUQ.jpg", "width": 1620, "height": 2160, "text": "", "date": 1531116622, "access_key": "92e935d641a8de785e"}}], "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 0, "groups_can_post": true, "can_post": 1}, "likes": {"count": 0, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 562}}, {"id": 45626, "from_id": -61006621, "owner_id": -61006621, "date": 1531095010, "marked_as_ads": 0, "post_type": "post", "text": "\u041e\u0442\u0434\u0430\u043c \u0434\u0435\u0442\u0441\u043a\u0438\u0435 \u0432\u0435\u0449\u0438 \u0441 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f. \u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0440\u0430\u0437\u043d\u043e\u0435", "signer_id": 68650358, "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 0, "groups_can_post": true, "can_post": 1}, "likes": {"count": 0, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 824}}, {"id": 45625, "from_id": -61006621, "owner_id": -61006621, "date": 1531095006, "marked_as_ads": 0, "post_type": "post", "text": "\u041e\u0442\u0434\u0430\u043c, \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442, \u043d\u043e \u0441\u0431\u0438\u0432\u0430\u044e\u0442\u0441\u044f \u043a\u0430\u043d\u0430\u043b\u044b. \u0411\u0435\u0437 \u043f\u0443\u043b\u044c\u0442\u0430.", "signer_id": 160831686, "attachments": [{"type": "photo", "photo": {"id": 456250848, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c846520/v846520490/971cd/4CqM5F1gaiw.jpg", "photo_130": "https://pp.userapi.com/c846520/v846520490/971ce/bCnsryiN3aU.jpg", "photo_604": "https://pp.userapi.com/c846520/v846520490/971cf/2glPMkC-DhA.jpg", "photo_807": "https://pp.userapi.com/c846520/v846520490/971d0/nFEpAGlzhSw.jpg", "photo_1280": "https://pp.userapi.com/c846520/v846520490/971d1/qLJB7cI5ke8.jpg", "photo_2560": "https://pp.userapi.com/c846520/v846520490/971d2/MhCKfHBpVJc.jpg", "width": 720, "height": 1280, "text": "", "date": 1531073714, "access_key": "bcd976249a8d9fcd82"}}, {"type": "photo", "photo": {"id": 456250849, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c846220/v846220490/96511/0jNBsB9TRLs.jpg", "photo_130": "https://pp.userapi.com/c846220/v846220490/96512/KNKiZDhQ8GU.jpg", "photo_604": "https://pp.userapi.com/c846220/v846220490/96513/ElOzb7al-GQ.jpg", "photo_807": "https://pp.userapi.com/c846220/v846220490/96514/Px5DAtkgGOo.jpg", "photo_1280": "https://pp.userapi.com/c846220/v846220490/96515/62TA99YB8Dg.jpg", "photo_2560": "https://pp.userapi.com/c846220/v846220490/96516/5ieJUEv0tFI.jpg", "width": 720, "height": 1280, "text": "", "date": 1531073714, "access_key": "051ab6f0a045d2bf5d"}}, {"type": "photo", "photo": {"id": 456250850, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c845221/v845221490/95981/vx-jVHV37W8.jpg", "photo_130": "https://pp.userapi.com/c845221/v845221490/95982/4at8rG1jArk.jpg", "photo_604": "https://pp.userapi.com/c845221/v845221490/95983/ZAe95ihABDg.jpg", "photo_807": "https://pp.userapi.com/c845221/v845221490/95984/DVY7tUlB_Iw.jpg", "photo_1280": "https://pp.userapi.com/c845221/v845221490/95985/hhdgV9mjCg4.jpg", "width": 1280, "height": 720, "text": "", "date": 1531073714, "access_key": "b17747f96efd11602c"}}], "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 3, "groups_can_post": true, "can_post": 1}, "likes": {"count": 3, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 1013}}, {"id": 45621, "from_id": -61006621, "owner_id": -61006621, "date": 1531064418, "marked_as_ads": 0, "post_type": "post", "text": "\u041e\u0442\u0434\u0430\u043c \u043c\u044f\u0433\u043a\u0438\u0435 \u0438\u0433\u0440\u0443\u0448\u043a\u0438,\u043e\u0447\u0435\u043d\u044c \u043c\u043d\u043e\u0433\u043e!:)", "signer_id": 320139240, "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 2, "groups_can_post": true, "can_post": 1}, "likes": {"count": 0, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 911}}, {"id": 45619, "from_id": -61006621, "owner_id": -61006621, "date": 1531064411, "marked_as_ads": 0, "post_type": "post", "text": "\u041e\u0442\u0434\u0430\u043c. \u0412\u043e\u043f\u0440\u043e\u0441\u044b \u0432 \u043b\u0441.", "signer_id": 461064610, "attachments": [{"type": "photo", "photo": {"id": 456250842, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c830609/v830609641/13b4cb/z86q6mtyV0M.jpg", "photo_130": "https://pp.userapi.com/c830609/v830609641/13b4cc/a4ZXBqyl1Yw.jpg", "photo_604": "https://pp.userapi.com/c830609/v830609641/13b4cd/FtOaYsb__3g.jpg", "photo_807": "https://pp.userapi.com/c830609/v830609641/13b4ce/0XhH_CbZD5M.jpg", "photo_1280": "https://pp.userapi.com/c830609/v830609641/13b4cf/QLD5SA5SDDg.jpg", "width": 960, "height": 720, "text": "", "date": 1531057446, "lat": 56.22605, "long": 93.514991, "access_key": "b54dbf970766adc03d"}}, {"type": "photo", "photo": {"id": 456250843, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c849228/v849228641/22d06/deNl8fUY4GQ.jpg", "photo_130": "https://pp.userapi.com/c849228/v849228641/22d07/HgLrR2qWvKs.jpg", "photo_604": "https://pp.userapi.com/c849228/v849228641/22d08/n6tdt5Ov8Tw.jpg", "photo_807": "https://pp.userapi.com/c849228/v849228641/22d09/guMiRAsADx4.jpg", "photo_1280": "https://pp.userapi.com/c849228/v849228641/22d0a/JCY5zZrWKqM.jpg", "width": 847, "height": 960, "text": "", "date": 1531057446, "lat": 56.226, "long": 93.514986, "access_key": "f8af1007c75bdc8c75"}}, {"type": "photo", "photo": {"id": 456250844, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c834202/v834202641/14f159/IWc1_CnMKb8.jpg", "photo_130": "https://pp.userapi.com/c834202/v834202641/14f15a/71bwlYQGXYI.jpg", "photo_604": "https://pp.userapi.com/c834202/v834202641/14f15b/o7bsr8TIBr8.jpg", "photo_807": "https://pp.userapi.com/c834202/v834202641/14f15c/5UEryIqh8G8.jpg", "photo_1280": "https://pp.userapi.com/c834202/v834202641/14f15d/DzRHh6mjjmg.jpg", "width": 960, "height": 720, "text": "", "date": 1531057446, "lat": 56.226076, "long": 93.514949, "access_key": "d7ee797a1d164fb91b"}}, {"type": "photo", "photo": {"id": 456250845, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c834202/v834202641/14f162/Zb2KN8us58k.jpg", "photo_130": "https://pp.userapi.com/c834202/v834202641/14f163/0cHG7gneUBY.jpg", "photo_604": "https://pp.userapi.com/c834202/v834202641/14f164/5P9XOg8Ex7g.jpg", "photo_807": "https://pp.userapi.com/c834202/v834202641/14f165/3SoNiUNuH0s.jpg", "photo_1280": "https://pp.userapi.com/c834202/v834202641/14f166/_e7_LGa4O90.jpg", "width": 720, "height": 960, "text": "", "date": 1531057446, "lat": 56.226076, "long": 93.514949, "access_key": "b1d6b67390bd4aea34"}}], "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 0, "groups_can_post": true, "can_post": 1}, "likes": {"count": 1, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 843}}, {"id": 45618, "from_id": -61006621, "owner_id": -61006621, "date": 1531064403, "marked_as_ads": 0, "post_type": "post", "text": "\u043e\u0442\u0434\u0430\u043c 26\u0440", "signer_id": 296641548, "attachments": [{"type": "photo", "photo": {"id": 456250846, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c849428/v849428910/2391a/1m9yd4uc9K8.jpg", "photo_130": "https://pp.userapi.com/c849428/v849428910/2391b/dnQgYrxQBxY.jpg", "photo_604": "https://pp.userapi.com/c849428/v849428910/2391c/jXn_2Nu-5pQ.jpg", "photo_807": "https://pp.userapi.com/c849428/v849428910/2391d/6NlqC4426kQ.jpg", "photo_1280": "https://pp.userapi.com/c849428/v849428910/2391e/9C5Sb0j72-o.jpg", "photo_2560": "https://pp.userapi.com/c849428/v849428910/2391f/a4yPnuBy3gE.jpg", "width": 1620, "height": 2160, "text": "", "date": 1531059357, "lat": 56.241253, "long": 93.545269, "access_key": "704e2ea525e09472a4"}}, {"type": "photo", "photo": {"id": 456250847, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c845123/v845123910/94a2e/Jd1klrCPvJg.jpg", "photo_130": "https://pp.userapi.com/c845123/v845123910/94a2f/BivE5PGJMdw.jpg", "photo_604": "https://pp.userapi.com/c845123/v845123910/94a30/YCjkIJ4q1_Q.jpg", "photo_807": "https://pp.userapi.com/c845123/v845123910/94a31/LFlnlMd0ImI.jpg", "photo_1280": "https://pp.userapi.com/c845123/v845123910/94a32/RtK0I3LatgQ.jpg", "photo_2560": "https://pp.userapi.com/c845123/v845123910/94a33/9VcLNJ8bb-4.jpg", "width": 1620, "height": 2160, "text": "", "date": 1531059357, "lat": 56.241253, "long": 93.545269, "access_key": "5e55d348f3916f7168"}}], "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 0, "groups_can_post": true, "can_post": 1}, "likes": {"count": 0, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 784}}, {"id": 45605, "from_id": -61006621, "owner_id": -61006621, "date": 1531031760, "marked_as_ads": 0, "post_type": "post", "text": "\u041e\u0442\u0434\u0430\u043c \u043c\u043e\u0436\u0435\u0442 \u043d\u0430\u0434\u043e \u043a\u043e\u043c\u0443", "signer_id": 34210140, "attachments": [{"type": "photo", "photo": {"id": 456250834, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c846524/v846524785/953a8/ZDgaFl_oLrE.jpg", "photo_130": "https://pp.userapi.com/c846524/v846524785/953a9/2KuTkingSSY.jpg", "photo_604": "https://pp.userapi.com/c846524/v846524785/953aa/N6hC580sBLI.jpg", "photo_807": "https://pp.userapi.com/c846524/v846524785/953ab/0v2uICqNf94.jpg", "photo_1280": "https://pp.userapi.com/c846524/v846524785/953ac/glDpOYMJoLM.jpg", "photo_2560": "https://pp.userapi.com/c846524/v846524785/953ad/O-4-VTx8HH0.jpg", "width": 1620, "height": 2160, "text": "", "date": 1531023767, "access_key": "bcb325c626702caf95"}}], "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 0, "groups_can_post": true, "can_post": 1}, "likes": {"count": 4, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 1277}}, {"id": 45604, "from_id": -61006621, "owner_id": -61006621, "date": 1531031755, "marked_as_ads": 0, "post_type": "post", "text": "\u041e\u0442\u0434\u0430\u043c \u0432\u0435\u0449\u0438. \u041f\u043e \u0432\u043e\u043f\u0440\u043e\u0441\u0430\u043c \u043e\u0431\u0440\u0430\u0449\u0430\u0442\u044c\u0441\u044f \u0432 \u041b\u0421.", "signer_id": 28024669, "attachments": [{"type": "photo", "photo": {"id": 456250835, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c844722/v844722474/9b70b/xa5XTmhUEaI.jpg", "photo_130": "https://pp.userapi.com/c844722/v844722474/9b70c/s24zvEIeE5Q.jpg", "photo_604": "https://pp.userapi.com/c844722/v844722474/9b70d/vtYaFUo01FA.jpg", "photo_807": "https://pp.userapi.com/c844722/v844722474/9b70e/PQCPUV94OP4.jpg", "photo_1280": "https://pp.userapi.com/c844722/v844722474/9b70f/N_XIwY3KhLI.jpg", "photo_2560": "https://pp.userapi.com/c844722/v844722474/9b710/ZL7Mk8E5CHQ.jpg", "width": 2560, "height": 1920, "text": "\u0420\u0430\u0437\u043c\u0435\u0440 42-44", "date": 1531027304, "access_key": "a80b13adbb3cd5b0a7"}}, {"type": "photo", "photo": {"id": 456250836, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c844722/v844722474/9b701/VygAKhgTZ2M.jpg", "photo_130": "https://pp.userapi.com/c844722/v844722474/9b702/F3zMOtQuXIM.jpg", "photo_604": "https://pp.userapi.com/c844722/v844722474/9b703/cbrdIsjpCe4.jpg", "photo_807": "https://pp.userapi.com/c844722/v844722474/9b704/4qyKw6NYZpw.jpg", "photo_1280": "https://pp.userapi.com/c844722/v844722474/9b705/UFvoy9E5PzA.jpg", "photo_2560": "https://pp.userapi.com/c844722/v844722474/9b706/rfIsGb2v4Dg.jpg", "width": 2560, "height": 1920, "text": "\u0420\u0430\u0437\u043c\u0435\u0440 42-44", "date": 1531027304, "access_key": "25817f585bc5d6aa24"}}, {"type": "photo", "photo": {"id": 456250837, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c844722/v844722474/9b6f7/bDPixDDiGPw.jpg", "photo_130": "https://pp.userapi.com/c844722/v844722474/9b6f8/8dGHW4HiU_4.jpg", "photo_604": "https://pp.userapi.com/c844722/v844722474/9b6f9/4536MNgVTuA.jpg", "photo_807": "https://pp.userapi.com/c844722/v844722474/9b6fa/ZVPTTPE-JYU.jpg", "photo_1280": "https://pp.userapi.com/c844722/v844722474/9b6fb/qfBvAiIvR5c.jpg", "photo_2560": "https://pp.userapi.com/c844722/v844722474/9b6fc/W9A14HdgBrg.jpg", "width": 2560, "height": 1920, "text": "\u0428\u0442\u0430\u043d\u044b \u0443\u0442\u0435\u043f\u043b\u0435\u043d\u043d\u044b\u0435 \u043d\u0430 \u0444\u043b\u0438\u0441\u0435. \u0420\u0430\u0437\u043c\u0435\u0440 38-40.\n\u041a\u043e\u0444\u0442\u0430 - \u0440\u0430\u0437\u043c\u0435\u0440 42.", "date": 1531027304, "access_key": "538e08d48e491a09e9"}}], "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 1, "groups_can_post": true, "can_post": 1}, "likes": {"count": 2, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 1073}}, {"id": 45603, "from_id": -61006621, "owner_id": -61006621, "date": 1531031751, "marked_as_ads": 0, "post_type": "post", "text": "\u041e\u0442\u0434\u0430\u043c \u0434\u0430\u0440\u043e\u043c,\u0441\u0442\u0430\u0440\u043e\u0435 \u043a\u0440\u0435\u0441\u043b\u043e \u043d\u0430 \u0434\u0430\u0447\u0443,\u0441\u0430\u043c\u043e\u0432\u044b\u0432\u043e\u0437 ,\u0432\u0441\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u044b \u043f\u043e \u0442 .89232191096.", "signer_id": 317325265, "attachments": [{"type": "photo", "photo": {"id": 456250838, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c824411/v824411812/184278/7EjzpR5KT78.jpg", "photo_130": "https://pp.userapi.com/c824411/v824411812/184279/Km_7WnAG7tY.jpg", "photo_604": "https://pp.userapi.com/c824411/v824411812/18427a/dR03T4mHrkQ.jpg", "photo_807": "https://pp.userapi.com/c824411/v824411812/18427b/UkI2o8WjSAs.jpg", "photo_1280": "https://pp.userapi.com/c824411/v824411812/18427c/vLevI9JBxgw.jpg", "photo_2560": "https://pp.userapi.com/c824411/v824411812/18427d/iOYcGFCJOq4.jpg", "width": 1080, "height": 1800, "text": "", "date": 1531031609, "access_key": "010d91fecccc8ba85a"}}, {"type": "photo", "photo": {"id": 456250839, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://sun9-9.userapi.com/c834204/v834204812/186ce3/h1a76A_nuEo.jpg", "photo_130": "https://sun9-7.userapi.com/c834204/v834204812/186ce4/PducVEcTtXo.jpg", "photo_604": "https://sun9-4.userapi.com/c834204/v834204812/186ce5/_OAusqCr5eM.jpg", "photo_807": "https://sun9-8.userapi.com/c834204/v834204812/186ce6/OauVC_pnF_o.jpg", "photo_1280": "https://sun9-9.userapi.com/c834204/v834204812/186ce7/r4brGN_izkM.jpg", "photo_2560": "https://sun9-3.userapi.com/c834204/v834204812/186ce8/YcLe2h090Xc.jpg", "width": 1080, "height": 1800, "text": "", "date": 1531031609, "access_key": "404c5587d3d97b3411"}}], "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 0, "groups_can_post": true, "can_post": 1}, "likes": {"count": 1, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 997}}, {"id": 45580, "from_id": -61006621, "owner_id": -61006621, "date": 1530963156, "marked_as_ads": 0, "post_type": "post", "text": "39 \u0440\u0430\u0437\u043c\u0435\u0440", "signer_id": 266234913, "attachments": [{"type": "photo", "photo": {"id": 456250830, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c844521/v844521324/7c836/QLPbU1IYt1U.jpg", "photo_130": "https://pp.userapi.com/c844521/v844521324/7c837/Np98xmLfPUY.jpg", "photo_604": "https://pp.userapi.com/c844521/v844521324/7c838/o8xQBkuVvoY.jpg", "photo_807": "https://pp.userapi.com/c844521/v844521324/7c839/2QC84ndQExI.jpg", "photo_1280": "https://pp.userapi.com/c844521/v844521324/7c83a/RLBbDKy0cog.jpg", "photo_2560": "https://pp.userapi.com/c844521/v844521324/7c83b/d0hz9zqdofo.jpg", "width": 1620, "height": 2160, "text": "", "date": 1530962533, "post_id": 45576, "access_key": "1a14111b0eedb7b4dd"}}], "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 2, "groups_can_post": true, "can_post": 1}, "likes": {"count": 0, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 1318}}, {"id": 45572, "from_id": -61006621, "owner_id": -61006621, "date": 1530962339, "marked_as_ads": 0, "post_type": "post", "text": "\u041e\u0442\u0434\u0430\u043c \u043a\u0440\u0435\u0441\u043b\u043e. \u0441.\u0442. 8 902 942 5999 (\u043f\u043e\u0441\u043b\u0435 14-00 )", "signer_id": 187411503, "attachments": [{"type": "photo", "photo": {"id": 456250828, "album_id": -7, "owner_id": -61006621, "user_id": 100, "photo_75": "https://pp.userapi.com/c834104/v834104811/188d65/gwiWye3RSoA.jpg", "photo_130": "https://pp.userapi.com/c834104/v834104811/188d66/4JesGGL0MLI.jpg", "photo_604": "https://pp.userapi.com/c834104/v834104811/188d67/fSqT82mHc10.jpg", "photo_807": "https://pp.userapi.com/c834104/v834104811/188d68/qKepXy7x_fs.jpg", "photo_1280": "https://pp.userapi.com/c834104/v834104811/188d69/ea57CuCFE88.jpg", "photo_2560": "https://pp.userapi.com/c834104/v834104811/188d6a/BHF171Dmado.jpg", "width": 1620, "height": 2160, "text": "", "date": 1530961046, "access_key": "dd6b200698ce9a57dc"}}], "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 0, "groups_can_post": true, "can_post": 1}, "likes": {"count": 0, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 1173}}, {"id": 45564, "from_id": -61006621, "owner_id": -61006621, "date": 1530936269, "marked_as_ads": 0, "post_type": "post", "text": "\u041e\u0442\u0434\u0430\u043c \u0442\u0440\u043e\u0439\u043d\u0438\u043a \u0441 \u0445\u0432\u043e\u0441\u0442\u043e\u043c \u043c\u0435\u0442\u0440\u0430 \u0434\u0432\u0430. \n\u041a\u0440\u043e\u043b\u0438\u043a \u043f\u0435\u0440\u0435\u0433\u0440\u044b\u0437 \u043f\u0440\u043e\u0432\u043e\u0434, \u043f\u0440\u0438\u0448\u043b\u043e\u0441\u044c \u043e\u0442\u0440\u0435\u0437\u0430\u0442\u044c \u0432\u0438\u043b\u043a\u0443. :)))\n\u0423\u043c\u0435\u043b\u044c\u0446\u044b \u043b\u0435\u0433\u043a\u043e  \u043f\u0440\u0438\u043a\u0440\u0443\u0442\u044f\u0442 \u0432\u0438\u043b\u043a\u0443 \u0438 \u043c\u043e\u0436\u043d\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u044c\u0441\u044f.", "signer_id": 227037173, "post_source": {"type": "api", "platform": "android"}, "comments": {"count": 0, "groups_can_post": true, "can_post": 1}, "likes": {"count": 0, "user_likes": 0, "can_like": 1, "can_publish": 1}, "reposts": {"count": 0, "user_reposted": 0}, "views": {"count": 1267}}]}
'''
JSON_TINGLI = '''[{"word":{"id":"e3d11321-532d-42ea-b422-ad4cf2d77d4c","word":"你","transcription":[],"created_at":"2024-07-11T08:33:59Z","examples":["你好。|nǐ hǎo.|Привет.","你吃饭了吗？|nǐ chīfàn le ma?|Ты уже ел(а)?","你是哪里人？|nǐ shì nǎlǐ rén?|Откуда ты?"],"word_type":null,"word_comment":"","meta_data":{"translation":"ты, вы (вежливо)"}},"student_word":null,"similar_words":null,"word_list_id":[],"translations":[{"dictionary_id":"e3d11321-532d-42ea-b422-ad4cf2d77d4c","left_words":"你","left_lang":"zh","right_words":null,"right_pos":"noun","right_lang":"ru","left_order_num":null}],"attachments":[],"examples":[{"pinyin":"nǐ hǎo.","phrase":"你好。","translation":"Привет."},{"pinyin":"nǐ chīfàn le ma?","phrase":"你吃饭了吗？","translation":"Ты уже ел(а)?"},{"pinyin":"nǐ shì nǎlǐ rén?","phrase":"你是哪里人？","translation":"Откуда ты?"}],"radical":null,"hieroglyphs":[{"word":{"id":"e3d11321-532d-42ea-b422-ad4cf2d77d4c","word":"你","transcription":[],"created_at":"2024-07-11T08:33:59Z","examples":["你好。|nǐ hǎo.|Привет.","你吃饭了吗？|nǐ chīfàn le ma?|Ты уже ел(а)?","你是哪里人？|nǐ shì nǎlǐ rén?|Откуда ты?"],"word_type":null,"word_comment":"","meta_data":{"translation":"ты, вы (вежливо)"}},"student_word":null,"similar_words":null,"word_list_id":null,"translations":[{"dictionary_id":"e3d11321-532d-42ea-b422-ad4cf2d77d4c","left_words":"你","left_lang":"zh","right_words":"ты","right_pos":"noun","right_lang":"ru","left_order_num":0}],"attachments":[],"examples":[{"pinyin":"nǐ hǎo.","phrase":"你好。","translation":"Привет."},{"pinyin":"nǐ chīfàn le ma?","phrase":"你吃饭了吗？","translation":"Ты уже ел(а)?"},{"pinyin":"nǐ shì nǎlǐ rén?","phrase":"你是哪里人？","translation":"Откуда ты?"}],"radical":null,"hieroglyphs":null,"children":null,"parent":null,"type_open_card":null}],"children":[{"word":{"id":"1ebe5502-c52c-4231-93a8-b2af39a793a1","word":"小","transcription":[],"created_at":"2024-07-05T18:23:08Z","examples":["这是个小房间。|zhè shì gè xiǎo fángjiān|Это маленькая комната.","小明是个小男孩。|xiǎo míng shì gè xiǎo nánháir|Сяо Минь — маленький мальчик.","我喜欢小猫。|wǒ xǐhuān xiǎo māo|Мне нравятся маленькие котята."],"word_type":null,"word_comment":null,"meta_data":{"translation":"маленький, небольшой, молодой, юный"}},"student_word":null,"similar_words":null,"word_list_id":null,"translations":[{"dictionary_id":"1ebe5502-c52c-4231-93a8-b2af39a793a1","left_words":"小","left_lang":"zh","right_words":"маленький","right_pos":"noun","right_lang":"ru","left_order_num":0},{"dictionary_id":"1ebe5502-c52c-4231-93a8-b2af39a793a1","left_words":"小","left_lang":"zh","right_words":" небольшой","right_pos":"noun","right_lang":"ru","left_order_num":1}],"attachments":null,"examples":null,"radical":null,"hieroglyphs":null,"children":null,"parent":{"id":"e3d11321-532d-42ea-b422-ad4cf2d77d4c","word":"你","transcription":[],"created_at":"2024-07-11T08:33:59Z","examples":["你好。|nǐ hǎo.|Привет.","你吃饭了吗？|nǐ chīfàn le ma?|Ты уже ел(а)?","你是哪里人？|nǐ shì nǎlǐ rén?|Откуда ты?"],"word_type":null,"word_comment":"","meta_data":{"translation":"ты, вы (вежливо)"}},"type_open_card":null},{"word":{"id":"9f4ae782-6dac-4f03-959e-ae95b2d8b638","word":"亻","transcription":[],"created_at":"2024-07-05T18:23:08Z","examples":[],"word_type":null,"word_comment":"","meta_data":null},"student_word":null,"similar_words":null,"word_list_id":null,"translations":[{"dictionary_id":"9f4ae782-6dac-4f03-959e-ae95b2d8b638","left_words":"亻","left_lang":"zh","right_words":"человек","right_pos":"adjective","right_lang":"ru","left_order_num":0}],"attachments":null,"examples":null,"radical":null,"hieroglyphs":null,"children":null,"parent":{"id":"e3d11321-532d-42ea-b422-ad4cf2d77d4c","word":"你","transcription":[],"created_at":"2024-07-11T08:33:59Z","examples":["你好。|nǐ hǎo.|Привет.","你吃饭了吗？|nǐ chīfàn le ma?|Ты уже ел(а)?","你是哪里人？|nǐ shì nǎlǐ rén?|Откуда ты?"],"word_type":null,"word_comment":"","meta_data":{"translation":"ты, вы (вежливо)"}},"type_open_card":null}],"parent":null,"type_open_card":null}]'''
JOIN_PROFILE='''{"user_id": "user_id", "id": "01K80NK1WMEQ9JNZCDR82J5TPT", "is_deleted": false, "time_zone": "Europe/Moscow", "country_id": null, "first_name": null, "surname": null, "patronymic": null, "birth_date": null, "description": null, "sex": null, "social_network": null, "email": "new_user_id@sdfsdf.ui", "phone": null, "worked_at": null, "education": null, "price": null, "lang_level": null, "working_time": {"monday": [["12:00", "13:00"]]}, "code_to_find": null, "settings": null}'''
@dataclass(frozen=True)
class JsonList(UJsonMixin):
    x: List[int]


@dataclass(frozen=True)
class JsonSimple(UJsonMixin):
    x: int

class EnumType(enum.IntEnum):
    Two = 2
    One = 1

@dataclass(frozen=True)
class JsonSimpleEnum(UJsonMixin):
    x: EnumType

class EnumStrType(enum.StrEnum):
    Two = "two"
    One = "one"

@dataclass(frozen=True)
class JsonSimpleEnumStr(UJsonMixin):
    x: EnumStrType

@dataclass(frozen=True)
class JsonSimpleDateTime(UJsonMixin):
    dt: datetime

@dataclass(frozen=True)
class JsonSimpleSkip(UJsonMixin):
    x: int
    _x: int


@dataclass(frozen=True)
class JsonSimplNested(UJsonMixin):
    x: JsonSimple

@dataclass(frozen=True)
class JsonDict(UJsonMixin):
    x: Dict[str, int]


@dataclass(frozen=True)
class JsonNoTypingDict(UJsonMixin):
    x: dict


@dataclass(frozen=True)
class JsonNoTypingList(UJsonMixin):
    x: list


@dataclass(frozen=True)
class JsonNested(UJsonMixin):
    a: JsonSimple
    b: JsonList
    c: Optional[JsonNoTypingDict]


@dataclass(frozen=True)
class JsonUnion(UJsonMixin):
    a: Union[str, int]
    b: Union[dict, list]
    c: Union[Dict[str, int], List[int]]


@dataclass(frozen=True)
class JsonListNested(UJsonMixin):
    a: JsonSimple
    b: List[JsonList]
    c: List[JsonNoTypingDict]


@dataclass(frozen=True)
class JsonSimpleOptional(UJsonMixin):
    x: int
    y: Optional[int]

@dataclass(frozen=True)
class JsonSimpleOptionalV2(UJsonMixin):
    x: int
    y: int | None


@dataclass(frozen=True)
class JsonSimpleNotOptional(UJsonMixin):
    x: int
    y: int


@dataclass(frozen=True)
class WallAttachmentPhoto(UJsonMixin):
    id: int
    album_id: int
    owner_id: int
    user_id: int
    width: int
    height: int
    text: str
    date: int
    access_key: str
    photo_75: str
    photo_130: str
    photo_604: str
    photo_807: str
    photo_1280: str


@dataclass(frozen=True)
class WallAttachment(UJsonMixin):
    type: str
    photo: WallAttachmentPhoto


@dataclass(frozen=True)
class WallItem(UJsonMixin):
    id: int
    from_id: int
    owner_id: int
    date: int
    marked_as_ads: int
    post_type: str
    text: str
    can_pin: Optional[bool]
    attachments: List[WallAttachment]


@dataclass(frozen=True)
class WallResponse(UJsonMixin):
    count: int
    items: List[WallItem]

class WordType(enum.StrEnum):
    MeasureWord = "measure_word"

@dataclass(frozen=True)
class WordSource(UJsonMixin):
    id: str
    word: str
    transcription: List[str] 
    created_at: str
    examples: List[str] 
    word_type: Optional[WordType] = None
    word_comment: Optional[str] = None
    meta_data: Optional[dict] = None

class UserWordStatus(enum.IntEnum):
    Excellent = 5
    Good = 4
    Normal = 3
    Bad = 2
    VeryBad = 1
    NotStarted = 0

@dataclass(frozen=True)
class UserWord(UJsonMixin):
    id: str
    dictionary_id: str
    word: str
    student_profile_id: str
    word_source: WordSource

    created_at: datetime 

    how_well_remember: UserWordStatus 
    lesson_revision_id: Optional[str] = None
    is_deleted: bool = False
    examples: Optional[List[str]] = None
    parent_word: Optional[str] = None
    not_only_radical: Optional[bool] = None
    card: Optional[Dict] = None
    card_due_repeat_at: Optional[datetime] = None


@dataclass
class RadicalBase(UJsonMixin):
    word: str
    pinyin: str
    side_writing: str | None
    upper_writing: str | None
    lower_writing: str | None
    alternative_writing: str | None
    full_writing: str | None
    comment: str | None
    translation: str | None


@dataclass(frozen=True)
class ExamplePhrase(UJsonMixin):
    pinyin: str
    phrase: str
    translation: str

class Languages(enum.StrEnum):
    EN = "en"
    RU = "ru"

class PartOfSpeech(enum.StrEnum):
    NOUN   = "noun"
    VERB   = "verb"
    ADJ    = "adj"

class WordAttachmentType(enum.StrEnum):
    IMAGE   = "image"
    AUDIO   = "audio"
    VIDEO   = "video"

@dataclass(eq=False)
class WordTranslation:
    dictionary_id: str
    left_word: str | None
    left_lang: Languages | None
    right_word: str | None
    right_pos: PartOfSpeech | None
    right_lang: Languages | None
    left_order_num: int | None


@dataclass(eq=False)
class WordAttachmentRecord(UJsonMixin):
    id: str
    dictionary_id: str
    word: str
    attachment_id: str
    word_attachment_type: Optional[WordAttachmentType] = None
    order_num: int = 0
    is_deleted: bool = False
    student_profile_id: Optional[str] = None


@dataclass
class RadicalWithAttachment(RadicalBase):
    attachment: WordAttachmentRecord | None


@dataclass(frozen=True)
class ChineseWordDetailBase(UJsonMixin):
    word: WordSource
    student_word: Optional[UserWord] = None
    similar_words: Optional[list[WordSource]] = None
    word_list_id: Optional[list[str]] = None
    radical: Optional[RadicalWithAttachment] = None
    translations: Optional[list[WordTranslation]] = None
    examples: Optional[list[str]] = None
    parent: Optional[WordSource] = None
    children: Optional[list["ChineseWordDetailBase"]] = None


@dataclass(eq=False)
class MediaAttachment(UJsonMixin):
    size: int
    storage_driver_name: str
    path: str
    media_type: str
    created_by: str
    content_type: str
    id: str
    created_at: datetime
    updated_at: datetime
    is_deleted: bool = False


@dataclass(frozen=True)
class ChineseWordDetailBase(UJsonMixin):
    word: WordSource
    student_word: Optional[UserWord] = None
    similar_words: Optional[list[WordSource]] = None
    word_list_id: Optional[list[str]] = None
    radical: Optional[RadicalWithAttachment] = None
    examples: Optional[list[str]] = None
    parent: Optional[WordSource] = None
    children: Optional[list["ChineseWordDetailBase"]] = None

@dataclass(frozen=True)
class ChineseWordDetail(ChineseWordDetailBase):
    attachments: Optional[list[MediaAttachment]] = None
    word_attachments: Optional[list[WordAttachmentRecord]] = None
    translations: Optional[list[WordTranslation]] = None


@dataclass(eq=False)
class MediaAttachment(UJsonMixin):
    size: int
    storage_driver_name: str
    path: str
    media_type: str
    created_by: str
    content_type: str
    id: str
    created_at: datetime
    updated_at: datetime
    is_deleted: bool = False


@dataclass(frozen=True)
class ChineseWordDetailV2(UJsonMixin):
    translations: list[WordTranslation]

@dataclass(frozen=True)
class ChineseWordDetailV3(UJsonMixin):
    translations: list[WordTranslation] | None

WorkingType: TypeAlias = dict[str, Optional[list[list[str]]]]

@dataclass(frozen=True)
class Profile(UJsonMixin):
    user_id: str 
    id: str 
    working_time: Optional[WorkingType]

@dataclass(frozen=True)
class ProfileV2(UJsonMixin):
    user_id: str 
    id: str 
    working_time: WorkingType

@dataclass(frozen=True)
class ProfileV3(UJsonMixin):
    user_id: str 
    id: str 
    working_time: WorkingType | None