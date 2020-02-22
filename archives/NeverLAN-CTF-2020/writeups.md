
https://ctf.neverlanctf.com/challenges



DasPrime [NeverLAN CTF Programming 100]

# 前提知識

- エラトステネスの篩

# 解法

競プロをやっていれば、朝飯前だろう。  
エラトステネスの篩で10^6まで素数列挙して、10497番目の素数を答えるだけ。




Cookie Monster [NeverLAN CTF Web 10]

# 前提知識

- Cookieの編集方法
- セサミストリートの知識

# 解法

開くと、`He's my favorite Red guy`と書いてある。  
問題にCookieとあるので、Cookieをとりあえず確認する。  
NameGoesHereと書いてある。  
ほう。ここに『彼』の名前を書けというのか。  
クッキーモンスター、赤といえば、セサミストリートの主人公エルモだろう。  
英語にすると「Elmo」なので、入れるとフラグが出てくる。







Stop the Bot [NeverLAN CTF Web 50]

# 前提知識

- robots.txt

# 解法

とにかく検索エンジンに載せたくないらしい。  
画面、ソースコードに怪しい所が見当たらなかったので、検索エンジンなので、とりあえずrobots.txtを参照してみる。  
すると、全体とflag.txtがDisallowされているので、flag.txtにアクセスするとフラグがある。





Browser Bias [NeverLAN CTF Web 150]

# 前提知識

- User Agent偽装

# 解法

サイトに入ると、`Sorry, this site is only optimized for browsers that run on commodo 64`と表示される。  
`commodo 64`というのが聞き慣れない。  
～向けとあるので、User Agentだろう。  
`commodo 64 user agent`でググると[このサイト](https://www2.sal.tohoku.ac.jp/~gothit/ua.html)に書いてある。  
`Contiki/1.0 (Commodore 64; http://dunkels.com/adam/contiki/)`をUser Agentにして開くと、フラグが書いてある。

