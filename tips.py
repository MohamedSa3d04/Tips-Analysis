#Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#page config
st.set_page_config(
    page_title='First Project',
     page_icon=None,
     layout="wide",
      initial_sidebar_state="auto",
       menu_items=None
    )
#importing data 
df = pd.read_csv('./tips.csv')

#Making the side bar
sb = st.sidebar
sb.header("Tips Dashboard")
sb.image('./s.jpg')
sb.write("This Is A Graphical Statistics For Tips Data Set")
sb.write("")
sb.markdown("Made with [Eng/Mohamed Saad](https://www.facebook.com/profile.php?id=61557483869983):heart_eyes:")
sb.write("\nFilter the data by: ")

cat_fil = sb.selectbox('Catogrical Filter:',[None,'sex','smoker','time'])
num_fil = sb.selectbox('Numerical Filter:',[None,'total_bill','tip'])
#Filtering column and row
row_fil = sb.selectbox('Column Filter:',[None,'sex'])
col_fil = sb.selectbox('Row Filter:',[None,'time'])


#Main page
a1,a2,a3,a4 = st.columns(4)
a1.metric('Max. Total Bill',df['total_bill'].max())
a2.metric('Min. Total Bill',df['total_bill'].min())
a3.metric('Total Bill',df['total_bill'].sum())
a4.metric('Avg. Total Bill',df['total_bill'].aggregate('mean').round(0))

#2
st.subheader("Total Bill vs Tips")
fig = px.scatter(
    data_frame=df,
    x='total_bill',
    y='tip',
    color=cat_fil,
    size=num_fil,
    facet_col=col_fil,
    facet_row=row_fil
)
st.plotly_chart(fig, use_container_width=True)

#3
c1, c2, c3 = st.columns((40,30,30))
with c1:
    st.text("Sex - Total Bill")
    fig2 = px.bar(df,
    x='sex',
    y='total_bill',
    color=cat_fil)
    st.plotly_chart(fig2, use_container_width=True)

with c2:
    st.text("Tip")
    fig3 = px.pie(df,
    names=cat_fil,
    values='tip')
    st.plotly_chart(fig3, use_container_width=True)

with c3:
    pass