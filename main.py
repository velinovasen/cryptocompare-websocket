import websocket
import json

headers = json.dumps({
'Host': 'premws-pt2.365lpodds.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Sec-WebSocket-Version': '13',
'Origin': 'https://www.bet365.com',
'Sec-WebSocket-Protocol': 'zap-protocol-v1',
'Sec-WebSocket-Extensions': 'permessage-deflate',
'Sec-WebSocket-Key': 'udoOAAfQi4isUWTydt84nw==',
'Connection': 'keep-alive, Upgrade',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache',
'Upgrade': 'websocket'
})

ws = websocket.create_connection('wss://premws-pt2.365lpodds.com', headers=headers)

