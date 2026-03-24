# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Perusahaan menghadapi permasalahan tingginya tingkat attrition (karyawan keluar), yang dapat berdampak pada produktivitas, biaya rekrutmen, serta stabilitas operasional. Oleh karena itu, diperlukan analisis berbasis data untuk memahami faktor-faktor utama yang memengaruhi attrition serta membangun model prediksi guna mengidentifikasi karyawan yang berisiko tinggi untuk keluar.

---

### Permasalahan Bisnis

Beberapa permasalahan utama yang dihadapi perusahaan antara lain:

- Tingginya tingkat attrition karyawan
- Sulitnya mengidentifikasi faktor utama penyebab karyawan resign
- Tidak adanya sistem prediksi untuk mendeteksi karyawan berisiko tinggi
- Kurangnya strategi retensi berbasis data

---

### Cakupan Proyek

Cakupan proyek ini meliputi:

- Melakukan eksplorasi data (EDA) untuk memahami pola attrition
- Membuat visualisasi dalam bentuk business dashboard
- Mengidentifikasi faktor-faktor utama yang memengaruhi attrition
- Membangun model machine learning untuk prediksi attrition
- Membuat sistem prediksi berbasis script (batch & manual)

---

## Persiapan Proyek

### Sumber Data

Dataset yang digunakan dalam proyek ini adalah **IBM HR Analytics Employee Attrition & Performance**, yang dapat diunduh melalui tautan berikut:

🔗 [https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Unduh file `Employee_data.csv` dan letakkan di direktori root proyek sebelum menjalankan skrip.

---

### Setup Environment

#### 1. Clone Repository

Silahkan Download semua file yang ada di Gdrive: [https://drive.google.com/drive/folders/1LRtRMhq6sHkRJZvTg32Xb3j7BD8D5ONH?usp=drive_link](https://drive.google.com/drive/folders/1LRtRMhq6sHkRJZvTg32Xb3j7BD8D5ONH?usp=drive_link)

#### 2. Membuat Virtual Environment

```bash
python -m venv venv
```

#### 3. Mengaktifkan Virtual Environment

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  source venv/bin/activate
  ```

#### 4. Menginstal Dependensi

```bash
pip install -r requirements.txt
```

---

### Menjalankan Skrip Python

#### Prediksi Batch (dari file CSV)

Untuk menjalankan prediksi secara batch terhadap seluruh data dalam file CSV:

```bash
python prediction.py --mode batch --input data.csv
```

#### Prediksi Manual (input satu karyawan)

Untuk menjalankan prediksi secara manual berdasarkan script code:

```bash
python prediction.py --mode manual
```

#### Menjalankan Notebook Analisis

Jika ingin menjalankan eksplorasi data dan pelatihan model secara interaktif:

```bash
jupyter notebook notebook.ipynb
```

---

## Business Dashboard

Dashboard dibuat untuk memvisualisasikan faktor-faktor utama yang memengaruhi attrition secara interaktif dan informatif.

Beberapa insight utama yang ditampilkan dalam dashboard:

- Distribusi attrition karyawan
- Pengaruh lembur (OverTime) terhadap attrition
- Perbandingan rata-rata gaji terhadap attrition
- Tingkat attrition berdasarkan job level
- Hubungan kepuasan lingkungan kerja dengan attrition
- Tren attrition berdasarkan masa kerja (Years at Company)

Dashboard ini membantu stakeholder dalam memahami pola attrition secara cepat dan mendukung pengambilan keputusan berbasis data.

---

## Conclusion

Proyek ini berhasil membangun model machine learning untuk memprediksi karyawan yang berpotensi melakukan attrition. Model terbaik yang dipilih adalah **Logistic Regression**, dengan hasil evaluasi pada data uji (212 sampel) sebagai berikut:

| Kelas | Precision | Recall | F1-Score | Support |
|---|---|---|---|---|
| No Attrition | 0.94 | 0.73 | 0.82 | 176 |
| Attrition | 0.37 | 0.78 | 0.50 | 36 |
| **Weighted Avg** | **0.85** | **0.74** | **0.77** | **212** |

- **Accuracy: 74%** — model mampu mengklasifikasikan mayoritas karyawan dengan benar.
- **Recall kelas Attrition: 78%** — model berhasil mendeteksi 78% karyawan yang benar-benar akan keluar, yang merupakan metrik terpenting dalam konteks bisnis ini agar kasus attrition tidak terlewat.
- **Precision kelas Attrition: 37%** — menunjukkan adanya false positive yang cukup tinggi, sehingga model lebih cocok digunakan sebagai sistem peringatan dini (early warning) yang kemudian diverifikasi oleh tim HR, bukan sebagai penentu keputusan tunggal.

Berdasarkan hasil analisis data dan visualisasi pada dashboard, diperoleh beberapa insight utama:

- **Lembur (OverTime)** menjadi faktor paling dominan — karyawan yang sering lembur memiliki tingkat attrition jauh lebih tinggi.
- **Pendapatan rendah** berkorelasi kuat dengan kecenderungan karyawan untuk keluar, terutama pada level jabatan awal.
- **Job Level** berpengaruh signifikan: attrition terkonsentrasi di level bawah dan menurun seiring naiknya jabatan.
- **Kepuasan lingkungan kerja (Environment Satisfaction)** yang rendah memperparah risiko attrition.
- **Masa kerja awal (0–3 tahun)** adalah periode paling rentan, di mana angka attrition tertinggi terjadi.

Secara keseluruhan, model ini dapat membantu tim HR mengidentifikasi karyawan berisiko tinggi secara proaktif sebelum mereka memutuskan untuk resign. Dengan informasi ini, perusahaan dapat merancang intervensi yang lebih tepat sasaran, seperti program retensi khusus, peninjauan kompensasi, atau perbaikan kondisi kerja.

---

### Rekomendasi Action Items

- Mengurangi beban lembur dan mengatur workload secara lebih seimbang
- Meningkatkan kompensasi terutama pada level karyawan dengan gaji rendah
- Memfokuskan strategi retensi pada karyawan level awal (0–3 tahun masa kerja)
- Meningkatkan kualitas lingkungan kerja untuk mendongkrak kepuasan karyawan
- Mengoptimalkan program onboarding dan pendampingan pada masa awal kerja
- Mengintegrasikan model prediksi ini ke dalam sistem HR untuk pemantauan attrition secara berkala
