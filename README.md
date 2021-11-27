# 仮想環境の準備
```bash
# プロジェクト直下に.venvを作成する設定
$ export PIPENV_VENV_IN_PROJECT=1
# 仮想環境の削除
$ pipenv --rm
# 仮想環境の作成
$ pipenv --python 3.9
```

# FastAPIの起動
```python
# Pipfile
[scripts]
start = "uvicorn main:app --reload"
```
```bash
$ pipenv run start
```

# シークレットキーの生成
```bash
$ python -c 'import os; print(os.urandom(24).hex())'
```

# 環境変数に必要な項目
```
ALLOW_ORIGIN=
SECRET_KEY=
CRYPTO_PASSWORD=
HASH_KEY=

DB_USER=
DB_PASS=
DB_HOST=
DB_PORT=
DB_NAME=
```

# pipenv -> requirements.txt
```bash
# pipenvのライブラリをrequirements.txtに書き出す
$ pipenv lock -r > requirements.txt
# requirements.txtをもとにライブラリインストール
$ pip install -r requirements.txt
```