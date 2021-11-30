import requests
import json

def roomCreate(apiKey:str):
    header1= {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    r = requests.post("https://w2g.tv/rooms/create.json",headers = header1, data =json.dumps({"w2g_api_key": apiKey,"share": "https://www.youtube.com/watch?v=8Wdp35Z-fRs","bg_color": "#00ff00","bg_opacity": 50 }))

    x = json.loads(r.text)
    print(f' A szobád : \n https://w2g.tv/rooms/{x["streamkey"]}')





if __name__ == '__main__':
    roomCreate('gqv3cx5qiier6r5kum9nhhomq6uqw614xqdq4itc58wkrh562n0gitxs768audjk')