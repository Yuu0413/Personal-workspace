import streamlit as st
import sqlite3
from datetime import datetime, time, date

DBNAME = 'OC/book.db'

def create_database():
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            writer TEXT NOT NULL,
            first_date DATE NOT NULL,
            synopsis TEXT NOT NULL,
            );
    ''')
    conn.commit()
    conn.close()

def add_book(title, writer, first_date, synopsis):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO books (title, writer, first_date, synopsis)
        VALUES (?, ?, ?, ?);
    ''', (title, writer, first_date, synopsis))
    conn.commit()
    conn.close()

def get_books():
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books;')
    books = cursor.fetchall()
    conn.close()
    return books

