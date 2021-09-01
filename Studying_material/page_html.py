import requests
res = requests.get('http://naver.com', verify=True)
print(res.status_code)
res.raise_for_status()

print(len(res.text))
print(res.text)

with open('mynaver.html', 'w', encoding='utf-8') as f:
        f.write(res.text)