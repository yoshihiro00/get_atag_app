from urllib import request 
import requests
from bs4 import BeautifulSoup
import datetime
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("the比較-解析").sheet1


target_url = "https://thehikaku.net/"
# target_url = "https://thehikaku.net/gaming/"
target_url = "https://thehikaku.net/pc/sony/22vaio-sx14.html"

html_text = requests.get(target_url).text
soup = BeautifulSoup(html_text, 'html.parser')

soup_a = soup.find_all("a")

# 結果を格納する変数
analysed_data = ""
row_num = 1
for i in soup_a:
    # # 記事パターン
    # if i.find("div",class_="article_txt_box"):
    #     article_link = str(i.get('href')) + "\n"
    #     article_title = i.find("h3",class_="title").text
    #     analysed_data += "[記事リンク]" + "\n" + article_title + "\n" + article_link
    #     continue
    # # バナーパターン(画像のみのリンク)
    # if i.find("img"):
    #     banner_link = str(i.get('href')) + "\n"
    #     banner_address = i.find("img").get('src')
    #     analysed_data += "[画像リンク]" + "\n" + banner_address + "\n" + banner_link + "\n" 
    #     continue

    # 普通のリンク
    # if len(i.contents) == 1:
    #     normal_link = str(i.get('href')) 
    #     analysed_data += "[普通のリンク]" + "\n" + str(i.text) + "\n" + normal_link + "\n" 

    # 記事パターン
    if i.find("div",class_="article_txt_box"):
        article_link = str(i.get('href')) + "\n"
        article_title = i.find("h3",class_="title").text
        analysed_data = ["記事リンク",article_title,article_link]
        sheet.insert_row(analysed_data,row_num)
        row_num += 1
        time.sleep(1.5)
        continue

    # バナーパターン(画像のみのリンク)
    if i.find("img"):
        banner_link = str(i.get('href')) + "\n"
        banner_address = i.find("img").get('src')
        analysed_data = ["画像リンク",banner_address,banner_link]
        sheet.insert_row(analysed_data,row_num)
        row_num += 1
        time.sleep(1.5)
        continue

    # 普通のリンク
    if len(i.contents) == 1:
        normal_link = str(i.get('href')) 
        analysed_data = ["普通のリンク",str(i.text),normal_link]
        sheet.insert_row(analysed_data,row_num)
        row_num += 1
        time.sleep(1.5)
        continue



# 解析した内容を書き込む
# dt_now = datetime.datetime.now().strftime('%m%d_%H:%M %S')
# log_file_name = "log/log_file" + dt_now + "txt"
# log_file = open(log_file_name,"w")
# log_file.write(analysed_data)
# log_file.close
