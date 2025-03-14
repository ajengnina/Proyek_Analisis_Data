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
    st.write("Peminjaman sepeda cenderung meningkat pada jam sibuk, terutama saat pagi (sekitar pukul 08:00) dan sore (sekitar pukul 17:00-18:00), menunjukkan bahwa sepeda banyak digunakan untuk keperluan perjalanan kerja atau sekolah.")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=hour_df, x="hr", y="cnt", ax=ax)
    plt.xlabel("Jam")
    plt.ylabel("Jumlah Peminjaman")
    st.pyplot(fig)

elif selected_question == "Perbedaan Peminjaman antara Hari Kerja dan Akhir Pekan":
    st.subheader("Distribusi Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan")
    st.write("Data menunjukkan bahwa jumlah peminjaman lebih tinggi pada hari kerja dibandingkan akhir pekan. Hal ini menunjukkan bahwa mayoritas pengguna menggunakan sepeda sebagai alat transportasi harian.")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=day_df, x="workingday", y="cnt", ax=ax)
    plt.xticks([0, 1], ["Akhir Pekan", "Hari Kerja"])
    st.pyplot(fig)

elif selected_question == "Hubungan Suhu dan Peminjaman Sepeda":
    st.subheader("Hubungan Suhu dan Jumlah Peminjaman Sepeda")
    st.write("Peminjaman sepeda cenderung meningkat saat suhu lebih tinggi, tetapi menurun saat suhu terlalu panas. Hal ini menunjukkan bahwa cuaca sedang lebih disukai oleh pengguna.")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=day_df, x="temp", y="cnt", alpha=0.5, ax=ax)
    st.pyplot(fig)

elif selected_question == "Dampak Kondisi Cuaca terhadap Peminjaman":
    st.subheader("Rata-rata Peminjaman Sepeda Berdasarkan Kondisi Cuaca")
    st.write("Peminjaman sepeda lebih banyak terjadi saat cuaca cerah dan mendung, tetapi menurun secara drastis saat hujan ringan dan hujan lebat, yang menunjukkan bahwa kondisi cuaca ekstrem berdampak negatif pada jumlah peminjaman sepeda.")
    avg_cnt_weather = day_df.groupby("weathersit")["cnt"].mean().reset_index()
    weather_labels = {1: "Cerah", 2: "Mendung", 3: "Hujan Ringan", 4: "Hujan Lebat"}
    avg_cnt_weather["weathersit"] = avg_cnt_weather["weathersit"].map(weather_labels)
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=avg_cnt_weather, x="weathersit", y="cnt", palette="coolwarm", ax=ax)
    st.pyplot(fig)

elif selected_question == "Tren Peminjaman Sepeda dari 2011 ke 2012":
    st.subheader("Tren Peminjaman Sepeda dari 2011 ke 2012")
    st.write("Terdapat peningkatan tren peminjaman sepeda dari tahun 2011 ke 2012, yang menunjukkan semakin populernya layanan bike-sharing dari waktu ke waktu.")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=day_df, x="dteday", y="cnt", hue="yr", ax=ax)
    st.pyplot(fig)
