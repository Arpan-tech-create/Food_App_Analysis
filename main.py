import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.header('EDA🍲')

raw=pd.read_csv('indian_food.csv')

st.write(raw)



st.subheader('Countplot............')

fig = plt.figure(figsize=(10, 4))
plt.xticks(rotation=60)
sns.countplot(x="diet",data=raw)
st.pyplot(fig)


val=raw['diet'].value_counts()
st.sidebar.write(val)



fig=plt.figure(figsize=(10,5))
st.subheader("Barplot")
sns.barplot(x=raw['course'].value_counts().index,y=raw['course'].value_counts())

st.pyplot(fig)
bar=raw['course'].value_counts()
st.sidebar.write(bar)


fig=plt.figure(figsize=(10,5))
st.sidebar.subheader("PIE_CHART")
pie=plt.pie(raw['course'].value_counts(),labels=raw['course'].value_counts().index,autopct='%1.1f%%')

st.sidebar.pyplot(fig)