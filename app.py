import streamlit as st
import pandas as pd

st.set_page_config(page_title="PilahinAja", layout="centered")

# Sidebar untuk jenis sampah
st.title("Aplikasi Pemilah Dan Pengolahan Sampah")

# Sidebar untuk input jenis sampah
st.sidebar.header("Masukkan Jenis Sampah")
jenis_sampah = st.sidebar.selectbox("Jenis Sampah:",["Organik","Anorganik"])
jumlah_sampah = st.sidebar.number_input("Jumlah(kg):", min_value=0.1, step=0.1)
tanggal = st.sidebar.date_input("Tanggal:")

# Tombol untuk menyimpan data
if st.sidebar.button("Simpan Data"):
    data = {'Jenis Sampah': [jenis_sampah], 'Jumlah (kg)': [Jumlah_Sampah], 'Tanggal': [Tanggal]}
    df = pd.DataFrame(data)
    st.sidebar.successs("Data berhasil disimpan!")

# Menampilkan informasi pengolahan(contoh sederhana)
st.header("Informasi Pengolahan")
if jenis_sampah == "Organik":
    st.info("Sampah organik dapat diolah menjadi kompos atau biogas.")
elif jenis_sampah == "Anorganik":
    st.info("Sampah anorganik seperti plastik,kertas,dan logam dapat didaur ulang.")
    
        
