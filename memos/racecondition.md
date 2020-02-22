# Race Condition

## 概要

- 競合状態。攻撃対象に対して同時に操作を行ったときに、意図しない動作になることを利用する
- [CWE-362](https://jvndb.jvn.jp/ja/cwe/CWE-362.html)
- [参考](https://www.ipa.go.jp/security/awareness/vendor/programmingv2/contents/c304.html)
- [MSDNにガイドラインがあった](https://docs.microsoft.com/ja-jp/dotnet/standard/security/security-and-race-conditions)

## pwn

- https://bitbucket.org/ptr-yudai/writeups/src/master/2019/TokyoWesterns_CTF_5th_2019/multi_heap/

## web

- ファイルをアップロードして何かを行うサービスがあったときに
    - アップロードした直後にそのファイルを実行すると、任意プログラム実行が可能なケースがある