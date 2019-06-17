import random
import psycopg2
import datetime as dt
import threading

class menu:

    def __init__(self):
        self.conn = psycopg2.connect("dbname=k_userkey user=postgres host=localhost password=474849")

    def menu_print(self, place, day):  # 사용자가 요청시 해당 식당의 식단정보를 반환
        day_db_h = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일', '월요일(다음주)']  # DB 텍스트에 넣을 요일 문자 리스트

        cur = self.conn.cursor()
        sql_str = "select menu, breakfast, lunch, dinner from school_menu where place='%s' and day='%s';" % (place, day_db_h[day])
        cur.execute(sql_str)
        result = cur.fetchall()
        data = result[0][0]

        return data

    def restaurant_list(self, message):  # 인근 식당의 정보를 반환
        cur = self.conn.cursor()
        if message == '리스트':  # 사용자가 리스트 입력시 인근 식당의 리스트를 반환
            sql_str = "select distinct name, tel, delivery from restaurant order by name asc;"
            cur.execute(sql_str)

            results = cur.fetchall()

            list_data = '식당 이름 / 전화번호 / 배달여부\n'
            for result in results:
                list_data += str(result[0]) + ' / ' + str(result[1]) + ' / ' + str(result[2]) + '\n'

            return list_data

        elif message == '처음으로':
            return '처음으로 돌아갑니다'

        else:  # 리스트 이외의 값을 입력했을때
            sql_str = "select menu, price, tel, delivery from restaurant where name='%s';" % message
            cur.execute(sql_str)

            results = cur.fetchall()

            if len(results) == 0:  # 입력을 잘못했거나 없는 자료 요청시
                return '등록된 정보가 없거나 잘못된 값을 입력했습니다.\n식당 이름은 \n리스트\n를 입력하여 참고하세요'
            else:  # 사용자가 요청한 정보가 존재할 시
                tel = results[0][2]
                delivery = results[0][3]
                list_data = '%s 정보\n전화번호 : %s\n배달여부 : %s\n\n' % (message, tel, delivery)
                list_data += '메뉴 / 가격\n'
                for result in results:
                    list_data += str(result[0]) + ' / ' + str(result[1]) + '\n'

                return list_data

    def domitori(self):  # 기숙사 당일 정보
        self.random_ad()

        day_of_week = dt.datetime.today().weekday()

        data = self.menu_print('기숙사', day_of_week)
        data += "\n\n아니면 여기는 어떨까요?\n---%s---" % self.ad_data
        data += "\n\n※공지※ 안동대학식봇은 19년 1학기이후 종료할 예정입니다. 자세한 사항은 학식봇 홈페이지를 참고바랍니다"

        return data

    def domitori_tomorrow(self):  # 기숙사 익일 정보
        self.random_ad()

        day_of_week = dt.datetime.today().weekday()
        day_of_week += 1

        data = self.menu_print('기숙사', day_of_week)
        data += "\n\n아니면 여기는 어떨까요?\n---%s---" % self.ad_data
        data += "\n\n※공지※ 안동대학식봇은 19년 1학기이후 종료할 예정입니다. 자세한 사항은 학식봇 홈페이지를 참고바랍니다"

        return data

    def cheaum(self):  # 채움관 당일 정보
        self.random_ad()

        day_of_week = dt.datetime.today().weekday()

        data = self.menu_print('채움관', day_of_week)
        data += "\n아니면 여기는 어떨까요?\n---%s---" % self.ad_data
        data += "\n\n※공지※ 안동대학식봇은 19년 1학기이후 종료할 예정입니다. 자세한 사항은 학식봇 홈페이지를 참고바랍니다"

        return data

    def cheaum_tomorrow(self):  # 채움관 익일 정보
        self.random_ad()

        day_of_week = dt.datetime.today().weekday()
        day_of_week += 1

        data = self.menu_print('채움관', day_of_week)

        data += "\n아니면 여기는 어떨까요?\n---%s---" % self.ad_data
        data += "\n\n※공지※ 안동대학식봇은 19년 1학기이후 종료할 예정입니다. 자세한 사항은 학식봇 홈페이지를 참고바랍니다"

        return data

    def erum(self):  # 이움관 당일 정보
        self.random_ad()

        day_of_week = dt.datetime.today().weekday()

        data = self.menu_print('이룸관', day_of_week)
        data += "\n아니면 여기는 어떨까요?\n---%s---" % self.ad_data
        data += "\n\n※공지※ 안동대학식봇은 19년 1학기이후 종료할 예정입니다. 자세한 사항은 학식봇 홈페이지를 참고바랍니다"
        return data

    def erum_tomorrow(self):  # 이움관 익일 정보
        self.random_ad()

        day_of_week = dt.datetime.today().weekday()
        day_of_week += 1

        data = self.menu_print('이룸관', day_of_week)

        data += "\n아니면 여기는 어떨까요?\n---%s---" % self.ad_data
        data += "\n\n※공지※ 안동대학식봇은 19년 1학기이후 종료할 예정입니다. 자세한 사항은 학식봇 홈페이지를 참고바랍니다"

        return data

    def restaurant(self):  # 양식당 정보
        self.random_ad()

        res_list = ['등심돈가스: 3800원', '치즈돈가스: 4000원', '치킨까스: 3800원', '불닭덮밥: 3800원', '스팸덮밥: 3800원', '참치마요: 3500원',
                    '김밥: 1500원', '참치김밥: 2500원', \
                    '돼지등뼈곰탕: 3800원', '우동: 2500원', '샐러드파스타: 3800원', '돼지불고기덮밥: 4000원', '오리불고기덮밥: 5000원']
        rest_data = "🕞 운영시간 10:00 ~ 19:00\n(주말, 공휴일 제외)\n\n"

        for i in res_list:
            rest_data += '%s\n' % i

        rest_data += "\n아니면 여기는 어떨까요?\n---%s---" % self.ad_data
        rest_data += "\n\n※공지※ 안동대학식봇은 19년 1학기이후 종료할 예정입니다. 자세한 사항은 학식봇 홈페이지를 참고바랍니다"

        return rest_data

    def moms_db(self, moms_type):  # 박물관-맘스터치의 정보를 반환
        cur = self.conn.cursor()
        str_sql = "select * from moms where note='%s';" % moms_type
        cur.execute(str_sql)

        results = cur.fetchall()

        if moms_type == '버거':  # 버거 메뉴 정보 호출시 단품/세트 메뉴 구분용 형식
            moms_data = '메뉴 / 단품가격 / 세트가격\n'
            for result in results:
                moms_data += str(result[0]) + ' / ' + str(result[1]) + ' / ' + str(result[2]) + '\n'
        else:  # 버거 이외 형식
            moms_data = '메뉴 / 가격\n'
            for result in results:
                moms_data += str(result[0]) + ' ' + str(result[1]) + '\n'

        return moms_data

    def moms(self, moms_type):  # 맘스터치 정보
        moms_data = self.moms_db(moms_type)

        return moms_data

    def random_ad(self):  # 식단정보 하단에 임의의 인근 식당 상호를 반환
        rd_num = random.randint(0, 42)

        cur = self.conn.cursor()
        sql_str = "select distinct name from restaurant order by name asc limit 1 offset %d;" % rd_num
        cur.execute(sql_str)

        ad_results = cur.fetchall()
        self.ad_data = ad_results[0]
