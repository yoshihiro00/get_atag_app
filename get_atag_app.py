from urllib import request 
import requests
from bs4 import BeautifulSoup
import datetime

# target_url = "https://thehikaku.net/"
target_url = "https://thehikaku.net/gaming/"

html_text = requests.get(target_url).text
soup = BeautifulSoup(html_text, 'html.parser')

soup_a = soup.find_all("a")

# 結果を格納する変数
analysed_data = ""

for i in soup_a:
    # 記事パターン
    if i.find("div",class_="article_txt_box"):
        article_link = str(i.get('href')) + "\n"
        article_title = i.find("h3",class_="title").text
        analysed_data += "[記事リンク]" + "\n" + article_title + "\n" + article_link
        continue
    # バナーパターン(画像のみのリンク)
    if i.find("img"):
        banner_link = str(i.get('href')) + "\n"
        banner_address = i.find("img").get('src')
        analysed_data += "[画像リンク]" + "\n" + banner_address + "\n" + banner_link + "\n" 
        continue
    # 普通のリンク
    if len(i.contents) == 1:
        normal_link = str(i.get('href')) 
        analysed_data += "[普通のリンク]" + "\n" + str(i.text) + "\n" + normal_link + "\n" 

# 解析した内容を書き込む
dt_now = datetime.datetime.now().strftime('%m%d_%H:%M %S')
log_file_name = "log/log_file" + dt_now + "txt"
log_file = open(log_file_name,"w")
log_file.write(analysed_data)
log_file.close
