import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Import Seaborn

# Membaca dataset dari file Excel
file_path = 'Dataset_Studi_Kasus_Cuaca.xlsx'  # Sesuaikan dengan lokasi file
df = pd.read_excel(file_path, sheet_name='Cuaca Harian')

# Menampilkan beberapa baris pertama untuk memeriksa data
print(df.head())
print(df.columns)  # Cek nama kolom yang ada di dataset
print(df.info())  # Informasi tipe data
print(df.describe())  # Statistik deskriptif

# Menggunakan pandas untuk mengolah data
# Asumsi kolom 'Tanggal', 'Suhu', dan 'Curah Hujan' ada dalam dataset
tanggal = df['Tanggal']
suhu = df['Suhu (°C)']
curah_hujan = df['Curah Hujan (mm)']

# Menggunakan numpy untuk melakukan beberapa operasi dasar
rata_rata_suhu = np.mean(suhu)
suhu_maksimum = np.max(suhu)
suhu_minimum = np.min(suhu)
suhu_stdev = np.std(suhu)

print(f"Rata-rata Suhu: {rata_rata_suhu}")
print(f"Suhu Maksimum: {suhu_maksimum}")
print(f"Suhu Minimum: {suhu_minimum}")
print(f"Suhu Standar Deviasi: {suhu_stdev}")

# Visualisasi data menggunakan seaborn

# Barplot
plt.figure(figsize=(10, 6))
sns.barplot(x='Tanggal', y='Suhu (°C)', data=df)
plt.title('Barplot Suhu Harian')
plt.xticks(rotation=45)
plt.show()

# Scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Suhu (°C)', y='Curah Hujan (mm)', data=df)
plt.title('Scatterplot Suhu vs Curah Hujan')
plt.show()

# Pairplot
sns.pairplot(df[['Suhu (°C)', 'Curah Hujan (mm)']])
plt.show()

# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Suhu (°C)', data=df)
plt.title('Boxplot Suhu Harian')
plt.show()

# KDE Plot
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Suhu (°C)'], fill=True)
plt.title('KDE Plot Suhu Harian')
plt.show()

# Histplot
plt.figure(figsize=(10, 6))
sns.histplot(df['Suhu (°C)'], bins=10, kde=True)
plt.title('Histogram Suhu Harian')
plt.show()

# Relplot
sns.relplot(x='Tanggal', y='Curah Hujan (mm)', kind="line", data=df)
plt.title('Relplot Curah Hujan Harian')
plt.xticks(rotation=45)
plt.show()

# Lineplot
plt.figure(figsize=(10, 6))
sns.lineplot(x='Tanggal', y='Suhu (°C)', data=df, marker='o')
plt.title('Lineplot Suhu Harian')
plt.xticks(rotation=45)
plt.show()
# Menyimpan grafik ke file gambar
plt.savefig('grafik_suhu_harian.png')

# Menampilkan grafik
plt.show()
