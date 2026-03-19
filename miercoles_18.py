import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(layout='centered',
                    page_title='Talento Tech',
                    page_icon=':bar_chart:')
st.title('Análisis de datos con python')
st.markdown('hola mundo')

t1, t2 =st.columns([0.3,0.7])
t1.image('meme-Shakira-oficina-730x524 (1).jpeg',width=200)
t2.title('Análisis de datos con python')
t2.markdown('**tel** 3135039395| **email:** **saraal19@hotmail.com**')

steps=st.tabs(['Pestaña 1', 'Pestaña 2', 'Pestaña $\sqrt{9}$'])

with steps[0]:
    st.write('Contenido de la pestaña1')

with steps [1]:
    st.title('pestaña 2')

with steps [2]:
    df=pd.DataFrame({
        'A':[1,2,3],
        'B':[4,5,6],
        'C':[7,8,9]})
st.dataframe(df)

fig, ax=plt.subplots()
ax=sns.barplot(x=['A','B','C'], y=[1, 2, 3])
st.pyplot(fig)

with steps [1]:
    df=pd.DataFrame({
        'A':[1,2,3],
        'B':[4,5,6],
        'C':[7,8,9]})
st.dataframe(df)

fig, ax=plt.subplots()
ax=sns.barplot(x=['A','B'], y=[1, 2], ax=ax[0])
ax=sns.barplot(x=['C','D'], y=[3, 4], ax=ax[1])
st.pyplot(fig)




