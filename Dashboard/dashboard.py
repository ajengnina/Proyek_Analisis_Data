import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
day_df = pd.read_csv("C:/Users/ajeng/Coding Camp 2025/Proyek_Analisis_Data/Data/day.csv")
hour_df = pd.read_csv("C:/Users/ajeng/Coding Camp 2025/Proyek_Analisis_Data/Data/hour.csv")

# Convert date column to datetime
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

# Sidebar navigation
st.sidebar.title("Bike Sharing Dashboard")
page = st.sidebar.radio("Navigasi", [
    "📊 Pola Peminjaman Sepeda", 
    "🌡️ Hubungan Suhu & Peminjaman", 
    "👥 Perbandingan Pengguna", 
    "☔ Dampak Cuaca Ekstrem", 
    "📈 Tren Peminjaman"
])

if page == "📊 Pola Peminjaman Sepeda":
    st.title("Pola Peminjaman Sepeda Berdasarkan Waktu")
    
    # Line chart rata-rata peminjaman per jam
    st.subheader("Rata-rata Peminjaman Sepeda per Jam")
    avg_rentals = hour_df.groupby('hr')['cnt'].mean()
    fig, ax = plt.subplots()
    sns.lineplot(x=avg_rentals.index, y=avg_rentals.values, marker='o', ax=ax)
    plt.xlabel("Jam")
    plt.ylabel("Rata-rata Penyewaan")
    plt.grid()
    st.pyplot(fig)
    
    # Boxplot peminjaman sepeda berdasarkan jam
    st.subheader("Distribusi Peminjaman Sepeda per Jam")
    fig, ax = plt.subplots()
    sns.boxplot(x=hour_df['hr'], y=hour_df['cnt'], ax=ax)
    plt.xlabel("Jam")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(fig)
    
if page == "🌡️ Hubungan Suhu & Peminjaman":
    st.title("Hubungan Antara Suhu dan Jumlah Peminjaman")
    
    # Scatter plot suhu vs peminjaman
    st.subheader("Scatter Plot: Suhu vs Peminjaman Sepeda")
    fig, ax = plt.subplots()
    sns.scatterplot(x=day_df['temp'], y=day_df['cnt'], ax=ax)
    plt.xlabel("Suhu (ternormalisasi)")
    plt.ylabel("Jumlah Peminjaman")
    st.pyplot(fig)
    
    # Heatmap korelasi
    st.subheader("Korelasi antara Suhu dan Peminjaman")
    fig, ax = plt.subplots()
    sns.heatmap(day_df[['temp', 'cnt']].corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
    
if page == "👥 Perbandingan Pengguna":
    st.title("Perbedaan Penggunaan Sepeda: Kasual vs Terdaftar")
    
    # Stacked bar chart pengguna kasual vs terdaftar
    st.subheader("Pengguna Kasual vs Terdaftar pada Hari Kerja vs Akhir Pekan")
    fig, ax = plt.subplots()
    sns.barplot(x=day_df['workingday'], y=day_df['casual'], label='Kasual', ax=ax)
    sns.barplot(x=day_df['workingday'], y=day_df['registered'], label='Terdaftar', ax=ax)
    plt.xlabel("Hari Kerja (0 = Akhir Pekan, 1 = Hari Kerja)")
    plt.ylabel("Jumlah Penyewaan")
    plt.legend()
    st.pyplot(fig)
    
if page == "☔ Dampak Cuaca Ekstrem":
    st.title("Dampak Cuaca Ekstrem terhadap Peminjaman Sepeda")
    
    # Boxplot cuaca vs peminjaman
    st.subheader("Distribusi Penyewaan Berdasarkan Cuaca")
    fig, ax = plt.subplots()
    sns.boxplot(x=day_df['weathersit'], y=day_df['cnt'], ax=ax)
    plt.xlabel("Kondisi Cuaca")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(fig)
    
if page == "📈 Tren Peminjaman":
    st.title("Tren Peminjaman Sepeda dari 2011 ke 2012")
    
    # Line chart tren penyewaan dari tahun ke tahun
    st.subheader("Tren Penyewaan Sepeda")
    fig, ax = plt.subplots()
    sns.lineplot(x=day_df['dteday'], y=day_df['cnt'], ax=ax)
    plt.xlabel("Tanggal")
    plt.ylabel("Jumlah Peminjaman")
    plt.grid()
    st.pyplot(fig)
