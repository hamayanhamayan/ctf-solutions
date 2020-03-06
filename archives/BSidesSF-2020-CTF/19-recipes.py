
import jwt

payload = {
  "exp": 1583488183,
  "iat": 1583484583,
  "iss": "recipebot",
  "nbf": 1583484583,
  "sub": "6180f0c8-778b-442f-a5ab-10e18bef4c2d"
}

res = jwt.encode(payload, '', algorithm='none')
print(res)


'''

# 前提知識

- SSRF
- JWT

# 解説

ソースコードを漁っていると、`https://recipes-0abb43f9.challenges.bsidessf.net/users`というURLを見つける。  
ここには、`Access only allowed from local tools. Recipebot server at 0.0.0.0:8080`とある。  
もうすでにサイトを隅々まで観察していた私は、レシピの投稿画面に  
`Must be on a reachable web server. JPG or PNG image formats only.`  
と書かれたURL指定欄があることを思い出す。  
ひたすらpizzaの画像を置いてもダメだったが、こっちならどうだろうか。  

- `https://recipes-0abb43f9.challenges.bsidessf.net/users` → ダメ
- `https://recipes-0abb43f9.challenges.bsidessf.net/users?a=.png` → ダメ
- `http://recipes-0abb43f9.challenges.bsidessf.net/users?a=.png` → OK（分かるか）

すると、指定のURL先がbase64で埋め込まれてくるので、これをデコード。  
自分の時は+が&#43;になってたから、そこだけ変換してデコードしたらきれいにでてきた。  
その中から大切そうな部分だけ抜き出してくるとこれ。  
上は自分のアカウント。  
下が攻撃対象のアカウント。  

```
<li><a href='/profile/3a88623b-09f6-41ea-99c6-6cf887b83b2a'>user178</a></li>
<li><a href='/profile/6180f0c8-778b-442f-a5ab-10e18bef4c2d'>boudin_bakery</a></li>
```

自分のアカウントのプロファイル以下であるが、どこかで見覚えがある。  
このサイトのクッキーにはJWTが使われている。  
[JSON Web Tokens - jwt.io](https://jwt.io/)  
ここにクッキーを放り込んでやると、subにこれと同じIDが入る。

subを修正することでセッション偽造できないだろうか。  
方針は「algをnoneにする」か「秘密鍵を特定」であるが、まずは低コストな前者を試す。  
試すとできる。

'''