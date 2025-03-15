import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

# Konversi tanggal
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Sidebar untuk filter tanggal
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Mulai Tanggal", day_df["dteday"].min())
end_date = st.sidebar.date_input("Akhir Tanggal", day_df["dteday"].max())

# Sidebar untuk filter musim (season)
season_options = {1: "Musim Semi", 2: "Musim Panas", 3: "Musim Gugur", 4: "Musim Dingin"}
selected_season = st.sidebar.multiselect("Pilih Musim", options=list(season_options.keys()), format_func=lambda x: season_options[x], default=list(season_options.keys()))

# Filter data sesuai dengan input pengguna
day_filtered = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) & (day_df["dteday"] <= pd.to_datetime(end_date)) & (day_df["season"].isin(selected_season))]

# Judul dashboard
st.title("Dashboard Analisis Data Bike Sharing")
st.write("""
Dashboard ini menyajikan berbagai analisis terkait pola peminjaman sepeda berdasarkan dataset Bike Sharing.
Gunakan sidebar untuk memilih analisis yang ingin ditampilkan.
""")

# Sidebar interaktif
selected_question = st.sidebar.selectbox(
    "Pilih Analisis", 
    [
        "Pola Peminjaman Sepeda Berdasarkan Waktu", 
        "Perbedaan Peminjaman antara Hari Kerja dan Akhir Pekan", 
        "Hubungan Suhu dan Peminjaman Sepeda", 
        "Dampak Kondisi Cuaca terhadap Peminjaman", 
        "Tren Peminjaman Sepeda dari 2011 ke 2012"
    ]
)

# Visualisasi berdasarkan pilihan pengguna
if selected_question == "Pola Peminjaman Sepeda Berdasarkan Waktu":
    st.subheader("Tren Peminjaman Sepeda per Jam dalam Sehari")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=hour_df, x="hr", y="cnt", ax=ax)
    plt.xlabel("Jam")
    plt.ylabel("Jumlah Peminjaman")
    st.pyplot(fig)

elif selected_question == "Perbedaan Peminjaman antara Hari Kerja dan Akhir Pekan":
    st.subheader("Distribusi Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=day_filtered, x="workingday", y="cnt", ax=ax)
    plt.xticks([0, 1], ["Akhir Pekan", "Hari Kerja"])
    st.pyplot(fig)

elif selected_question == "Hubungan Suhu dan Peminjaman Sepeda":
    st.subheader("Hubungan Suhu dan Jumlah Peminjaman Sepeda")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=day_filtered, x="temp", y="cnt", alpha=0.5, ax=ax)
    st.pyplot(fig)

elif selected_question == "Dampak Kondisi Cuaca terhadap Peminjaman":
    st.subheader("Rata-rata Peminjaman Sepeda Berdasarkan Kondisi Cuaca")
    avg_cnt_weather = day_filtered.groupby("weathersit")["cnt"].mean().reset_index()
    weather_labels = {1: "Cerah", 2: "Mendung", 3: "Hujan Ringan", 4: "Hujan Lebat"}
    avg_cnt_weather["weathersit"] = avg_cnt_weather["weathersit"].map(weather_labels)
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=avg_cnt_weather, x="weathersit", y="cnt", palette="coolwarm", ax=ax)
    st.pyplot(fig)

elif selected_question == "Tren Peminjaman Sepeda dari 2011 ke 2012":
    st.subheader("Tren Peminjaman Sepeda dari 2011 ke 2012")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=day_filtered, x="dteday", y="cnt", hue="yr", ax=ax)
    st.pyplot(fig)
