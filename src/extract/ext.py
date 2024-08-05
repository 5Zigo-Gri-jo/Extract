import requests
import os
import pandas as pd

def save2df(load_dt='20190101', url_param={}):
    """airflow 호출 지점"""
    df = list2df(url_param=url_param, load_dt=load_dt)
    # df 에 load_dt 컬럼 추가 (조회 일자 YYYYMMDD 형식 으로)
    df['load_dt'] = load_dt
    # 아래 파일 저장시
    df.to_parquet(f'~/data/2019movie/{load_dt}.parquet')
    return df


def list2df(load_dt='20190101', url_param={}):
    l = req2list(load_dt, url_param)
    df = pd.DataFrame(l)
    return df

def req2list(load_dt='20190101', url_param={}) -> list:
    _, data = req(load_dt, url_param)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    return l

def get_key():
    key = os.getenv('MOVIE_API_KEY')
    return key

def req(load_dt="20190101", url_param={}):
    url = gen_url(load_dt, url_param)
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    return code, data

def gen_url(dt="20190101", url_param = {}):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"
    for k, v in url_param.items():
        url = url + f"&{k}={v}"
    return url
