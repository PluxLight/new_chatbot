from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from app import menu_data
from app import response_manage

from django.http import JsonResponse

@csrf_exempt
def menu_up(request):
    menu = menu_data.menu()
    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)

    user_key = received_json['userRequest']['user']['properties']['plusfriendUserKey']

    r_m = response_manage.key_manage() #플러스친구 고유 키 값 관리

    user_value = received_json['action']['detailParams']['학생식당']['value']
    #print(user_value)

    pre_input_text = r_m.pre_value(user_key)  # 사용자가 한단계전에 입력한 값을 변수에 저장
    pre_pre_input_text = r_m.pre_pre_value(user_key)  # 사용자가 두단계전에 입력한 값을 변수에 저장
    r_m.key_insert(user_key, user_value)  # 사용자가 현재 입력한 값을 DB에 저장

    if pre_input_text == '내일의 메뉴':
        if user_value == '채움관':
            return_text = menu.cheaum_tomorrow()
        elif user_value == '이룸관':
            return_text = menu.erum_tomorrow()
        elif user_value == '기숙사':
            return_text = menu.domitori_tomorrow()
    else:
        if user_value == '채움관':
            return_text = menu.cheaum()
        elif user_value == '이룸관':
            return_text = menu.erum()
        elif user_value == '양식당':
            return_text = menu.restaurant()
        elif user_value == '맘스터치(치킨)':
            return_text = menu.moms('치킨')
        elif user_value == '맘스터치(버거)':
            return_text = menu.moms('버거')
        elif user_value == '맘스터치(스낵)':
            return_text = menu.moms('스낵')
        elif user_value == '기숙사':
            return_text = menu.domitori()

    return JsonResponse(
        {
            'version': "2.0",
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': return_text
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

@csrf_exempt
def first_time(request):
    return JsonResponse(
        {
            'version': "2.0",
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': '처음으로 돌아갑니다 \n\n※공지※ 안동대학식봇은 19년 1학기이후 종료할 예정입니다. 자세한 사항은 학식봇 홈페이지를 참고바랍니다'
                        }
                    }
                ],
                "quickReplies": [
                    {
                        'action': 'message',
                        "label": "채움관",
                        "messageText": "채움관"
                    },
                    {
                        'action': 'message',
                        "label": "이룸관",
                        "messageText": "이룸관"
                    },
                    {
                        'action': 'message',
                        "label": "양식당",
                        "messageText": "양식당"
                    }
                ]
            }
        }
    )

@csrf_exempt
def tomorrow_menu(request):
    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)

    user_key = received_json['userRequest']['user']['properties']['plusfriendUserKey']

    r_m = response_manage.key_manage()  # 플러스친구 고유 키 값 관리

    user_value = received_json['userRequest']['utterance']
    # print(user_value)

    pre_input_text = r_m.pre_value(user_key)  # 사용자가 한단계전에 입력한 값을 변수에 저장
    pre_pre_input_text = r_m.pre_pre_value(user_key)  # 사용자가 두단계전에 입력한 값을 변수에 저장
    r_m.key_insert(user_key, user_value)  # 사용자가 현재 입력한 값을 DB에 저장

    return JsonResponse(
        {
            'version': "2.0",
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': '장소를 선택하세요'
                        }
                    }
                ],
                "quickReplies": [
                    {
                        'action': 'message',
                        "label": "채움관",
                        "messageText": "채움관"
                    },
                    {
                        'action': 'message',
                        "label": "이룸관",
                        "messageText": "이룸관"
                    },
                    {
                        'action': 'message',
                        "label": "기숙사",
                        "messageText": "기숙사"
                    },
                    {
                        'action': 'message',
                        "label": "🏠처음으로",
                        "messageText": "처음으로"
                    }
                ]
            }
        }
    )

