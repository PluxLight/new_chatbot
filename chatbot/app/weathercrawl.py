from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%95%88%EB%8F%99%EC%8B%9C+%EC%86%A1%EC%B2%9C%EB%8F%99+%EB%82%A0%EC%94%A8'

    req = requests.get(url)

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # = soup.find('', class_='').text

    temp = str(soup.find('span', class_='todaytemp').text)
    cast_text = soup.find('p', class_='cast_txt').text
    cast_text = cast_text
    min_temp = soup.find('span', class_='min').text
    min_temp = str(min_temp)
    max_temp = soup.find('span', class_='max').text

    # all_dust = soup.find_all('span', class_='num')
    # dust = all_dust[4].text
    # tiny_dust = all_dust[5].text

    all_dust = soup.find_all('dd')
    dust = all_dust[4].text
    dust = dust.replace("㎥", "㎥ ")
    tiny_dust = all_dust[5].text
    tiny_dust = tiny_dust.replace("㎥", "㎥ ")

    today_info = soup.find('li', class_='date_info today')
    morning_rainy = today_info.find('span', class_='point_time morning').text
    afternoon_rainy = today_info.find('span', class_='point_time afternoon').text

    weather_list = [temp, cast_text, min_temp, max_temp, dust, tiny_dust, morning_rainy, afternoon_rainy]

    # print(weather_list)

    weather_str = "현재 온도는 %s°C 입니다.\n\n%s\n최저온도 %s 최고온도 %s\n\n미세먼지 %s\n초미세먼지 %s\n\n오전%s\n오후%s" % (weather_list[0], weather_list[1], weather_list[2], weather_list[3], weather_list[4], weather_list[5], weather_list[6], weather_list[7])

    # weather_str = "현재 온도는 %s 입니다.\n%s\n최저온도 %s 최고온도 %s\n\n미세먼지 %s, 초미세먼지 %s" %(temp, cast_text, min_temp, max_temp, dust, tiny_dust)
    #print(weather_str)

    return weather_str

@csrf_exempt
def weather_print(request):
    return_text = main()

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


if __name__ == '__main__':
    main()