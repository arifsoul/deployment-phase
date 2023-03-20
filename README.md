
# Image Classification 

Proyek klasifikasi gambar menggunakan pytorch

# Dependensi
- Flask
- torch
- torchvision
- Pillow
- psycopg2

# Cara Menjalankan Kode
- Instal dependensi dengan menjalankan perintah pip install -r requirements.txt.
- Siapkan database PostgreSQL dan sesuaikan parameter koneksi pada variabel conn.
- Jalankan kode dengan menjalankan perintah python app.py di terminal.
- Aplikasi Flask akan berjalan di alamat http://localhost:5000/.

# Struktur Kode
- Impor dependensi.
- Koneksi ke database.
- Muat model deep learning untuk klasifikasi gambar.
- Definisikan Flask app.
- Definisikan nama kelas.
- Definisikan transformasi gambar.
- Definisikan route untuk halaman utama.
- Definisikan route untuk mengunggah gambar dan memprediksi kelas.
- Simpan hasil prediksi ke dalam database.
- Kembali hasil prediksi dalam format JSON.
- Jalankan aplikasi Flask dan tutup koneksi database.

## Model
[model.pt](https://drive.google.com/file/d/1-2zFVoH03q9pZTgoLPugnWvkyoy3BhFw/view?usp=sharing)

Simpan model tersebut pada folder model

## Deployment

Jalankan docker

```bash
  docker pull arifsoul/image_classification_pytorch
```


