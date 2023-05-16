from bs4 import BeautifulSoup

# http 요청 처리 라이브러리
import requests

headers = {
    "User-Agent" : "Dongyang Mirae Univ"
}

# 뉴스
webpage = requests.get("https://n.news.naver.com/mnews/article/032/0003223755?sid=105",headers=headers)
print(webpage)

# 페이지의 html 가져오기
soup = BeautifulSoup(webpage.content, "html.parser")
print(soup)

# dic_area
news = soup.select_one("#dic_area").get_text().strip()
print(news)