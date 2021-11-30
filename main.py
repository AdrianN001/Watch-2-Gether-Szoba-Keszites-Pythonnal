import requests
import json

# https://community.w2g.tv/t/watch2gether-api-documentation/133767
header1= {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

r = requests.post("https://w2g.tv/rooms/create.json",headers = header1, data =json.dumps({"w2g_api_key": "gqv3cx5qiier6r5kum9nhhomq6uqw614xqdq4itc58wkrh562n0gitxs768audjk","share": "https://www.youtube.com/watch?v=8Wdp35Z-fRs","bg_color": "#00ff00","bg_opacity": 50 }))

x = json.loads(r.text)
print(x['streamkey'])