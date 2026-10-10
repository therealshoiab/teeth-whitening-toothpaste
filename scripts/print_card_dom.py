import urllib.request

req = urllib.request.Request('https://theperforaa.myshopify.com', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

idx = html.find('card-wrapper')
if idx != -1:
    print(html[idx:idx+2500])
