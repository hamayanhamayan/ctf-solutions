

'''

# 前提知識

- websocketの通信を確認する方法

# 解説

問題文の説明によると、  
[Publish and subscribe](https://www.meteor.com/tutorials/blaze/publish-and-subscribe)  
この部分はやってないとかいてある。  
さらっと見ると`security story`やら書いてあるので、1段落分を見ると、ほかの人のprivateな投稿も  
見えないけど、送ってしまっている状態にあるようだ。  
なので、通信が見れれば、そこにフラグがありそう。

とりあえず、ChoromeのデベロッパーツールのNetworkを使って通信を見てみよう。  
すると、websocketが使われていることがわかる。  
websocketの中身を見てみると、フラグらしき文字列があるので、`CTF{`で検索して出てきた文字列が答え。
'''