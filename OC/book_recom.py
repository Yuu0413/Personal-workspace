import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer, util
import requests
from bs4 import BeautifulSoup

url = "https://bookmeter.com/"
res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')
def get_book_data():