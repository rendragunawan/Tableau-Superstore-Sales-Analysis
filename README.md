Analisis Penjualan dan Profitabilitas Superstore | Proyek Portofolio Data Analis

➡️ [Lihat Dashboard Interaktif Langsung di Tableau Public](https://public.tableau.com/app/profile/rendra.gunawan/viz/Proyek-Superstore-kaggle/ExecutiveSalesProfitabilityOverview)

1. Latar Belakang & Masalah Bisnis
Proyek ini merupakan analisis data end-to-end dari dataset penjualan Superstore. Tujuannya adalah untuk bertindak sebagai seorang analis data internal yang ditugaskan untuk mengidentifikasi pendorong utama pendapatan dan profitabilitas, menemukan area atau produk yang kurang berkinerja, dan memberikan rekomendasi strategis berbasis data kepada manajemen untuk meningkatkan efisiensi operasional dan keuntungan.

2. Pratinjau Dashboard
Dashboard interaktif ini dirancang untuk memberikan gambaran umum eksekutif dan memungkinkan analisis drill-down pada berbagai dimensi seperti waktu, geografi, produk, dan segmen pelanggan.

(Saran: Ganti gambar statis di bawah ini dengan GIF yang menunjukkan interaktivitas dashboard Anda. Anda bisa menggunakan aplikasi gratis seperti ScreenToGif atau Giphy Capture untuk merekam layar)

3. Wawasan Bisnis & Rekomendasi Aksi
Berikut adalah temuan utama dari analisis dan rekomendasi yang bisa ditindaklanjuti oleh tim bisnis:

Insight 1: Kategori Mebel (Furniture) Memiliki Profitabilitas Rendah.
Meskipun menyumbang volume penjualan yang signifikan, kategori Mebel secara konsisten menunjukkan rasio keuntungan yang paling rendah, seringkali mendekati nol atau bahkan negatif.

Rekomendasi: Lakukan peninjauan ulang terhadap strategi diskon untuk produk-produk mebel, terutama untuk item dengan diskon di atas 30%. Pertimbangkan untuk mengurangi diskon atau membuat paket bundling dengan produk yang lebih menguntungkan.

Insight 2: Kerugian Signifikan di Beberapa Negara Bagian.
Negara bagian dengan penjualan tinggi seperti Texas, Pennsylvania, dan Illinois ternyata merupakan pusat kerugian terbesar bagi perusahaan.

Rekomendasi: Lakukan analisis biaya yang lebih dalam (deep-dive) untuk negara bagian ini. Identifikasi apakah kerugian disebabkan oleh biaya pengiriman yang tinggi, persaingan harga lokal, atau penerapan diskon yang tidak efektif.

Insight 3: Potensi Besar di Segmen Korporat.
Meskipun segmen Konsumen (Consumer) memiliki jumlah transaksi terbanyak, segmen Korporat (Corporate) menunjukkan nilai keuntungan rata-rata per transaksi yang lebih tinggi.

Rekomendasi: Kembangkan program loyalitas atau kampanye pemasaran yang ditargetkan khusus untuk klien korporat guna meningkatkan frekuensi pembelian dan membangun hubungan jangka panjang.

4. Proses Teknis & Metodologi
Proyek ini dilaksanakan melalui beberapa tahapan metodologis:

Pengumpulan Data: Menggunakan dataset standar "Sample - Superstore".

Pembersihan Data (Data Cleaning): Dilakukan menggunakan Python dengan library Pandas. Proses ini mencakup penanganan nilai duplikat, koreksi tipe data (terutama kolom tanggal), dan memastikan konsistensi data.

Analisis Data Eksploratif (EDA): Menggunakan Python (Pandas, Matplotlib, Seaborn) untuk menggali data, menemukan pola awal, dan memvalidasi hipotesis melalui statistik deskriptif dan visualisasi awal.

Desain Dashboard & Visualisasi: Merancang dan membangun dashboard interaktif di Tableau dengan fokus pada pengalaman pengguna (UX) dan kejelasan wawasan. Fitur interaktivitas seperti Filter Actions dan Global Filters diimplementasikan untuk analisis mandiri.

Publikasi: Mempublikasikan dashboard akhir ke Tableau Public untuk aksesibilitas publik dan menyusun dokumentasi proyek di GitHub.

5. Teknologi yang Digunakan
Python 3.x

Libraries: Pandas, Matplotlib, Seaborn

Lingkungan: Jupyter Notebook

Visualisasi & Dashboard: Tableau Desktop

Platform Sharing: Tableau Public, GitHub

6. Reproduksi Proyek
Untuk mereproduksi analisis yang ada di notebook:

Clone repositori ini.

Pastikan Anda memiliki Python dan Jupyter Notebook terpasang.

Instal library yang dibutuhkan: pip install pandas matplotlib seaborn

Jalankan notebook yang ada di folder /notebooks.

Kontak
Nama: Rendra Gunawan

LinkedIn: www.linkedin.com/in/rendra-gunawan-9827771b1

Email: rendragunawan023.rg@gmail.com
