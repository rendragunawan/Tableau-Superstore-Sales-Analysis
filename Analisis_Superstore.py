#!/usr/bin/env python
# coding: utf-8

# In[14]:


# memanggil pustaka

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[15]:


# memuat dan membaca file .csv

df = pd.read_csv('Sample-Superstore.csv', encoding='windows-1252')
print(df.head())


# In[16]:


# informasi dan tipe data kolom
df.info()


# In[17]:


# Memeriksa nilai yang  hilang
df.isnull().sum()


# In[18]:


# Memeriksa baris yang terduplikay
df.duplicated().sum()


# In[19]:


# Mengubah kolom 'Order Date' dan 'Ship Date' ke format datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Order Date'])

# Cek ulang informasi data
df.info()


# In[20]:


# Menyimpan data yang telah dibersihkan
cleaned_file_name = 'Superstore_Cleaned.csv'
df.to_csv(cleaned_file_name, index=False)


# In[22]:


# Melihat ringkasan statistik
df.describe().T


# In[25]:


# Mulai EDA
sns.set(style="whitegrid")

# Tren Penjualan dan Keuntungan dari Waktu ke Waktu?
# Resample data perbulan
monthly_sales_profit = df.set_index('Order Date').resample('M').agg({'Sales': 'sum', 'Profit': 'sum'})

plt.figure(figsize=(14,7))
plt.plot(monthly_sales_profit.index, 'Sales', data=monthly_sales_profit, label='Penjualan', color='blue', linewidth=2)
plt.plot(monthly_sales_profit.index, 'Profit', data=monthly_sales_profit, label='Keuntungan', color='green', linewidth=2)
plt.title('Tren Penjualan Keuntungan Bulanan (2014-2017)', fontsize=16)
plt.xlabel('Tanggal', fontsize=12)
plt.ylabel('Jumlah ($)', fontsize=12)
plt.legend()
plt.show()


# In[31]:


# Kategori dan Sub-Kategori mana yang paling perform?

#Kinerja berdasarkan kategori
category_performance = df.groupby('Category')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
print(category_performance)
category_performance.plot(kind='bar', y=['Sales', 'Profit'], figsize=(12,6), secondary_y='Profit', rot=0)
plt.title('Kinerja Kategori Produk')
plt.show()


# In[30]:


# Kinerja berdasarkan Sub-Kategori (Top 10 Penjualan)
subcategory_performance = df.groupby('Sub-Category')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False).head(10)
print(subcategory_performance)
subcategory_performance.plot(kind='bar', y=['Sales', 'Profit'], figsize=(12,6), secondary_y='Profit')
plt.title('Top 10 Kinerja Sub-Kategori Produk')
plt.show()


# In[32]:


# Wilayah dan segmen pelanggan mana yang paling berkontribusi?

# Kinerja berdasarkan Wilayah (Region)
region_performance = df.groupby('Region')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
print(region_performance)
region_performance.plot(kind='bar', y='Sales', figsize=(10,6), rot=0, legend=False)
plt.title('Total Penjualan per Wilayah')
plt.ylabel('Penjualan($)')
plt.show()


# In[34]:


#10 negara bagian teratas berdasarkan penjualan dan keuntungan
top_10_states_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)
top_10_states_profit = df.groupby('State')['Profit'].sum().sort_values(ascending=False).head(10)
print(top_10_states_sales)
print(top_10_states_profit)


# In[37]:


# Visualisasi 10 Negara Bagian berdasarkan Total Penjualan
plt.figure(figsize=(12,6))
sns.barplot(x=top_10_states_sales.values, y=top_10_states_sales.index, palette='viridis')
plt.title('Top 10 Negara Bagian berdasarkan Total Penjualan', fontsize=16)
plt.xlabel('Total Penjualan ($)', fontsize=12)
plt.ylabel('Negara Bagian (State)', fontsize=12)
plt.show()


# In[38]:


# Visualisasi 10 Negara Bagian berdasarkan Total Keuntungan
plt.figure(figsize=(12,6))
sns.barplot(x=top_10_states_profit.values, y=top_10_states_profit.index, palette='viridis')
plt.title('Top 10 Negara Bagian berdasarkan Total Keuntungan', fontsize=16)
plt.xlabel('Total Keuntungan ($)', fontsize=12)
plt.ylabel('Negara Bagian (State)', fontsize=12)
plt.show()


# In[41]:


# Analisis berdasarkan Segmen Pelanggan
segment_analysis = df.groupby('Segment')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
print(segment_analysis)

# Visualisasi Performa Segmen
segment_analysis.plot(kind='bar', figsize=(10, 6), rot=0)
plt.title('Total Penjualan dan Keuntungan per Segmen Pelanggan', fontsize=16)
plt.xlabel('Segmen Pelanggan', fontsize=12)
plt.ylabel('Jumlah ($)', fontsize=12)
plt.show()


# In[42]:


# Analisis jumlah pesanan per segmen
segment_orders = df['Segment'].value_counts()
print("\nJumlah Pesanan per Segmen:")
print(segment_orders)

plt.figure(figsize=(8, 8))
plt.pie(segment_orders, labels=segment_orders.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Distribusi Jumlah Pesanan per Segmen Pelanggan', fontsize=16)
plt.ylabel('') # Menghilangkan label 'Segment' dari sumbu y
plt.show()


# In[45]:


# Bagaimana pengaruh diskon terhadap keuntungan?
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Discount', y='Profit', hue='Category')
plt.title('Hubungan Antara Diskon dan Keuntungan', fontsize=16)
plt.xlabel('Diskon', fontsize=12)
plt.ylabel('Keuntungan ($)', fontsize=12)
plt.axhline(0, color='red', linestyle='--') # Garis batas keuntungan/kerugian
plt.show()


# In[ ]:




