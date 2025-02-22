# ベースイメージ
FROM python:3.9

# 作業ディレクトリ
WORKDIR /app

# 依存関係のインストール
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコピー
COPY . .

# ポート公開 (今回は不要なのでコメントアウト)
# EXPOSE 80

# コマンド (開発中はコメントアウト)
# CMD ["python", "main.py"]