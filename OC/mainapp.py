import streamlit as st
import sqlite3
from sentence_transformers import SentenceTransformer, util

#モデルとDB接続
model = SentenceTransformer('all-MiniLM-L6-v2')
conn = sqlite3.connect('novel_database.db')
cursor = conn.cursor()

#ユーザー入力画面作成
st.header("好みの小説検索 by 小説家になろう")
st.subheader("")

def choose_nearly_title():
    title = st.text_input("あなたが所持している小説のタイトルを入力してください")


def choose_nearly_story():
    story = st.text_area("あなたが所持している小説のあらすじを入力してください")