# Dicoding Data Analysist Project : Bike Sharing
Pada proyek ini dilakukan analisis pada [Bike Sharing Dataset](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view). *Bike sharing* merupakan sistem persewaan sepeda tradisional di mana seluruh proses mulai dari keanggotaan, persewaan, dan pengembalian
kembali menjadi otomatis. Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari posisi tertentu dan kembali lagi pada posisi lain.

Sebagai *data analyst* saya akan menyelesaikan permasalahan bisnis:
- Bagimana performa jumlah sewa sepeda dalam satu tahun terakhir?
- Kapan orang-orang paling banyak menggunakan sewa sepeda?
- Berapa jam waktu yang paling banyak dihabiskan oleh user menggunakan sewa sepeda?
- Bagaimana jumlah user sewa sepeda berdasarkan jenis keanggotaannya? 

Sebelum dilakukan analisis data, terlebih dahulu dilakukan *assessing data* dan *cleaning data* agar analisis yang dihasilkan tidak bias. Untuk analisis data dilakukan dengan menggunakan statistik deskriptif kemudian dilakukan visualisasi data.

# Bike Sharing Dashboard
## Setup environment

conda create --name main-ds python=3.9

conda activate main-ds

pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel

## Run streamlit app
streamlit run dashboard.py

## Tautan dashboard
[Bike Sharing Dashboard](https://dashboardpy-3rqgcvg2f2eysuidoft8tl.streamlit.app)
