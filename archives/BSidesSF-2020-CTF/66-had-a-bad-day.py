import hhtools.util as hu
raw = 'PCEtLSBDYW4geW91IHJlYWQgdGhpcyBmbGFnPyAtLT4KPD9waHAKIC8vIENURntoYXBwaW5lc3NfbmVlZHNfbm9fZmlsdGVyc30KPz4='
res = hu.from_base64(raw)
print(res)


'''

# 前提知識

- LFI(Local File Injection)

# 解説

犬と猫を押すと、  
`https://had-a-bad-day-5b3328ad.challenges.bsidessf.net/index.php?category=meowers`  
のようにカテゴリー部分が異なって出てくる。  
カテゴリーに指定したファイルをとってきているのではないか？LFIか？  

変えてみると、`woofers`と`meowers`以外は受け付けないようだ。  
ダメという文字が出てくるので、なんらかのフィルタリングを行っているようなので、これをエスパーする。  
`meowersa`みたいに後ろ文字を付けてみると、警告が表示される。  
先頭一致か？と思ったが色々やつとどっかにあればいいみたい。  
どちらにしろ、includeが使われているみたいなのでLFIで突破は正しそうだ。  
ついでに.phpが後ろにつけられることもわかる。  

`meowers/../flag`をやってみる。   
すると何も表示されない。   
これは何？   
[Szarny.io](https://szarny.hatenablog.com/#Web--51pts-had-a-bad-day)   
ここを見るとPHPとして評価されているため、表示されないらしい。   
なるほど。   

なので、`php://filter/convert.base64-encode/resource=meowers/../flag`とすることでbase64で  
取り出してみる。

```
<!-- Can you read this flag? -->
<?php
 // CTF{happiness_needs_no_filters}
?>
```

'''