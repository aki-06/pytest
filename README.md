## pytestの学習

### 参考URL
- https://qiita.com/kg1/items/4e2cae18e9bd39f014d4

### 準備
```
pip install pytest
pip install pytest-pythonpath
```

### ディレクトリ構成
```
study_pytest
 ├─sample
 |  ├─ calc.py
 |  └─ say.py
 └─tests
    ├─ test_calc.py
    └─ test_say.py
```

### テスト実行コマンド
```
# 全てのテストを実施
$ pytest
```

```
# 特定のテストのみ実施
$ pytest tests/test_calc.py
```

```
# ヘルプの表示
$ pytest -h
```

```
# テストケース別に結果を知る
$ pytest -v
```

```
# 前回NGだったケースだけテストする
$ pytest -v --lf
```
