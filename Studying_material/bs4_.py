import requests
from bs4 import BeautifulSoup
import lxml



url = 'https://comic.naver.com/index'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html')
#print(soup.title)
#print(soup.title.get_text())

#print(soup.a)
print(soup.a.attrs)#dictionary형태로 나옴

print(soup.a['href'])

#FIND

print(soup.find("div", attrs={"class":"asideButton upload"})) #class = asideButton upload인 div elements를 찾아주셈
print(soup.find(attrs={"class":"asideButton upload"})) #class = asideButton upload인 elements를 찾아줘\

rank1 =soup.find("li", attrs={"class":"rank01"})
print(rank1.a)
print(rank1.a.get_text())

print(rank1.next_sibling)
print(rank1.next_sibling.next_sibling.a.get_text())

rank2 =rank1.next_sibling.next_sibling #.find_next_sibling('li')
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

print(rank1.parent)

rank2 = rank1.find_next_sibling('li')
print(rank2.a.get_text())

rank1 = rank3.find_previous_sibling('li')
print(rank1.a.get_text())

top10 = rank1.find_next_siblings('li')
print(top10)


webtoon = soup.find('a', text="더 복서-89화 우상")
print(webtoon)
                    
        
