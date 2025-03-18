import os
import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  # 추가

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")


def check_attendance():
    try:
        session = requests.Session()
        options = Options()
        options.add_argument("--headless=new")  # headless 모드 활성화
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)
        driver.get('https://www.itemmania.com/portal/user/p_login_form.html')

        driver.find_element(By.NAME, 'user_id').send_keys(os.getenv('ITEM_MANIA_USER_ID'))
        driver.find_element(By.NAME, 'user_password').send_keys(os.getenv('ITEM_MANIA_PASSWORD'), Keys.RETURN)

        time.sleep(5)
        cookies = driver.get_cookies()
        cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}
        session.cookies.update(cookies_dict)
        driver.quit()

        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://www.itemmania.com',
            'Referer': 'http://www.itemmania.com/event/event_ing/e190417_attend/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        data = {'type': '1'}
        response = session.post(
            url='http://www.itemmania.com/event/event_ing/e190417_attend/ajax_event.php',
            data=data,
            headers=headers
        ).json()

        return response  # 정상 반환 시 response를 반환 명시


    except Exception as e:
        print(f"Error: {e}")
        # 오류가 발생하면 None 대신 빈 딕셔너리 또는 오류 메시지 반환
        return {'result': 'error', 'msg': str(e), 'data': None}
