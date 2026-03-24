# Proyek Analisis Data & Predictive Modeling: Employee Attrition - Jaya Jaya Maju

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis faktor-faktor penyebab tingginya tingkat pengunduran diri karyawan (*attrition*) di perusahaan "Jaya Jaya Maju" serta membangun model prediksi untuk mengidentifikasi karyawan yang berisiko resign.

## Struktur Folder
- `model/`: Berisi file model machine learning yang telah dilatih (e.g., `.pkl` atau `.joblib`).
- `notebook.ipynb`: Proses Exploratory Data Analysis (EDA), Preprocessing, dan pelatihan model.
- `prediction.py`: Script Python untuk menjalankan prediksi data baru menggunakan model yang telah disimpan.
- `README.md`: Dokumentasi utama proyek.
- `garyfaldi-dashboard/`: Folder utama dashboard (berisi aset atau metadata dashboard).
- `metabase.db.mv.db`: File database instance Metabase yang berisi konfigurasi dashboard visualisasi.
- `requirements.txt`: Daftar library Python yang dibutuhkan untuk menjalankan proyek.

## Business Dashboard (Metabase)
Dashboard ini dibuat untuk membantu departemen HR memonitor faktor-faktor krusial penyebab *attrition*.

**Kredensial Akses:**
- **Email:** `root@mail.com`
- **Password:** `root123`

### Visualisasi Utama:
1. **Total Attrition Rate:** Menunjukkan angka 16.9% sebagai *baseline* masalah.
2. **MonthlyIncome vs Attrition:** Menunjukkan kesenjangan gaji yang sangat ekstrem antara karyawan yang bertahan ($6jt) vs yang resign (<$1jt).
3. **OverTime Impact (100% Stacked):** Membuktikan karyawan lembur memiliki risiko resign 3x lebih tinggi.
4. **Job Level Insight:** Menunjukkan bahwa karyawan di **Level 1 (Junior)** adalah kelompok paling rentan *attrition*.
5. **Environment & Tenure:** Analisis hubungan antara rendahnya kepuasan lingkungan kerja dan masa kerja kritis (0-5 tahun).

## Kesimpulan & Rekomendasi
### Faktor Utama Attrition:
1. **MonthlyIncome:** Faktor finansial adalah pembeda paling kontras.
2. **OverTime:** Beban kerja berlebih memicu *burnout* dan pengunduran diri.
3. **Job Level:** Kurangnya program retensi untuk level *entry/junior*.

### Action Items:
- **Prioritas Tinggi:** Penyesuaian standar gaji minimum dan evaluasi kebijakan jam lembur.
- **Prioritas Sedang:** Program mentoring khusus untuk Job Level 1 dan perbaikan fasilitas lingkungan kerja (berdasarkan skor kepuasan).

## Cara Menjalankan
1. Install library yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```
2. Untuk melihat analisis lengkap, buka notebook.ipynb.

3. Untuk menjalankan prediksi, gunakan: prediction.py.
