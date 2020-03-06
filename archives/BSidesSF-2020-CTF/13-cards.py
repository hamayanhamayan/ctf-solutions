
import hhtools.util as hu
import json

lose = "DealerWins"
blackjack = "Blackjack"

r = hu.get_file_via_internet_post_form_nocache_jsondata('https://cards-d38741c8.challenges.bsidessf.net/api', {})
j = json.loads(r)

doller = j['Balance']
state = j['SecretState']

while doller < 110000:
  r = hu.get_file_via_internet_post_form_nocache_jsondata('https://cards-d38741c8.challenges.bsidessf.net/api/deal', {"Bet": 500, "SecretState": state})
  j = json.loads(r)

  s = j['SecretState']
  if j['GameState'] == blackjack:
    doller = j['Balance']
    state = s
    print(r)
    continue


'''

# 使用テク

- 状態情報使いまわし（名前ある？）

# 解説

ブラックジャックができる。
ソースにヒントは少ないが、ネットワーク通信にたくさんあるので、そちらを見よう。

`https://cards-d38741c8.challenges.bsidessf.net/api`
ここにPOSTして初期状態をもらっている。
その時に状態管理値も発行してもらっているようだ。

`https://cards-d38741c8.challenges.bsidessf.net/api/config`
ゴールは10万ドル。なるほど。
Handlerがわざわざ書かれているが、何だろうか。

とりあえず、ディールしてもらおう。
`https://cards-d38741c8.challenges.bsidessf.net/api/deal`
ベット数と状態管理値。特に不審なところはない。

スタンド、ヒット、ダブルは状態管理値だけ渡していて、特に異常点なし。
`https://cards-d38741c8.challenges.bsidessf.net/api/stand`
`https://cards-d38741c8.challenges.bsidessf.net/api/hit`
`https://cards-d38741c8.challenges.bsidessf.net/api/double`

状態管理値を解析するのは大変じゃないか…？

よくあるマイナスベットかな…？
→ `{"error":"Invalid bet!"}` 違います。

んー、分からん！！！

[BSidesSF 2020 CTF の write-up - st98 の日記帳](https://st98.github.io/diary/posts/2020-02-25-bsidessf-2020-ctf.html#web-423-cards-7-solves)
天才かな？

再送攻撃とかあるし、そういう感じで考えてれば出てくるのかな？
状態管理値は再利用可能である。
なので、1000ドルを100000ドルなので、maxベットの500ドル賭けで198回勝てばいい。
これはまだ現実的な感じがする。
自動バトルコードを書いて、対戦させよう。
1発ブラックジャック狙いのロックな方針で書いていく。

'''