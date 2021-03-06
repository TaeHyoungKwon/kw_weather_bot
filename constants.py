fine_dust_sample_text = """2020년 05월 23일 (토)

오늘의 미세먼지(오전 11시 기준)

미세먼지 - 42㎍/㎥
초미세먼지 - 보통 30㎍/㎥
통합대기 - 나쁨 116

* 초미세먼지 - 초미세먼지는 1000분의 2.5mm미만 미세입자 먼지로, 코 점막을 통해 걸러지지 않고 호흡기,폐에 침투할 수 있어 각별한 주의가 필요합니다.
* 통합대기 - 통합대기지수는 대기오염도 6개 대기오염 측정치를 바탕으로 대기오염도에 따른 인체 영향 및 체감오염도를 고려하여 개발된 대기오염도 표현방식입니다.


안녕하세요. 여러분께 유용한 날씨, 미세먼지 정보를 매일 업데이트 해드리는 광운대날씨봇 입니다.
날씨는 이미 올려주시고 계셔서 미세먼지 정보 매일매일 올려드립니다. 혹시 추가로 필요한 정보 있으시면 피드백 부탁 드립니다!
즐거운 하루 되세요~
"""

weather_text = """2020년 05월 23일 (토)

오늘의 날씨(오후 1시 기준)

현재 기온 24℃
흐림, 어제보다 2˚ 높아요
최저 15˚/ 최고26˚ 체감온도 25.6˚
자외선 8 매우높음


안녕하세요. 여러분께 유용한 날씨, 미세먼지 정보를 매일 업데이트 해드리는 광운대날씨봇 입니다.
날씨는 이미 올려주시고 계셔서 미세먼지 정보 매일매일 올려드립니다. 혹시 추가로 필요한 정보 있으시면 피드백 부탁 드립니다!
즐거운 하루 되세요~
"""

WEATHER_INFO_TITLE = "날씨봇이 알려주는 오늘의 날씨"

WEATHER_AUTO_TEXT = """

{today_date} ({week_day}) (현재 시각: {today_datetime})

현재 기온: {today_temp} / {sensible}
현재 습도: {humidity}

{cast_txt}
{detail_info}

최저 {min_temperature}는 최고 {max_temperature} 입니다.
{clothes_message}

미세먼지: {mise_munji}
초미세먼지: {cho_mise_munji}
오존지수: {ozon}
"""

SECRET_BOARD_URL = "https://everytime.kr/255668"
FREE_BOARD_URL = "https://everytime.kr/370443"

NAVER_WEATHER_INFO_URL = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EC%84%9C%EC%9A%B8%EC%8B%9C+%EB%85%B8%EC%9B%90%EA%B5%AC+%EC%9B%94%EA%B3%84+2%EB%8F%99+%EB%82%A0%EC%94%A8"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"

WEEK_DAY = ("월", "화", "수", "목", "금", "토", "일")

DATE_FORMAT = "%Y년 %m월 %d일"
DATETIME_FORMAT = "%p %I시 %M분"

UNDER_0_DEGREE = "오늘은 뭘 입어도 추워요 ㅠㅠ 나가지말고 집에만.."
OVER_30_DEGREE = '오늘은 뭘 입어도 더워요 ㅠㅠ 에어콘 옆에 붙어있으세요'

UNDER_4_DEGREE = {'패딩', '두꺼운 코트', '히트텍', '목도리', '기모 레깅스', '두꺼운 청바지', '기모 면바지'}
UNDER_8_DEGREE = {'코트', '가죽자켓', '히트텍', '니트', '기모 레깅스', '두꺼운 청바지', '기모 면바지'}
UNDER_11_DEGREE = {'자켓', '트렌치코트', '야상', '니트', '여러겹 껴입기', '청바지', '면바지'}
UNDER_16_DEGREE = {'자켓', '가디건', '야상', '청바지', '면바지'}
UNDER_19_DEGREE = {'얇은 니트', '맨투맨', '가디건', '청바지', '슬랙스', '면바지', '원피스'}
UNDER_22_DEGREE = {'얇은 가디건', '얇은 긴팔', '면바지', '청바지', '슬랙스', '원피스'}
UNDER_27_DEGREE = {'반팔', '얇은 셔츠', '반바지', '얇은 면바지'}
UNDER_30_DEGREE = {'반팔', '반바지', '민소매'}

SAMPLE_COUNT = 2

CLOTHES_TEXT = "옷차림은 아침과 저녁 쌀쌀 할 때는 {clothes_first} 코디 / 낮에는 {clothes_seconds} 코디를 고려 해보세요~"


