import requests
from bs4 import BeautifulSoup

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

def room_data():
    url = 'http://www.anu.ac.kr/main/board/index.do?menu_idx=80&manage_idx=8'

    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'lxml')

    room_list = []
    room_num_list = []
    room_url_list = []
    room_date_list = []

    room = soup.select(
        'table > tbody > tr'
    )

    for i in room:
        room_list.append(i.get('title'))

    # room_num = soup.find_all("table",{"class": "subject"})

    room_num = soup.select(
        'table > tbody > tr > td > a'
    )

    for i in room_num:
        room_num_int = i.get('onclick').split('(')[1]
        room_num_int = int(room_num_int.split(')')[0])
        room_num_list.append(room_num_int)

    room_num_list = list(set(room_num_list))
    room_num_list.sort(reverse=True)

    for i in room_num_list:
        room_url = 'http://www.andong.ac.kr/main/board/view.do?menu_idx=80&manage_idx=8&board_idx=' + str(i)
        room_url_list.append(room_url)


    room_date = soup.find('table').find_all("td", {"class": "date"})
    for i in room_date:
        room_date_data = str(i).split('>')[1]
        room_date_data = room_date_data.split('<')[0]
        room_date_list.append(room_date_data)

    room_str = '자취/하숙 정보는 \n안동대학교 홈페이지에 작성된\n게시글을 중개하고 있습니다\n\n\n게시글 / 작성일\n'
    for i in range(len(room_list)):
        room_str += '%s / %s\n%s\n\n' % (room_list[i], room_date_list[i],room_url_list[i])

    return room_list, room_date_list, room_url_list

@csrf_exempt
def room_print(request):
    room_list, room_date_list, room_url_list = room_data()

    return JsonResponse(
        {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "📅  " + room_date_list[0],
                                    "description": room_list[0],
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "URL 연결",
                                            "webLinkUrl": room_url_list[0]
                                        }
                                    ]
                                },
                                {
                                    "title": "📅  " + room_date_list[1],
                                    "description": room_list[1],
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "URL 연결",
                                            "webLinkUrl": room_url_list[1]
                                        }
                                    ]
                                },
                                {
                                    "title": "📅  " + room_date_list[2],
                                    "description": room_list[2],
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "URL 연결",
                                            "webLinkUrl": room_url_list[2]
                                        }
                                    ]
                                },
                                {
                                    "title": "📅  " + room_date_list[3],
                                    "description": room_list[3],
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "URL 연결",
                                            "webLinkUrl": room_url_list[3]
                                        }
                                    ]
                                },
                                {
                                    "title": "📅  " + room_date_list[4],
                                    "description": room_list[4],
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "URL 연결",
                                            "webLinkUrl": room_url_list[4]
                                        }
                                    ]
                                },
                                {
                                    "title": "📅  " + room_date_list[5],
                                    "description": room_list[5],
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "URL 연결",
                                            "webLinkUrl": room_url_list[5]
                                        }
                                    ]
                                },
                                {
                                    "title": "📅  " + room_date_list[6],
                                    "description": room_list[6],
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "URL 연결",
                                            "webLinkUrl": room_url_list[6]
                                        }
                                    ]
                                },
                                {
                                    "title": "📅  " + room_date_list[7],
                                    "description": room_list[7],
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "URL 연결",
                                            "webLinkUrl": room_url_list[7]
                                        }
                                    ]
                                },
                                {
                                    "title": "📅  " + room_date_list[8],
                                    "description": room_list[8],
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "URL 연결",
                                            "webLinkUrl": room_url_list[8]
                                        }
                                    ]
                                },
                                {
                                    "title": "📅  " + room_date_list[9],
                                    "description": room_list[9],
                                    "buttons": [
                                        {
                                            "action": "webLink",
                                            "label": "URL 연결",
                                            "webLinkUrl": room_url_list[9]
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                ],
                "quickReplies": [
                    {
                        'action': 'message',
                        "label": "🍴교내식당",
                        "messageText": "교내식당"
                    },
                    {
                        'action': 'message',
                        "label": "🍽교외식당",
                        "messageText": "교외식당"
                    },
                    {
                        'action': 'message',
                        "label": "☁날씨확인",
                        "messageText": "날씨확인"
                    },
                    {
                        'action': 'message',
                        "label": "🏘자취방 확인",
                        "messageText": "자취방 확인"
                    }
                ]
            }
        }
    )