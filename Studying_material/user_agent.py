"""
https://www.whatismybrowser.com/detect/what-is-my-user-agent
사용자 에이전트 확인하기, 접속하는 브라우저에 따라 다른 내용이 나옴
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36
실제로 직접 크롬에서 볼 수 있는 정보를 받을 수 있음
"""


import requests
url = 'http://nadocoding.tistory.com'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

res = requests.get(url, headers=headers)

with open('nadocoding.html','w', encoding='utf-8') as f:
    f.write(res.text)

