import requests
import os
#680068
banner = ('''
  _______ ______ _      _      ____  _   ___     ____  __
 |__   __|  ____| |    | |    / __ \| \ | \ \   / /  \/  |
    | |  | |__  | |    | |   | |  | |  \| |\ \_/ /| \  / |
    | |  |  __| | |    | |   | |  | | . ` | \   / | |\/| |
    | |  | |____| |____| |____ |__| | |\  |  | |  | |  | |
    |_|  |______|______|______\____/|_| \_|  |_|  |_|  |_|

                 Coded by | @680068


''')
print(banner)

print(" ")

input("Press, Enter To Start :")
username = 'user.txt'
use = username
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '__cfduid=d0ffc45fa1efa9e0d736b1c14bb6c594a1605979176; _ga=GA1.2.821290333.1605979177; G_ENABLED_IDPS=google; __gads=ID=c7705da3c1f492a3:T=1606880061:S=ALNI_MZomN5KxOkG_i59jEZaJOEsiBQi6g; _gid=GA1.2.725225671.1606979880; cf_clearance=dcd41d1895597ca22ffa90136382f60ddea9e6e2-1606979881-0-150; __rtgt_sid=ki8ibzq4bp1k2d; _gat=1',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
file = open(username, "r")
while True:
  Check = file.readline().split('\n')[0]
  tiillog = f'https://tellonym.me/{Check}'
  rq = requests.get(tiillog, headers=headers)
  if rq.status_code == 404:
      count += 1
      print("{}: {}".format(count, Check.strip()) + " | Available")
      with open('usersfound.txt', 'a') as x:
             x.write(Check + '\n')
      

  elif rq.status_code == 200:
      
      count += 1
      
      print("{}: {}".format(count, Check.strip()) + " | NoT Available")
      if (Check == ""):
          break
