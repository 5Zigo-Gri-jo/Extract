import requests
import os

def req(load_dt="20190101", url_param={}):
    url = gen_url(load_dt, url_param)
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    print(code)
    return code, data


def gen_url(dt="20190101", url_param = {}):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = os.getenv('MOVIE_API_KEY')
    url = f"{base_url}?key={key}&targetDt={dt}"
    for k, v in url_param.items():
        url = url + f"&{k}={v}"
    
    print("*^=" * 10)
    print(url)
    print("*^=" * 10)
    return url

req()
