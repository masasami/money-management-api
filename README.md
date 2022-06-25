# 仮想環境の準備

```bash
# プロジェクト直下に.venvを作成する設定
$ export PIPENV_VENV_IN_PROJECT=1
# 仮想環境の削除
$ pipenv --rm
# 仮想環境の作成
$ pipenv --python 3.9
```

# FastAPI の起動

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
API_KEY=

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

# requirements.txt -> pipenv

```bash
$ pipenv install -r requirements.txt
```

# 本番環境での FastAPI デーモン化

```bash
# プロジェクトフォルダでgunicornをインストール
$ cd /var/www/money-management-api
$ pipenv install gunicorn
```

```bash
# /etc/systemd/system/gunicorn.service
[Unit]
Description=FastAPI
After=network-online.target

[Service]
User=root
WorkingDirectory=/var/www/money-management-api
Environment="PATH=/var/www/money-management-api/.venv/bin/"
ExecStart=/var/www/money-management-api/.venv/bin/gunicorn -k uvicorn.workers.UvicornWorker main:app
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

```bash
$ systemctl start gunicorn.service
# Warningが出たら
$ systemctl daemon-reload
# 動いてるかを確認
$ curl localhost:8000
```

# vscode での pipenv のライブラリのパス設定

```json
// .vscode/setting.json
// or
// VSCode上で「command + shift + p」 → 「Preferences: Open Settings (JSON)」を検索 → settings.json
{
  "python.analysis.extraPaths": [
    "/Users/masa/Desktop/develop/money-management-api/.venv/lib/python3.9/site-packages"
  ]
}
```
