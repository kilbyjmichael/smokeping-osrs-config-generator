from bs4 import BeautifulSoup
import requests


headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

server_list = {}


result = requests.get(url="http://oldschool.runescape.com/slu?order=WMLPA", headers=headers)
soup = BeautifulSoup(result.content, "html.parser")

table = soup.findAll("tr", "server-list__row")

with open(r"YOUR_PATH_HERE\\Targets", "w") as conf_file:
    conf_file.write("*** Targets ***\n")
    conf_file.write("probe = FPing\n")
    conf_file.write("menu = Top\n")
    conf_file.write("title = Network Latency Grapher\n\n")
    conf_file.write("+ RunescapeWorlds\n\nmenu = Runescape\ntitle = Runescape Ping\n\n")
    for row in table:
        data = row.find_all("td", class_="server-list__row-cell")
        w = data[0].text.split()[-1]
        c, t, a = data[2].text, data[3].text, data[4].text
        conf_file.write(f"++ World{int(w) + int(300)}\n")
        conf_file.write(f"menu = World {int(w) + int(300)}\n")
        conf_file.write(f"title = World {int(w) + int(300)} - {c} - {t} - {a}\n")
        conf_file.write(f"host = oldschool{w}.runescape.com\n\n")
        #print({"world": w, "country": c, "type": t, "activity": a})

print('done')

'''
+ RunescapeWorlds
menu = Runescape
title = Runescape Ping

++ WorldX+300

menu = World X+300
title = World X+300 - Country - Type - Activity
host = oldschoolX.runescape.com

'''
