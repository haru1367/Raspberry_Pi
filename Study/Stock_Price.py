import json
import requests
import time
from bs4 import BeautifulSoup

def sendToMeMessage(text):
    header = {"Authorization":"Bearer "+ KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post = {
        "object_type":"text",
        "text":text,
        "link":{
            "web_url":"https://developers.kakao.com",
            "mobile_web_url":"https://developers.kakao.com"
            },
        "button_title":"immediately confirm"
        }
    data = {"template_object":json.dumps(post)}
    return requests.post(url,headers=header,data=data)
KAKAO_TOKEN ="********************************************" // 자체모자이크처리

def get_price(com_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + com_code
    result = requests.get(url, headers={'User-agent':'Mozilla/5.0'})
    bs_obj = BeautifulSoup(result.content,"html.parser")
    no_today = bs_obj.find("p",{"class":"no_today"})
    blind_now=no_today.find("span",{"class":"blind"})
    return blind_now.text
try:
    while True:
        text = "sinsung's stock price : " +get_price("065350")
        print(sendToMeMessage(text).text)
        time.sleep(60.0)
except KeyboardInterrupt:
    pass
