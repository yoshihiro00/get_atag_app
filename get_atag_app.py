from urllib import request 
import requests
from bs4 import BeautifulSoup
import datetime

target_url = "https://thehikaku.net/"
# response = request.urlopen(target_url)
# soup = BeautifulSoup(response)


html_text = requests.get(target_url).text
soup = BeautifulSoup(html_text, 'html.parser')

soup_a = soup.find_all("a")
dt_now = datetime.datetime.now().strftime('%m%d_%H:%M %S')
log_file_name = "log/log_file" + dt_now + "txt"

log_file = open(log_file_name,"w")
log_file.write(soup_a)
log_file.close
# print("done")