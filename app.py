# paste seluruh kode Streamlit kamu di bawah sini
import streamlit as st
import pandas as pd

st.title("Dashboard Absensi Fisika")

data = {
    "Nama": ["Ani", "Budi", "Citra"],
    "Status": ["Hadir", "Izin", "Hadir"]
}

df = pd.DataFrame(data)

st.subheader("Data Absensi Siswa")
st.dataframe(df)
