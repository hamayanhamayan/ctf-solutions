

'''

# 前提知識

- HTTPリクエストの知識

# 解説

一部以下をカンニングしている。  
[BSidesSF 2020 CTF の write-up - st98 の日記帳](https://st98.github.io/diary/posts/2020-02-25-bsidessf-2020-ctf.html#web-96-hurdles-21-solves)

https://hurdles-0afa81d6.challenges.bsidessf.net  
ここにアクセスすると、`You'll be rewarded with a flag if you can make it over some /hurdles.`とでる。  
ふむ。

/hurdlesにアクセスすると、`I'm sorry, I was expecting the PUT Method.`と出る。  
ついでに`x-hurdles-remaining: 12`と出る。

PUTでアクセスすると、`I'm sorry, Your path would be more exciting if it ended in !`と出る。  
ついでに`x-hurdles-remaining: 11`と出る。なるほど？後11個ハードルがあると。  
以下ハードルとその対応方法

- 11個目 `I'm sorry, Your path would be more exciting if it ended in !`
    - !で終わらないとダメとあるが、`/hurdles/!`じゃないと通らないっぽいので、そうする
- 10個目 `I'm sorry, Your URL did not ask to `get` the `flag` in its query string.`
    - 意味わからんエスパーか。`?get=flag`してやると通る
- 9個目 `I'm sorry, I was looking for a parameter named &=&=&`
    - パラメタ名が`&=&=&`とあるが、そのままじゃ置けないので、URLエンコードして置く。`%26%3D%26%3D%26=any`
    - 値はなんでもいい
    - `I'm sorry, I expected '&=&=&' to equal '%00'`と怒られてハードルが減らない
    - 実際には%00の後に妙な改行がついている
    - 値をこれにしてくれということなので、%と改行をURLエンコードして置く
    - ちなみに改行は`\n`だけ
- 8個目 `I'm sorry, Basically, I was expecting the username player.`
    - `Basically`なので、Basic認証をつける
    - ユーザー名がplayerでパスは指定がないので、適当
    - `I'm sorry, Basically, I was expecting the password of the hex representation of the md5 of the string 'open sesame'`
    - 言われたとおりにやる。
- 7個目 `I'm sorry, I was expecting you to be using a 1337 Browser.`
    - ユーザーエージェントを変える
    - `I'm sorry, I was expecting your browser version (v.XXXX) to be over 9000!`
    - `1337 Browser v.9001`で送ろう
- 6個目 `I'm sorry, I was expecting this to be forwarded through 127.0.0.1`
    - 転送元を偽装する`X-Forwarded-For`ヘッダを追加する（proxy1を見ているみたい）
    - `I'm sorry, I was expecting the forwarding client to be 13.37.13.37`
    - はい。clientをそれに変える。
- 5個目 `I'm sorry, I was expecting a Fortune Cookie`
    - Cookieを付ける `Fortune=any`
    - `I'm sorry, I was expecting the cookie to contain the number of the HTTP Cookie (State Management Mechanism) RFC from 2011.`
    - [RFC 6265 - HTTP State Management Mechanism](https://tools.ietf.org/html/rfc6265)
    - anyではなくて6265をつける
- 4個目 `I'm sorry, I expect you to accept only plain text media (MIME) type.`
    - `Accept: text/plain`を付ける
- 3個目 `I'm sorry, Я ожидал, что вы говорите по-русски.`
    - 急にどうした。後半をGoogle翻訳にかけると`ロシア語が話せると期待した。`と来た。
    - んー、そんなのあったっけと思ったらあった。 `Accept-Language: ru`
- 2個目 `I'm sorry, I was expecting to share resources with the origin https://ctf.bsidessf.net`
    - `Origin: https://ctf.bsidessf.net`
- 1個目 `I'm sorry, I was expecting you would be refered by https://ctf.bsidessf.net/challenges?`
    - `Referer: https://ctf.bsidessf.net/challenges`
- Congratulations!
    - `x-ctf-flag: CTF{I_have_been_expecting_U}`
    - curlって便利ですね
'''