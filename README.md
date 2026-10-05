<div align="center">

<h1 id="readme-top">SISTEM PENGELOLAAN JADWAL WORKOUT</h1>

Aplikasi CLI berbasis Python untuk mengelola jadwal latihan olahraga mingguan, lengkap dengan sistem login dan dua role pengguna.


**Nama : Muhammad Irfan Nazir | Kelas : B | NIM : 070**

</div>

---

## Daftar Isi

1. [Tentang Program](#tentang-program)
2. [Flowchart dan Penjelasan Alur](#flowchart-dan-penjelasan-alur)
3. [Penjelasan Code](#penjelasan-code)
4. [Screenshot Output](#screenshot-output)

---

## Tentang Program

Program ini adalah aplikasi CLI (command line) untuk mengelola jadwal latihan olahraga (workout) mingguan, dengan tambahan sistem login dan 2 role pengguna yang memiliki hak akses berbeda.

| Role | Akses Menu | Data yang Terlihat |
|---|---|---|
| admin | Tambah, Lihat, Ubah, Hapus, Keluar (CRUD lengkap) | Jadwal semua user |
| user | Tambah, Lihat, Keluar (tidak bisa mengubah atau menghapus) | Hanya jadwal miliknya sendiri |

Setiap data jadwal workout disimpan sebagai **dictionary** (bukan list biasa seperti di Miniproject 1), dengan field `pemilik` untuk menandai milik username siapa data itu, sehingga data antar user bisa dipisahkan saat ditampilkan. Kumpulan dictionary tersebut ditampung dalam sebuah list.

Data akun login juga disimpan sebagai dictionary (`USERS`), dan hak akses tiap role disimpan sebagai dictionary berisi himpunan menu yang boleh diakses (`AKSES_MENU`).

Program juga mendukung **ganti akun** dalam satu kali program berjalan, tanpa harus menutup aplikasi, sehingga mudah diuji:

1. Login sebagai user, lalu tambah data.
2. Keluar (menu 5) dan pilih login dengan akun lain.
3. Login sebagai admin untuk melihat data yang baru saja ditambahkan user tadi.

---

## Fitur

- **Login dengan batas percobaan.** Maksimal 3 kali salah, password tersembunyi saat diketik, dan waktu login dicatat.
- **Hak akses berdasarkan role.** Admin dan user mendapat menu yang berbeda.
- **Tambah jadwal** workout (hari, jenis olahraga, durasi, set, reps, status).
- **Lihat jadwal** dalam bentuk tabel. Admin melihat semua data, user hanya data miliknya.
- **Ubah jadwal** (khusus admin). Field yang dikosongkan tidak berubah.
- **Hapus jadwal** (khusus admin) dengan konfirmasi y/n.
- **Validasi input** pada semua isian, sehingga data yang masuk selalu benar.
- **Ganti akun** tanpa menjalankan ulang program.

---

## Akun Contoh dan Hak Akses

Akun untuk login:

| Username | Password | Role |
|---|---|---|
| admin | admin123 | admin |
| irfan | irfan123 | user |
| nazir | nazir123 | user |

Menu yang bisa diakses tiap role:

| Menu | Fitur | Admin | User |
|:---:|---|:---:|:---:|
| 1 | Tambah Jadwal Workout | Ya | Ya |
| 2 | Lihat Jadwal | Ya (semua data) | Ya (data sendiri) |
| 3 | Ubah Jadwal Workout | Ya | Tidak |
| 4 | Hapus Jadwal Workout | Ya | Tidak |
| 5 | Keluar | Ya | Ya |

---

## Struktur Data

Contoh satu data jadwal workout:

```python
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

| Field | Tipe | Keterangan |
|---|---|---|
| `pemilik` | string | Username yang membuat jadwal |
| `hari` | string | Senin sampai Minggu |
| `jenis` | string | Jenis olahraga, (tidak boleh kosong) |
| `durasi` | integer | Lama latihan dalam menit, lebih dari 0 |
| `set` | integer | Jumlah set, lebih dari 0 |
| `reps` | integer | Jumlah repetisi per set, lebih dari 0 |
| `status` | string | `Sudah` atau `Belum` |


<p align="right">(<a href="#readme-top">back to top</a>)</p>


---

## Flowchart dan Penjelasan Alur

<img width="1507" height="990" alt="flowchart_program" src="https://github.com/user-attachments/assets/d8626910-03b9-4676-b549-5fae3956bf7c" />

### 1. Awal program

Program dimulai dari **Mulai**. Pengguna langsung diminta memasukkan **username dan password**.

### 2. Validasi login

Program mengecek: **Login benar?** Artinya, username ada di data akun (`USERS`) dan password-nya cocok.

- **Tidak:** tampil pesan "Username atau password salah". Program lalu mengecek **Gagal 3 kali?**
  - **Tidak:** pengguna kembali ke input username dan password.
  - **Ya:** tampil "Program dihentikan", lalu **Selesai**.
- **Ya:** tampil "Selamat datang + role", lalu lanjut ke pengecekan role.

Jadi pengguna hanya punya **3 kesempatan** untuk login.

### 3. Validasi role (admin atau user)

Program mengecek: **Role = admin?**

- **Ya:** tampil **Menu admin (1-5)**, yaitu semua fitur.
- **Tidak (user biasa):** tampil **Menu user (1, 2, 5)**, yaitu hanya tambah, tampilkan, dan keluar.

Dengan begitu menu ubah dan hapus tidak muncul untuk user biasa.

### 4. Memilih menu

Pengguna memasukkan **pilihan menu**. Program mengecek pilihan itu satu per satu dari kiri ke kanan:

| Pengecekan | Jika Ya | Akses |
|---|---|---|
| 1. Tambah data? | Tambah jadwal workout (hari, jenis, durasi, set, reps, status) | admin dan user |
| 2. Tampilkan data? | Tampilkan jadwal workout (admin: semua data, user: hanya miliknya) | admin dan user |
| 3. Ubah data? | Ubah jadwal workout | khusus admin |
| 4. Hapus data? | Hapus jadwal workout, dengan konfirmasi y/n | khusus admin |
| 5. Keluar? | Tampil "Terima kasih" | admin dan user |

Setelah menu 1 sampai 4 selesai, alur **kembali ke "Pilihan menu"**. Pengguna bisa memilih menu lain terus-menerus (looping) sampai memilih keluar.

### 5. Pilihan tidak valid

Jika pilihan tidak cocok dengan kelima pengecekan, misalnya user biasa memilih 3 atau 4, atau mengetik angka di luar menu, tampil "Pilihan tidak valid atau tidak punya akses, coba lagi". Alur lalu kembali ke "Pilihan menu".

### 6. Keluar atau ganti akun

Setelah memilih menu 5 dan "Terima kasih" tampil, program bertanya **Login akun lain? (y/n)**.

- **Ya:** kembali ke input username dan password.
- **Tidak:** program **Selesai**.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


---

## Penjelasan Code

### 1. Library yang Digunakan

```python
import time
import pwinput
from prettytable import PrettyTable
```

| Library | Kegunaan di program |
|---|---|
| `time` | `time.strftime()` mencatat waktu login, `time.sleep(1)` memberi jeda 1 detik agar pesan login sempat terbaca |
| `pwinput` | Menyembunyikan ketikan password (tampil `*`) |
| `prettytable` | Menampilkan data jadwal dalam bentuk tabel yang rapi |

### 2. Data dan Variabel Utama

```python
USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "irfan": {"password": "irfan123", "role": "user"},
    "nazir": {"password": "nazir123", "role": "user"},
}

AKSES_MENU = {
    "admin": {"1", "2", "3", "4", "5"},
    "user":  {"1", "2", "5"},
}

MAKSIMAL_PERCOBAAN_LOGIN = 3
jadwal_workout = []
HARI_VALID = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
STATUS_VALID = ["sudah", "belum"]
```

| Variabel | Tipe | Fungsi |
|---|---|---|
| `USERS` | dictionary | Menyimpan akun. Kuncinya username, nilainya dictionary berisi `password` dan `role` |
| `AKSES_MENU` | dictionary berisi set | Menentukan menu yang boleh diakses tiap role |
| `MAKSIMAL_PERCOBAAN_LOGIN` | integer | Batas salah login (3 kali) |
| `jadwal_workout` | list | Tempat menyimpan semua jadwal. Tiap jadwal berupa dictionary |
| `HARI_VALID` | list | Daftar hari yang dianggap benar saat validasi |
| `STATUS_VALID` | list | Daftar status yang dianggap benar ("sudah" atau "belum") |

### 3. Fungsi Bantuan (Validasi Input)

Semua fungsi input memakai `while True`, jadi pengguna terus diminta mengisi sampai inputnya benar.

| Fungsi | Aturan validasi | Hasil |
|---|---|---|
| `input_angka(teks)` | Harus angka dan lebih dari 0 (`isdigit()` dan `> 0`) | Integer |
| `input_hari()` | Harus ada di `HARI_VALID`, huruf besar kecil diabaikan (`lower()`) | String dengan huruf awal kapital, contoh `Senin` |
| `input_status()` | Harus "sudah" atau "belum" | `Sudah` atau `Belum` |
| `input_teks(teks, nama_field)` | Tidak boleh kosong | String |
| `input_password_tersembunyi()` | Memakai `pwinput` agar password tidak terlihat | String |
| `tekan_enter()` | Menahan layar sampai ENTER ditekan sebelum kembali ke menu | - |

Contoh fungsi validasi:

```python
def input_angka(teks):
    while True:
        nilai = input(teks)
        if nilai.isdigit() and int(nilai) > 0:
            return int(nilai)
        else:
            print(">> Input tidak valid! Harap masukkan angka lebih dari 0.\n")
```

### 4. Fitur Login: `login()`

Fungsi ini menangani proses masuk ke program dan menjadi **validasi user**.

1. Menampilkan judul login, lalu meminta username dan password (password tersembunyi).
2. Mengecek dua hal sekaligus: username ada di `USERS` **dan** password cocok.
3. Jika benar: mengambil `role`, mencatat waktu login, menampilkan pesan selamat datang, lalu mengembalikan `username, role`.
4. Jika salah: variabel `percobaan` bertambah dan sisa kesempatan ditampilkan.
5. Jika gagal 3 kali: mengembalikan `None, None`. Nilai ini dipakai `main()` untuk menghentikan program.

```python
if username in USERS and USERS[username]["password"] == password:
    role = USERS[username]["role"]
    ...
    return username, role
```

### 5. Fitur 1: Tambah Jadwal, `tambah_data(username)`

Dapat digunakan oleh **admin dan user**.

1. Meminta data berurutan: hari, jenis olahraga, durasi (menit), jumlah set, jumlah reps, dan status. Setiap input dicek oleh fungsi validasi.
2. Menyusun data menjadi dictionary `data_baru`. Field `pemilik` otomatis diisi dengan username yang sedang login.
3. Memasukkan dictionary ke list dengan `jadwal_workout.append(data_baru)`.
4. Menampilkan pesan berhasil.

### 6. Fitur 2: Lihat Jadwal, `tampilkan_data(username, role)`

Dapat digunakan oleh **admin dan user**, tetapi tampilannya berbeda.

- **Admin** melihat semua jadwal dari semua user, dan tabelnya memiliki kolom **Pemilik**.
- **User** hanya melihat jadwal miliknya. Data disaring dengan list comprehension:

```python
data_ditampilkan = [d for d in jadwal_workout if d["pemilik"] == username]
```

- Jika hasilnya kosong, tampil pesan "Belum ada data jadwal workout".
- Jika ada, program membuat `PrettyTable`, lalu `for` dengan `enumerate(..., start=1)` menambahkan nomor dan setiap baris data ke tabel.

### 7. Fungsi Pendukung: `tampilkan_data_ringkas()`

Mencetak daftar bernomor dengan satu baris per jadwal (pemilik, hari, jenis, durasi, set x reps, status). Fungsi ini dipakai oleh menu ubah dan hapus supaya admin tahu nomor mana yang akan dipilih.

### 8. Fitur 3: Ubah Jadwal, `ubah_data()`

Khusus **admin**.

1. Jika `jadwal_workout` kosong, fungsi berhenti dengan pesan.
2. Menampilkan daftar ringkas, lalu meminta nomor data yang akan diubah.
3. Jika nomor kurang dari 1 atau melebihi jumlah data, tampil "Nomor tidak ditemukan".
4. Nomor dikurangi 1 menjadi `index`, karena index list dimulai dari 0.
5. Menampilkan data lama, lalu admin mengisi nilai baru untuk setiap field:

| Kondisi input | Hasil |
|---|---|
| Dikosongkan | Data lama dipertahankan |
| Diisi dan valid | Field diperbarui |
| Diisi tetapi tidak valid | Data lama dipertahankan dan muncul pesan |

6. Menampilkan data hasil perubahan.

### 9. Fitur 4: Hapus Jadwal, `hapus_data()`

Khusus **admin**.

1. Mengecek data kosong, menampilkan daftar ringkas, lalu meminta nomor data (sama seperti `ubah_data`).
2. Meminta konfirmasi `y` atau `n`, diulang terus sampai inputnya salah satu dari keduanya.
3. Jika `y`, data dihapus dengan `jadwal_workout.pop(index)`. Jika `n`, penghapusan dibatalkan.

### 10. Menu: `tampilkan_menu(role)` dan `menu_utama(username, role)`

**`tampilkan_menu(role)`** mencetak menu sesuai role:

- Admin melihat menu 1 (Tambah), 2 (Lihat Semua Jadwal), 3 (Ubah), 4 (Hapus), dan 5 (Keluar).
- User melihat menu 1 (Tambah), 2 (Lihat Jadwal Workout Saya), dan 5 (Keluar).

**`menu_utama(username, role)`** adalah perulangan utama setelah login:

1. Menampilkan menu dan meminta pilihan.
2. Mengecek apakah pilihan ada di `AKSES_MENU[role]`:

```python
if pilihan not in AKSES_MENU[role]:
    print(">> Pilihan tidak valid atau Anda tidak memiliki akses ke menu ini!")
    continue
```

Pengecekan ini adalah **validasi role**. User biasa tidak bisa membuka menu ubah dan hapus, meskipun ia mengetik angka 3 atau 4.

3. Memanggil fungsi sesuai pilihan dengan `if / elif`.
4. Pilihan 5 menghentikan perulangan dengan `break`.

### 11. Fungsi Utama: `main()`

1. Menampilkan pesan selamat datang, lalu memanggil `login()`.
2. Jika login gagal (`username is None`), program berhenti.
3. Jika berhasil, memanggil `menu_utama(username, role)`.
4. Setelah keluar dari menu, program bertanya "Mau login sebagai akun lain? (y/n)". Jika `y`, kembali ke login. Jika bukan, program selesai.

Blok berikut memastikan `main()` hanya berjalan ketika file dijalankan langsung, bukan saat di-import:

```python
if __name__ == "__main__":
    main()
```

### 12. Konsep Pemrograman yang Digunakan

| Konsep | Contoh di program |
|---|---|
| Variabel, tipe data, operator | `percobaan`, `durasi`, `==`, `in`, `and`, `>` |
| Conditional statement | `if / elif / else` pada login, menu, dan validasi |
| Looping | `while True` pada login, menu, dan validasi; `for` pada tabel |
| List | `jadwal_workout`, `HARI_VALID`, `STATUS_VALID` |
| Dictionary | `USERS`, `AKSES_MENU`, dan setiap data jadwal |
| Function | `login()`, `tambah_data()`, `ubah_data()`, dan lainnya |
| Library | `time`, `pwinput`, `prettytable` |


<p align="right">(<a href="#readme-top">back to top</a>)</p>


---

## Screenshot Output

Berikut tampilan program saat dijalankan di terminal.

### 1. Login Berhasil

- Admin
<img width="902" height="125" alt="Screenshot 2026-10-04 215251" src="https://github.com/user-attachments/assets/92e3d65a-0af6-486a-ba0a-deb2c40c5444" />

---

- user
<img width="868" height="122" alt="Screenshot 2026-10-04 221559" src="https://github.com/user-attachments/assets/01e06f30-be5e-47e0-82a6-377ac5ddfb6d" />

Pengguna memasukkan username dan password (tampil `*`). Program menampilkan pesan selamat datang beserta role dan waktu login.

### 2. Login Gagal

<img width="866" height="280" alt="Screenshot 2026-10-04 221745" src="https://github.com/user-attachments/assets/1d7b5e08-cda9-47e4-96f4-6982e4deb00a" />

Jika username atau password salah, program menampilkan sisa percobaan. Setelah gagal 3 kali, program dihentikan.

### 3. Menu Admin

<img width="348" height="287" alt="Screenshot 2026-10-04 222158" src="https://github.com/user-attachments/assets/3ba1cbef-05bc-44e3-a66e-e3c6124599d9" />

Admin mendapat menu lengkap: *Tambah, Lihat Semua Jadwal, Ubah, Hapus, dan Keluar.*

### 4. Menu User

<img width="411" height="256" alt="image" src="https://github.com/user-attachments/assets/b469c919-ee8e-4240-9a06-8329149ee7ad" />

User hanya mendapat menu: *Tambah, Lihat Jadwal Workout Saya, dan Keluar.*

### 5. Tambah Jadwal Workout

<img width="939" height="413" alt="image" src="https://github.com/user-attachments/assets/550c67aa-825b-4d4a-9392-60da5a6eab53" />

Data diisi satu per satu dan setiap input divalidasi. Contoh input yang salah (hari tidak valid, durasi bukan angka) ditolak dan diminta ulang.

### 6. Lihat Jadwal sebagai User

<img width="362" height="261" alt="Screenshot 2026-10-05 001434" src="https://github.com/user-attachments/assets/3d5b308e-cd7e-48bd-a254-bddbd40f4ef5" />

User hanya melihat jadwal miliknya sendiri, tanpa kolom Pemilik.

### 7. Lihat Jadwal sebagai Admin

<img width="425" height="383" alt="image" src="https://github.com/user-attachments/assets/d4e4f529-b5f1-4d8a-bd0a-4f831628f71c" />

Admin melihat jadwal semua user, lengkap dengan kolom Pemilik.

### 8. Ubah Jadwal Workout

<img width="858" height="389" alt="Screenshot 2026-10-05 001728" src="https://github.com/user-attachments/assets/db11509e-0f14-4743-8fbc-f6acf9982a4c" />

Admin memilih nomor data, lalu mengisi nilai baru. Field yang dikosongkan tidak berubah.

### 9. Hapus Jadwal Workout

<img width="977" height="281" alt="image" src="https://github.com/user-attachments/assets/5c6df8c3-9a81-46dc-9f8a-ce518042dc81" />

Sebelum data dihapus, program meminta konfirmasi `y` atau `n`.

### 10. Akses Ditolak untuk User

<img width="383" height="500" alt="image" src="https://github.com/user-attachments/assets/41fc8e89-30af-41cc-a7cd-76efffd85982" />

Saat user biasa memilih menu 3 atau 4, program menampilkan pesan bahwa pilihan tidak valid atau tidak punya akses.

### 11. Keluar dan Ganti Akun

<img width="340" height="177" alt="image" src="https://github.com/user-attachments/assets/bfb3c45e-347b-406d-b81b-885deddbae4c" />

Setelah memilih menu 5, program bertanya apakah ingin login dengan akun lain.

- Jika `y` maka ganti akun.
- JIka `n` maka program berhenti.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


---
