# Minpro-2-DDP-SIstemPengelolaanJadwalWorkout






## Deskripsi Singkat Program

Program ini adalah aplikasi CLI (command line) untuk mengelola jadwal latihan olahraga (workout) mingguan, dengan tambahan sistem login dan 2 role pengguna yang memiliki hak akses berbeda:

Role Akses Menu	Data yang terlihat
* admin	Tambah, Lihat, Ubah, Hapus, Keluar (CRUD lengkap)	Jadwal semua user
* user	Tambah, Lihat, Keluar (tidak bisa mengubah/menghapus)	Hanya jadwal miliknya sendiri

Setiap data jadwal workout disimpan sebagai dictionary (bukan list biasa seperti di Miniproject 1), dengan field "pemilik" untuk menandai milik username siapa data itu, supaya data antar user bisa dipisahkan saat ditampilkan. Contoh:

```sh
{
    "pemilik": "irfan",
    "hari": "Senin",
    "jenis": "Push Up & Plank",
    "durasi": 30,
    "set": 3,
    "reps": 12,
    "status": "Belum"
}
```
Data akun login juga disimpan sebagai dictionary (USERS), dan hak akses tiap role disimpan sebagai dictionary berisi himpunan menu yang boleh diakses (AKSES_MENU).

Program juga mendukung ganti akun dalam satu kali program berjalan, tanpa harus menutup aplikasi supaya bisa langsung dites: 

login sebagai user, tambah data, logout, lalu login sebagai admin untuk melihat data yang baru saja ditambahkan user tadi.

### Akun contoh untuk login

```sh
Username Password  Role
admin	 admin123  admin
irfan	 irfan123  user
nazir	 nazir123  user
``` 



## Flowchart & Penjelasan Alur

<img width="1507" height="990" alt="flowchart_program" src="https://github.com/user-attachments/assets/d8626910-03b9-4676-b549-5fae3956bf7c" />

### Penjelasan Flowchart: Alur Utama Sistem Pengelolaan Jadwal Workout

1. Awal program

Program dimulai dari Mulai. Pengguna langsung diminta memasukkan username dan password.

2. Validasi login

Program mengecek: Login benar? Artinya, username ada di data akun (USERS) dan passwordnya cocok.

- Tidak: tampil pesan "Username atau password salah". Program lalu mengecek Gagal 3 kali?
    + Tidak: pengguna kembali ke input username dan password.
    + Ya: tampil "Program dihentikan", lalu Selesai.
- Ya: tampil "Selamat datang + role", lalu lanjut ke pengecekan role.

Jadi pengguna hanya punya 3 kesempatan untuk login.

3. Validasi role (admin atau user)

- Program mengecek: Role = admin?

    + Ya: tampil Menu admin (1-5), yaitu semua fitur.
    + Tidak (user biasa): tampil Menu user (1, 2, 5), yaitu hanya tambah, tampilkan, dan keluar.

Dengan begitu menu ubah dan hapus tidak muncul untuk user biasa.


