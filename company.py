import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.header("THE BEST COMPANY")

content="finance company, specialized financial institution that supplies credit for the purchase of consumer goods ." \
     "services by purchasing the time-sales contracts of merchants or by granting small loans directly to consumers."

st.write(content)
st.subheader("Our Team")

col1,col2,col3,col4,col5=st.columns([1.8,0.2,1.8,0.2,1.8])

df = pandas.read_csv("info.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("photos/"+row["photos"])

with col3:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("photos/"+row["photos"])

with col5:
    for index, row in df[8:12].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("photos/"+row["photos"])