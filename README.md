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

### Persiapan

Sumber data: Dataset Employee Attrition

Setup environment:
   ```bash
   pip install -r requirements.txt
   ```

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

Berdasarkan hasil analisis data dan visualisasi pada dashboard, diperoleh beberapa kesimpulan utama:

- Karyawan yang lembur memiliki tingkat attrition yang lebih tinggi dibandingkan yang tidak lembur
- Karyawan dengan pendapatan lebih rendah cenderung lebih berisiko untuk keluar
- Attrition lebih tinggi terjadi pada level jabatan rendah dan menurun pada level yang lebih tinggi
- Kepuasan lingkungan kerja yang rendah berkorelasi dengan tingkat attrition yang lebih tinggi
- Attrition paling banyak terjadi pada masa kerja awal dan menurun seiring bertambahnya masa kerja

---

### Rekomendasi Action Items (Optional)

- Mengurangi beban lembur dan mengatur workload secara lebih seimbang
- Meningkatkan kompensasi terutama pada level karyawan dengan gaji rendah
- Memfokuskan strategi retensi pada karyawan level awal
- Meningkatkan kualitas lingkungan kerja untuk meningkatkan kepuasan karyawan
- Mengoptimalkan program onboarding dan pendampingan pada masa awal kerja