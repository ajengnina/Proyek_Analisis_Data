import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
day_df = pd.read_csv("C:/Users/ajeng/Coding Camp 2025/Proyek_Analisis_Data/Data/day.csv")
hour_df = pd.read_csv("C:/Users/ajeng/Coding Camp 2025/Proyek_Analisis_Data/Data/hour.csv")

# Convert date columns
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Sidebar filters
st.sidebar.header("Filter Data")
selected_year = st.sidebar.selectbox("Pilih Tahun", options=[2011, 2012])
selected_season = st.sidebar.multiselect("Pilih Musim", options=[1, 2, 3, 4], default=[1, 2, 3, 4])

# Filter data
day_filtered = day_df[(day_df['yr'] == (selected_year - 2011)) & (day_df['season'].isin(selected_season))]

st.title("📊 Dashboard Analisis Peminjaman Sepeda")

# 1️⃣ Pola Peminjaman Sepeda Berdasarkan Waktu
st.header("1️⃣ Pola Peminjaman Sepeda Berdasarkan Waktu")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=hour_df.groupby('hr')['cnt'].mean().reset_index(), x='hr', y='cnt', ax=ax)
ax.set_title("Rata-rata Peminjaman Sepeda per Jam")
st.pyplot(fig)

# 2️⃣ Hubungan Antara Suhu dan Jumlah Peminjaman
st.header("2️⃣ Hubungan Antara Suhu dan Jumlah Peminjaman")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=day_filtered, x='temp', y='cnt', ax=ax)
ax.set_title("Hubungan Suhu dan Peminjaman Sepeda")
st.pyplot(fig)

# 3️⃣ Perbedaan Penggunaan Sepeda Antara Pengguna Terdaftar dan Kasual
st.header("3️⃣ Penggunaan Sepeda: Kasual vs Terdaftar")
fig, ax = plt.subplots(figsize=(8, 5))
day_filtered.groupby('weekday')[['casual', 'registered']].mean().plot(kind='bar', ax=ax)
ax.set_title("Penggunaan Sepeda Kasual vs Terdaftar per Hari")
st.pyplot(fig)

# 4️⃣ Dampak Kondisi Cuaca Ekstrem terhadap Peminjaman
st.header("4️⃣ Dampak Cuaca Terhadap Peminjaman")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=day_filtered, x='weathersit', y='cnt', ax=ax)
ax.set_title("Distribusi Peminjaman Berdasarkan Cuaca")
st.pyplot(fig)

# 5️⃣ Tren Peminjaman Sepeda dari 2011 ke 2012
st.header("5️⃣ Tren Peminjaman Sepeda dari Tahun ke Tahun")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=day_df, x='dteday', y='cnt', ax=ax)
ax.set_title("Tren Peminjaman Sepeda dari 2011 ke 2012")
st.pyplot(fig)

st.sidebar.markdown("---")
st.sidebar.write("👈 Gunakan filter di atas untuk eksplorasi lebih lanjut!")