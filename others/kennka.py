import streamlit as st

def name_list():
    list = ['大判焼','今川焼','回転焼','二重焼','太鼓焼(太鼓饅頭)','甘太郎焼','黄金焼','じまん焼','あじまん','おやき','きんつば','御座候','浅草焼','七越焼','夫婦饅頭','ドラムスコ','ベイクドモチョチョ']
    return list

def main_app():
    st.title("あの焼菓子の名称")
    st.header("もう喧嘩はやめよう...これからはこのルーレットで出た名前で呼ぶんだ...")
    button = st.button("ルーレットを回す", key="button1")
    if button:
        import random
        list = name_list()
        result = random.choice(list)
        st.write("今日から君の名前は「" + result + "」だ...")
        st.image('others/are.png', caption='あの焼菓子の名称')
        if result == 'ベイクドモチョチョ':
            st.write("↑ベイクドモチョチョ！？！？？？！？！？？！！？")