Tentu, ini draf README untuk proyek Anda.

# Perbandingan Model Deep Learning untuk Analisis Sentimen Ulasan Aplikasi DANA

Repositori ini berisi kode untuk melakukan scraping ulasan aplikasi DANA dari Google Play Store dan membandingkan kinerja tiga model *deep learning* (DNN, LSTM, BiLSTM) untuk klasifikasi sentimen. Proyek ini bertujuan untuk menemukan arsitektur model dan teknik ekstraksi fitur yang paling efektif untuk teks ulasan berbahasa Indonesia.

-----

## 📜 Struktur Proyek

```
.
├── scraping.py         # Skrip untuk mengambil data ulasan dari Google Play Store
├── notebook.py         # Notebook utama untuk pemrosesan data, pelatihan, dan evaluasi model
├── dataset.csv         # (Dihasilkan oleh scraping.py) File CSV berisi ulasan mentah
├── requirements.txt    # Daftar library yang digunakan pada project
└── README.md           # Anda sedang membacanya
```

-----

## ⚙️ Kebutuhan (Requirements)

Pastikan Anda telah menginstal semua pustaka Python yang diperlukan. Anda bisa menginstalnya menggunakan pip:

```bash
pip install -r requirements.txt
```

Anda juga perlu mengunduh data tambahan untuk NLTK. Jalankan perintah berikut di dalam skrip Python atau notebook:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

-----

## 🚀 Cara Menjalankan

Ikuti langkah-langkah berikut untuk mereproduksi hasil penelitian:

### **1. Scraping Data Ulasan**

Jalankan skrip `scraping.py` untuk mengumpulkan 15.000 ulasan terbaru dari aplikasi DANA.

```bash
python scraping.py
```

Proses ini akan menghasilkan file `dataset.csv`.

### **2. Menjalankan Notebook Analisis**

Buka dan jalankan semua sel dalam file `notebook.py` menggunakan Jupyter Notebook atau JupyterLab. Notebook ini akan melakukan seluruh proses, mulai dari memuat data, pra-pemrosesan, pelabelan, pelatihan model, hingga evaluasi dan pengujian.

-----

## 🔬 Metodologi

Alur kerja yang diimplementasikan dalam `notebook.py` adalah sebagai berikut:

1.  **Pemuatan Data**: Membaca `dataset.csv`.
2.  **Pra-pemrosesan Teks**: Serangkaian langkah untuk membersihkan dan menormalkan teks ulasan, termasuk:
      * *Cleaning* (menghapus emoji, angka, tanda baca).
      * *Case Folding* (mengubah ke huruf kecil).
      * *Slang Word Normalization* (mengganti kata gaul dengan kata baku).
      * *Tokenizing* (memecah kalimat menjadi kata).
      * *Stopword Removal* (menghapus kata umum).
      * *Stemming* (mengubah kata ke bentuk dasarnya).
3.  **Pelabelan Sentimen**: Memberi label **positif**, **negatif**, atau **netral** pada setiap ulasan secara otomatis menggunakan pendekatan berbasis leksikon.
4.  **Penyeimbangan Data**: Melakukan *oversampling* pada data latih untuk mengatasi masalah ketidakseimbangan kelas.
5.  **Pemodelan & Eksperimen**: Melatih dan mengevaluasi tiga arsitektur model yang berbeda.

-----

## 🤖 Model yang Dibandingkan

Proyek ini membandingkan tiga kombinasi teknik ekstraksi fitur dan model:

1.  **TF-IDF + DNN**: Vektorisasi teks menggunakan `TF-IDF` yang diumpankan ke model *Deep Neural Network*.
2.  **Word Embeddings + LSTM**: Teks diubah menjadi sekuens yang kemudian direpresentasikan oleh *Word Embeddings* sebelum diproses oleh model *Bidirectional LSTM*.
3.  **TF-IDF + BiLSTM**: Vektor `TF-IDF` diubah bentuknya (*reshaped*) untuk menjadi input bagi model *Bidirectional LSTM*.

-----

## ✨ Hasil Akhir

Meskipun **TF-IDF + BiLSTM** mencapai **akurasi tertinggi (97.08%)**, pengujian kualitatif menunjukkan bahwa model ini **sangat bias** dan cenderung memprediksi semua masukan sebagai "positif".

Model **TF-IDF + DNN**, dengan akurasi **93.26%**, terbukti menjadi model yang **paling andal dan seimbang**. Model ini mampu mengidentifikasi sentimen positif, negatif, dan netral dengan benar, menjadikannya pilihan terbaik untuk kasus penggunaan di dunia nyata.