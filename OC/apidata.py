import json
import sqlite3

db_name = "OC/novel_database.db"

# JSONファイルを読み込む（リスト形式を想定）
with open("OC/novel_info.json", 'r', encoding='utf-8') as f:
    data_list = json.load(f)  # ← 複数件なので list で受け取る

# DB接続
db = sqlite3.connect(db_name)
cur = db.cursor()

# テーブル作成
cur.execute('''
    CREATE TABLE IF NOT EXISTS novel_data (
        title TEXT,
        writer TEXT,
        story TEXT
    );
''')

# 各小説データをDBに挿入
sql = 'INSERT INTO novel_data (title, writer, story) VALUES (?, ?, ?);'
for data in data_list:
    title = data['title']
    writer = data['writer']
    story = data['story']
    cur.execute(sql, (title, writer, story))

db.commit()
db.close()