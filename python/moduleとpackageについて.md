# moduleのimportについて

ディレクトリにファイルが増えすぎたので，小ディレクトリからimportしようとしたらハマった．

例
```
- hoge /main.py
 |
 |- fuga/parent.py
        /child1.py  // parentクラスを継承
        /child2.py  // parentクラスを継承
```
このときにどうやってimportするのかわからなかった．

参考サイトを見ると，こんな構成になった．
```
- hoge /main.py
 |
 |- fuga/__init__.py //相対パス的な感じでかけるらしい
        /parent.py  // この中にchild1,child2クラスも書いちゃう
        /func.py    // 便利関数
```

```python
#! __init__.py
from .parent import parent, child1, child2
```
```python
#! main.py
from fuga import parent, child1, child2
from fuga import func

~~~
```

Javaとかは1ファイル1クラスが原則だったけど，Pythonはそんなことはないみたい．

[サンプルコード](ex_modules)


参考サイト
- [Python におけるモジュールとパッケージは「名前空間」](https://qiita.com/sukobuto/items/15c1173b3f37f0306dd5)
- [pythonで自作関数をモジュール化・パッケージ化](https://qiita.com/ren094275/items/5d42f7c6be8c5d3cd014)