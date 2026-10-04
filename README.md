# Minpro-2-DDP-SIstemPengelolaanJadwalWorkout






## Deskripsi Singkat Program

Program ini adalah aplikasi CLI (command line) untuk mengelola jadwal latihan olahraga (workout) mingguan, dengan tambahan sistem login dan 2 role pengguna yang memiliki hak akses berbeda:

Role	Akses Menu	Data yang terlihat
* admin	Tambah, Lihat, Ubah, Hapus, Keluar (CRUD lengkap)	Jadwal semua user
* user	Tambah, Lihat, Keluar (tidak bisa mengubah/menghapus)	Hanya jadwal miliknya sendiri

Setiap data jadwal workout disimpan sebagai dictionary (bukan list biasa seperti di Miniproject 1), dengan field "pemilik" untuk menandai milik username siapa data itu, supaya data antar user bisa dipisahkan saat ditampilkan. Contoh:

{
    "pemilik": "irfan",
    "hari": "Senin",
    "jenis": "Push Up & Plank",
    "durasi": 30,
    "set": 3,
    "reps": 12,
    "status": "Belum"
}

Data akun login juga disimpan sebagai dictionary (USERS), dan hak akses tiap role disimpan sebagai dictionary berisi himpunan menu yang boleh diakses (AKSES_MENU).

Program juga mendukung ganti akun dalam satu kali program berjalan, tanpa harus menutup aplikasi supaya bisa langsung dites: 

login sebagai user, tambah data, logout, lalu login sebagai admin untuk melihat data yang baru saja ditambahkan user tadi.

Akun contoh untuk login

```sh
Username Password        Role
admin	 admin123	admin
irfan	 irfan123	user
nazir	 nazir123	user
``` 