@csrf_exempt
def peri_list(request):
    menu = menu_data.menu()
    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)

    return_text = menu.restaurant_list('리스트')

    return JsonResponse(
        {
            'version': "2.0",
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': return_text
                        }
                    }
                ],
                "quickReplies": [
                    {
                        'action': 'block',
                        "label": "🔎검색하기",
                        "messageText": "검색하기"
                    },
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

@csrf_exempt
def bistro(request):
    menu = menu_data.menu()
    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)

    user_value = received_json['action']['detailParams']['교외식당리스트']['value']
    # print(user_value)

    return_text = menu.restaurant_list(user_value)

    return JsonResponse(
        {
            'version': "2.0",
            'template': {
                'outputs': [
                    {
                        'simpleText': {
                            'text': return_text
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


def dummy():
    {
        "contents": [
            {
                "type": "card.image",
                "cards": [
                    {
                        "imageUrl": "http://cfile22.uf.tistory.com/image/23390C4752A91485368E42"
                    }
                ]
            },
            {
                "type": "card.image",
                "cards": [
                    {
                        "title": "card.image 풀스펙",
                        "imageUrl": "http://catory.kr/files/attach/images/220/509/001/5e25851e432ce5b129d3d7d1886b5566.jpg",
                        "description": "준말은 발음 그대로 괭이. 비슷하게 고앵이, 꼬내기라고 부르는 지방도 있다. 남부, 제주도 사투리론 고냉이다.[10] 고내이, 앵고, 구이, 궤데기, 개냉이, 괭이, 야옹개, 개이 등, 남쪽으로 갈수록 변형이 심하다. 2011년 9월 1일부터 복수 표준어에 포함된 개발새발의 원조 괴발개발(관련 기사)의 '괴'가 고양이를 가리키는 말이다. 그리고 살찐이라 부르는 지역이 뜻밖에 많다.",
                        "linkUrl": {},
                        "buttons": [
                            {
                                "type": "url",
                                "label": "더보기",
                                "data": {
                                    "url": "http://www.melon.com"
                                }
                            },
                            {
                                "type": "url",
                                "label": "재생하기",
                                "data": {
                                    "url": "http://www.naver.com"
                                }
                            }
                        ]
                    }
                ]
            },
            {
                "type": "card.image",
                "cards": [
                    {
                        "title": "card.image 풀스펙",
                        "imageUrl": "http://pet.chosun.com/images/news/healthchosun_pet_201709/20170913132138_1364_3824_4532.jpg",
                        "description": "준말은 발음 그대로 괭이. 비슷하게 고앵이, 꼬내기라고 부르는 지방도 있다. 남부, 제주도 사투리론 고냉이다.[10] 고내이, 앵고, 구이, 궤데기, 개냉이, 괭이, 야옹개, 개이 등, 남쪽으로 갈수록 변형이 심하다. 2011년 9월 1일부터 복수 표준어에 포함된 개발새발의 원조 괴발개발(관련 기사)의 '괴'가 고양이를 가리키는 말이다. 그리고 살찐이라 부르는 지역이 뜻밖에 많다.",
                        "linkUrl": {},
                        "buttons": [
                            {
                                "type": "url",
                                "label": "더보기",
                                "data": {
                                    "url": "http://www.melon.com"
                                }
                            },
                            {
                                "type": "url",
                                "label": "재생하기",
                                "data": {
                                    "url": "http://www.naver.com"
                                }
                            }
                        ]
                    },
                    {
                        "title": "card.image 풀스펙",
                        "imageUrl": "https://memeguy.com/photos/images/the-only-lolcat-to-ever-make-me-literally-lol-17667.jpg",
                        "description": "특이한 점으로 균형 감각이 좋은 편이다. 이는 귀 속의 반고리관 안에 섬모라는 털이 있어서 고양이가 움직일 때 반고리관 내의 액체의 유동을 잘 감지하기 때문. 정교한 컨트롤이 가능한 꼬리 역시 균형 감각에 한몫한다. 덕분에 매우 좁은 담 위도 잘 걷고 높은 곳에서 떨어져도 잘 착지한다. 충격을 분산하기에 적합한 신체구조를 가져 충격을 최소화할 수 있다. 고양이가 개보다 쉽게 높은 담을 자유자재로 넘나들고 캣타워 등의 구조물도 올라가길 좋아하며, 대형 고양잇과인 표범 등이 나무에서 무리 없이 지내는 것도 평형감각이 뛰어나고 실수로 떨어져도 별걱정 없기 때문이다.",
                        "linkUrl": {},
                        "buttons": [
                            {
                                "type": "url",
                                "label": "더보기",
                                "data": {
                                    "url": "http://www.melon.com"
                                }
                            },
                            {
                                "type": "url",
                                "label": "재생하기",
                                "data": {
                                    "url": "http://www.naver.com"
                                }
                            }
                        ]
                    },
                    {
                        "title": "card.image 풀스펙",
                        "imageUrl": "https://longlivethekitty.com/wp-content/uploads/lolcat_airplane.jpg",
                        "description": "여러 품종이 뚜렷하게 구분되고 크기도 소형/중형/대형으로 분류되는 개와는 달리, 겉모습만으로 품종을 구분하기가 쉽지 않다. 물론, 한눈에 알아볼 수 있는 품종도 있다. 꽤 오래전부터 용도에 따라 품종을 개발한 개와는 달리, 고양이는 가축화 이후 쥐를 잡는 용도로만 이용되어 품종 개발 기간이 매우 짧아서, 상대적으로 유전적 다양성이 높고 환경 적응력 등이 뛰어나다고 한다.",
                        "linkUrl": {},
                        "buttons": [
                            {
                                "type": "url",
                                "label": "더보기",
                                "data": {
                                    "url": "http://www.melon.com"
                                }
                            },
                            {
                                "type": "url",
                                "label": "재생하기",
                                "data": {
                                    "url": "http://www.naver.com"
                                }
                            }
                        ]
                    },
                    {
                        "title": "card.image 풀스펙",
                        "imageUrl": "https://vignette.wikia.nocookie.net/meme/images/f/f6/Imaclolcat.jpg/revision/latest?cb=20081218101859",
                        "description": "인간에게 친숙한 동물임에도 강아지나 송아지처럼 어린 개체를 따로 칭하는 명사가 우리말에 없는 것이 다소 특이하다. (영어 등의 외국어에는 kitten 등 어린 고양이를 칭하는 명사가 있다.) 최근 고양이 애호가들에 의해 아기 고양이를 칭하는 아깽이라는 신조어가 만들어졌다.",
                        "linkUrl": {},
                        "buttons": [
                            {
                                "type": "url",
                                "label": "더보기",
                                "data": {
                                    "url": "http://www.melon.com"
                                }
                            },
                            {
                                "type": "url",
                                "label": "재생하기",
                                "data": {
                                    "url": "http://www.naver.com"
                                }
                            }
                        ]
                    }
                ]
            }
        ],
        "quickReplies": [
            {
                "type": "text",
                "label": "이미지카드 소스",
                "message": "이미지카드 소스"
            },
            {
                "type": "text",
                "label": "데모",
                "message": "데모"
            },
            {
                "type": "text",
                "label": "텍스트카드",
                "message": "텍스트카드"
            },
            {
                "type": "text",
                "label": "커머스카드",
                "message": "커머스카드"
            },
            {
                "type": "text",
                "label": "뮤직카드",
                "message": "뮤직카드"
            },
            {
                "type": "text",
                "label": "리스트카드",
                "message": "리스트카드"
            }
        ]
    }