import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    ranking = music.select_one('#body-content > div.newest-list > div > table > tbody > tr > td.number')
    title = music.select_one('#body-content > div.newest-list > div > table > tbody > tr > td.info > a.title.ellipsis')
    name = music.select_one('#body-content > div.newest-list > div > table > tbody > tr > td.info > a.artist.ellipsis')
    print (ranking.text.replace("\n", "")[0:2],title.text.strip(), name.text)
    
    



