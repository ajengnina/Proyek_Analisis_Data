import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np

# Set Streamlit Page Config
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Title and Header
st.title("🚲 Bike Sharing Dashboard")
st.markdown("### Analisis Peminjaman Sepeda Berdasarkan Berbagai Faktor")
st.write("Dashboard ini menyajikan informasi mendalam tentang pola peminjaman sepeda berdasarkan musim, kategori hari kerja, cuaca, dan faktor lainnya.")

# Sidebar Filters
st.sidebar.header("🔎 Filter Data")
year_filter = st.sidebar.selectbox("Pilih Tahun:", options=[2011, 2012])
season_filter = st.sidebar.multiselect("Pilih Musim:", options=["Spring", "Summer", "Fall", "Winter"], default=["Spring", "Summer", "Fall", "Winter"])
workingday_filter = st.sidebar.radio("Pilih Kategori Hari:", options=["Hari Kerja", "Akhir Pekan"], index=0)

# Dummy Data (Harus Diganti dengan Data Asli)
dates = pd.date_range(start="1/1/2011", periods=365*2, freq='D')
values = np.random.randint(500, 5000, size=len(dates))
data_df = pd.DataFrame({"Tanggal": dates, "Jumlah Peminjaman": values})

# Grafik Tren Peminjaman Harian
st.subheader("📈 Tren Peminjaman Harian")
fig = px.line(data_df, x="Tanggal", y="Jumlah Peminjaman", title="Tren Peminjaman Sepeda Harian")
st.plotly_chart(fig)

# Grafik Pie untuk Distribusi Peminjaman per Musim
st.subheader("🛞 Distribusi Peminjaman per Musim")
fig = px.pie(names=["Spring", "Summer", "Fall", "Winter"], values=[120000, 180000, 160000, 90000], title="Distribusi Peminjaman Berdasarkan Musim")
st.plotly_chart(fig)

# Heatmap Peminjaman per Jam dan Hari
st.subheader("🌡️ Heatmap Peminjaman Sepeda per Jam dan Hari")
heatmap_data = np.random.randint(0, 100, size=(24, 7))
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(heatmap_data, cmap="coolwarm", xticklabels=["Sen", "Sel", "Rab", "Kam", "Jum", "Sab", "Min"], yticklabels=range(24), ax=ax)
ax.set_xlabel("Hari dalam Seminggu")
ax.set_ylabel("Jam dalam Sehari")
st.pyplot(fig)

# Scatter Plot untuk Hubungan Cuaca dan Peminjaman
st.subheader("🌤️ Hubungan Cuaca dan Peminjaman")
fig = px.scatter(x=np.random.randint(10, 35, 500), y=np.random.randint(500, 5000, 500), title="Hubungan Suhu dengan Jumlah Peminjaman", labels={"x": "Suhu (°C)", "y": "Jumlah Peminjaman"})
st.plotly_chart(fig)

# Korelasi Faktor Cuaca dan Peminjaman
st.subheader("🔬 Korelasi Cuaca dan Peminjaman")
corr_matrix = pd.DataFrame(np.random.rand(5, 5), columns=["Suhu", "Kelembaban", "Angin", "Cuaca", "Peminjaman"])
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("#### 🚀 Dibuat oleh Ajeng Nina Riski | Bike Sharing Analysis")
