# PHP for CTF

- シリアライズしたものが出てくる問題
    - [https://ctftime.org/task/7103:title=Kaspersky Industrial CTF 2018 expression] [https://www.hamayanhamayan.com/entry/2018/11/25/215701:title=解説]

- PHP Object Injection
    - 外部からデシリアライズするデータを渡せるとき、意図しないクラスの意図しない状態のインスタンスを生成するテク [徳丸さん記事](https://blog.tokumaru.org/2017/09/introduction-to-object-injection.html) [OWASP](https://owasp.org/www-community/vulnerabilities/PHP_Object_Injection)
    - オブジェクトの変数（プロパティ）をインジェクションできる
        - デシリアライズ時に__constructは呼ばれない
        - だが、__destructや特殊な関数は呼ばれる可能性があり、そこでインジェクションしておいた変数の値を使って、いろんなことを行う [ここに網羅されてる](http://www.1x1.jp/blog/2010/11/php_unserialize_do_not_call_destruct.html)
    - 問題
        - [websec level04](http://websec.fr/)

- 比較の弱さ
    - PHPの比較は弱いことが知られている
    - `!strcasecmp($_POST['flag'], $flag)`
        - 実はバイパス可能
        - `$_POST['flag'] = []`となるようにPOSTで与えてやれば、全体をtrueにすることができる
        - 配列を渡すには`flag%5B%5D=`こんな感じにすればいい（`flag[]=`のURLエンコーディング後）
        - htmlでは`<input type="hidden" name="flag[]" value=""/>`こんな感じ

- parse_url関数
    - バージョンによっては`http://websec.fr/level25/index.php?page=main&send=%E9%80%81%E4%BF%A1&a=1:2`が失敗する
    - `:`が値に入っていると失敗する。失敗すると、戻り値がnullになる
