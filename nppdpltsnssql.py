from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # Tambahkan seaborn untuk visualisasi

# Membuat engine SQLAlchemy untuk koneksi MySQL
engine = create_engine("mysql+mysqlconnector://root:@localhost/visdat")

# Membuat DataFrame dari hasil query
query = "SELECT tingkat, nominal FROM biayapendidikan"
df = pd.read_sql(query, engine)

# Menampilkan beberapa baris pertama untuk memeriksa data
print(df.head())

# Mengolah data
tingkat = df['tingkat']
nominal = df['nominal']

# Menggunakan numpy untuk operasi dasar
rata_rata_nominal = np.mean(nominal)
nominal_maksimum = np.max(nominal)
nominal_minimum = np.min(nominal)
nominal_stdev = np.round(np.std(nominal), 2)

# Menampilkan hasil
print(f"Rata-rata Nominal: {rata_rata_nominal}")
print(f"Nominal Maksimum: {nominal_maksimum}")
print(f"Nominal Minimum: {nominal_minimum}")
print(f"Nominal Standar Deviasi: {nominal_stdev}")

# Visualisasi data menggunakan seaborn
plt.figure(figsize=(10, 6))

# Membuat grafik barplot menggunakan seaborn
sns.barplot(x=tingkat, y=nominal, hue=tingkat, palette='Blues_d', legend=False)

# Menambahkan judul dan label ke grafik
plt.title('Grafik Biaya Pendidikan per Tingkat', fontsize=16)
plt.xlabel('Tingkat', fontsize=12)
plt.ylabel('Nominal (IDR)', fontsize=12)

# Menampilkan grid dan memutar label x-axis untuk visibilitas lebih baik
plt.grid(True)
plt.xticks(rotation=45)

# Menyimpan grafik ke file gambar
plt.tight_layout()
plt.savefig('grafik_biaya_pendidikan_per_tingkat_seaborn.png')

# Menampilkan grafik
plt.show()
