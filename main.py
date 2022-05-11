from black import main
import pytchat
from ytlv import *
import time
import requests
import json
lv=islive()
try:
    with open("setting.json", "r") as f:
        data = json.load(f)
except:
    with open("setting.json", "w") as f:
        data = {
            "words":["KIDS","WEBCAMS","BESTCAMS","1WIN","TINDERX","SEX","PENETRATION","PUSSY"],
            "apikey":"",
            "ouath":""

        }
        json.dump(data, f)
        print("請設定setting的內容")
        exit

world=data["world"]
apikey=data["apikey"]
ouath=data["ouath"]
def main(id):
    chat = pytchat.create(video_id=id)
    while chat.is_alive():
        for c in chat.get().sync_items():
            print(f"{c.datetime} [{c.author.name}]- {c.message}")
            for i in world:
                if i.upper() in c.message:
                    print(f"檢測到垃圾{c.datetime} [{c.author.name}]- {c.message}")
                    requests.delete(f"https://www.googleapis.com/youtube/v3/liveChat/messages?id={c.id}&key={apikey}",headers={"Authorization":"Bearer "+ouath,"Accept":"application/json"})

while True:
    live=lv.ytid("UCP0BspO_AMEe3aQqqpo89Dg")
    if live[0]["status"]=="OK":
        id=live[0]["link"]
        #print(id)
        main(id)
        break
    time.sleep(60)








