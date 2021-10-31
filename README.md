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
$ python -c "import os; print(os.urandom(24).hex())"
```