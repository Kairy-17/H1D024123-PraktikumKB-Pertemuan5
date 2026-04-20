# Sistem Pakar Diagnosa Penyakit THT 🩺

Aplikasi Sistem Pakar berbasis GUI (Graphical User Interface) untuk mendiagnosa penyakit pada Telinga, Hidung, dan Tenggorokan (THT). Aplikasi ini dibangun menggunakan bahasa pemrograman Python dan library `tkinter`.

Proyek ini dibuat untuk memenuhi **Tugas Praktikum Sistem Pakar 2 (Pertemuan 5)**.

## 👨‍💻 Identitas Mahasiswa
* **Nama** : [Nama Kamu]
* **NIM** : [NIM Kamu]
* **Mata Kuliah** : Praktikum Kecerdasan Buatan / Sistem Pakar

## ✨ Fitur Aplikasi
1. **Antarmuka GUI Interaktif**: Menampilkan daftar 37 gejala penyakit THT lengkap dengan *Checkbox* (kotak centang) dan fitur *Scrollbar* agar mudah dinavigasi.
2. **Kalkulasi Persentase Kecocokan**: Menggunakan metode pencocokan berbasis himpunan (Set) untuk membandingkan gejala yang dialami (input pengguna) dengan *Knowledge Base* (aturan di modul).
3. **Hasil Diagnosa Cerdas**: Menampilkan kemungkinan penyakit beserta persentase kecocokannya (hanya menampilkan penyakit dengan probabilitas kecocokan $\ge$ 40%).
4. **Tombol Reset**: Memudahkan pengguna untuk mengosongkan semua pilihan gejala dengan satu kali klik.

## 🛠️ Prasyarat (Requirements)
* Python 3.x terinstal di komputer.
* Library `tkinter` (biasanya sudah bawaan *built-in* dari instalasi standar Python).

## 🚀 Cara Menjalankan Aplikasi
1. *Clone* atau unduh *repository* ini ke komputer lokal Anda.
2. Buka terminal atau *Command Prompt*.
3. Navigasikan ke direktori tempat file ini disimpan.
4. Jalankan perintah berikut:
   ```bash
   diagnosa_tht_gui.py
