import websocket
import json

headers = json.dumps({
    'Host': 'streamer.cryptocompare.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-WebSocket-Version': '13',
    'Origin': 'https://www.cryptocompare.com',
    'Sec-WebSocket-Extensions': 'permessage-deflate',
    'Sec-WebSocket-Key': 'Gshq/egz02K6fTbL+zVC6Q==',
    'Connection': 'keep-alive, Upgrade',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade': 'websocket',
    'Cookie': '__cfduid=d8aa1a29cf0094ccf572e135503f3e6a81613039992; __gads=ID=d411482435e0677d-22c33cb76eba0047:T=1613039994:RT=1613039994:S=ALNI_Mb_pJoIy3vHrpTUyay7rABSH5htpA; _ga=GA1.2.307285655.1613039995; _gid=GA1.2.1221453071.1613039995'})


ws = websocket.create_connection('wss://streamer.cryptocompare.com/v2?format=streamer', headers=headers)

ws.send(json.dumps({"action": "SubAdd", "subs": ["11~BTC", "21~BTC", "5~CCCAGG~BTC~USD", "11~ETH", "21~ETH", "5~CCCAGG~ETH~USD", "11~BCH", "21~BCH", "5~CCCAGG~BCH~USD",
                    "11~EOS", "21~EOS", "5~CCCAGG~EOS~USD", "11~XRP", "21~XRP","5~CCCAGG~XRP~USD", "11~LTC", "21~LTC", "5~CCCAGG~LTC~USD",
                    "11~ETC", "21~ETC", "5~CCCAGG~ETC~USD", "11~BSV", "21~BSV", "5~CCCAGG~BSV~USD", "11~LINK", "21~LINK", "5~CCCAGG~LINK~USD", "11~ATOM", "21~ATOM", "5~CCCAGG~ATOM~USD"]}))

while True:
    try:
        result = ws.recv()
        if 'ETH~USD' in result:
            print(result)
    except Exception as e:
        print(e)
        break