import time                       
import pwinput                    
from prettytable import PrettyTable  

# DATA AKUN & HAK AKSES PER ROLE

USERS = {
    "admin": {"password": "admin123", "role": "admin"},
    "irfan": {"password": "irfan123",  "role": "user"},
    "nazir": {"password": "nazir123",  "role": "user"},
}


AKSES_MENU = {
    "admin": {"1", "2", "3", "4", "5"},
    "user":  {"1", "2", "5"},
}

MAKSIMAL_PERCOBAAN_LOGIN = 3


# VARIABEL 
jadwal_workout = []  

HARI_VALID = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
STATUS_VALID = ["sudah", "belum"]


# FUNGSI BANTUAN/VALIDASI

def input_angka(teks):
    while True:
        nilai = input(teks)
        if nilai.isdigit() and int(nilai) > 0:
            return int(nilai)
        else:
            print(">> Input tidak valid! Harap masukkan angka lebih dari 0.\n")


def input_hari():
    while True:
        hari = input("Masukkan hari (Senin-Minggu): ").strip()
        if hari.lower() in HARI_VALID:
            return hari.capitalize()
        else:
            print(">> Hari tidak valid! Contoh yang benar: Senin, Selasa, dst.\n")


def input_status():
    while True:
        status = input("Masukkan status workout (Sudah/Belum): ").strip()
        if status.lower() in STATUS_VALID:
            return status.capitalize()
        else:
            print(">> Status tidak valid! Isi 'Sudah' atau 'Belum'.\n")


def input_teks(teks, nama_field):
    while True:
        nilai = input(teks).strip()
        if nilai != "":
            return nilai
        else:
            print(f">> {nama_field} tidak boleh kosong! Coba lagi.\n")


def tekan_enter():
    input("\nTekan ENTER untuk kembali ke menu...")


def input_password_tersembunyi():
    return pwinput.pwinput(prompt="Password: ")


# FUNGSI LOGIN

def login():
    percobaan = 0

    while percobaan < MAKSIMAL_PERCOBAAN_LOGIN:
        print("\n=== LOGIN - SISTEM PENGELOLAAN JADWAL WORKOUT ===")
        username = input("Username: ").strip()
        password = input_password_tersembunyi()

        if username in USERS and USERS[username]["password"] == password:
            role = USERS[username]["role"]
            waktu_login = time.strftime("%d-%m-%Y %H:%M:%S")
            print(f"\n>> Login berhasil! Selamat datang, {username} (role: {role}).")
            print(f">> Waktu login: {waktu_login}")
            time.sleep(1)  
            return username, role
        else:
            percobaan += 1
            sisa = MAKSIMAL_PERCOBAAN_LOGIN - percobaan
            if sisa > 0:
                print(f">> Username atau password salah! Sisa percobaan: {sisa}\n")
            else:
                print(">> Gagal login 3 kali. Program dihentikan.\n")

    return None, None


# FUNGSI UTAMA CRUD

def tambah_data(username):
    print("\n=== TAMBAH JADWAL WORKOUT ===")
    hari = input_hari()
    jenis = input_teks("Masukkan jenis olahraga: ", "Jenis olahraga")
    durasi = input_angka("Masukkan durasi (menit): ")
    set_latihan = input_angka("Masukkan jumlah set: ")
    reps = input_angka("Masukkan jumlah reps per set: ")
    status = input_status()

    data_baru = {
        "pemilik": username,
        "hari": hari,
        "jenis": jenis,
        "durasi": durasi,
        "set": set_latihan,
        "reps": reps,
        "status": status,
    }
    jadwal_workout.append(data_baru)

    print(f"\n>> Berhasil menambahkan jadwal untuk {username}: {data_baru}")
    tekan_enter()


def tampilkan_data(username, role):
    print("\n=== DAFTAR JADWAL WORKOUT ===")

    if role == "admin":
        data_ditampilkan = jadwal_workout
    else:
        data_ditampilkan = [d for d in jadwal_workout if d["pemilik"] == username]

    if len(data_ditampilkan) == 0:
        print("Belum ada data jadwal workout.")
    else:
        tabel = PrettyTable()
        if role == "admin":
            tabel.field_names = ["No", "Pemilik", "Hari", "Jenis Olahraga", "Durasi", "Set", "Reps", "Status"]
        else:
            tabel.field_names = ["No", "Hari", "Jenis Olahraga", "Durasi", "Set", "Reps", "Status"]

        for i, data in enumerate(data_ditampilkan, start=1):
            if role == "admin":
                tabel.add_row([i, data["pemilik"], data["hari"], data["jenis"], data["durasi"], data["set"], data["reps"], data["status"]])
            else:
                tabel.add_row([i, data["hari"], data["jenis"], data["durasi"], data["set"], data["reps"], data["status"]])

        print(tabel)

    tekan_enter()


def tampilkan_data_ringkas():
    for i, data in enumerate(jadwal_workout, start=1):
        print(f"{i}. [{data['pemilik']}] {data['hari']} - {data['jenis']} - {data['durasi']} menit - "
            f"{data['set']} set x {data['reps']} reps - status: {data['status']}")
    print()


def ubah_data():
    print("\n=== UBAH JADWAL WORKOUT ===")

    if len(jadwal_workout) == 0:
        print("Belum ada data yang bisa diubah.")
        tekan_enter()
        return

    tampilkan_data_ringkas()
    nomor = input_angka("Masukkan nomor data yang ingin diubah: ")

    if nomor < 1 or nomor > len(jadwal_workout):
        print(">> Nomor tidak ditemukan dalam daftar!")
        tekan_enter()
        return

    index = nomor - 1
    data_lama = jadwal_workout[index]
    print(f"Data lama (milik {data_lama['pemilik']}): {data_lama}")
    print("(Kosongkan input lalu tekan ENTER jika tidak ingin mengubah field tersebut)")

    hari_baru = input(f"Hari baru [{data_lama['hari']}]: ").strip()
    jenis_baru = input(f"Jenis olahraga baru [{data_lama['jenis']}]: ").strip()
    durasi_baru = input(f"Durasi baru (menit) [{data_lama['durasi']}]: ").strip()
    set_baru = input(f"Jumlah set baru [{data_lama['set']}]: ").strip()
    reps_baru = input(f"Jumlah reps baru [{data_lama['reps']}]: ").strip()
    status_baru = input(f"Status baru [{data_lama['status']}]: ").strip()

    if hari_baru != "":
        if hari_baru.lower() in HARI_VALID:
            jadwal_workout[index]["hari"] = hari_baru.capitalize()
        else:
            print(">> Hari tidak valid, hari lama tetap dipakai.")

    if jenis_baru != "":
        jadwal_workout[index]["jenis"] = jenis_baru

    if durasi_baru != "":
        if durasi_baru.isdigit() and int(durasi_baru) > 0:
            jadwal_workout[index]["durasi"] = int(durasi_baru)
        else:
            print(">> Durasi tidak valid, durasi lama tetap dipakai.")

    if set_baru != "":
        if set_baru.isdigit() and int(set_baru) > 0:
            jadwal_workout[index]["set"] = int(set_baru)
        else:
            print(">> Jumlah set tidak valid, set lama tetap dipakai.")

    if reps_baru != "":
        if reps_baru.isdigit() and int(reps_baru) > 0:
            jadwal_workout[index]["reps"] = int(reps_baru)
        else:
            print(">> Jumlah reps tidak valid, reps lama tetap dipakai.")

    if status_baru != "":
        if status_baru.lower() in STATUS_VALID:
            jadwal_workout[index]["status"] = status_baru.capitalize()
        else:
            print(">> Status tidak valid, status lama tetap dipakai.")

    print(f"\n>> Data berhasil diubah menjadi: {jadwal_workout[index]}")
    tekan_enter()


def hapus_data():
    print("\n=== HAPUS JADWAL WORKOUT ===")

    if len(jadwal_workout) == 0:
        print("Belum ada data yang bisa dihapus.")
        tekan_enter()
        return

    tampilkan_data_ringkas()
    nomor = input_angka("Masukkan nomor data yang ingin dihapus: ")

    if nomor < 1 or nomor > len(jadwal_workout):
        print(">> Nomor tidak ditemukan dalam daftar!")
        tekan_enter()
        return

    index = nomor - 1
    data_terhapus = jadwal_workout[index]

    while True:
        konfirmasi = input(f"Yakin ingin menghapus data milik {data_terhapus['pemilik']} ini? "
                            f"{data_terhapus} (y/n): ").strip().lower()
        if konfirmasi in ["y", "n"]:
            break
        else:
            print(">> Masukkan 'y' untuk ya atau 'n' untuk tidak.")

    if konfirmasi == "y":
        jadwal_workout.pop(index)
        print(">> Data berhasil dihapus.")
    else:
        print(">> Penghapusan dibatalkan.")

    tekan_enter()


# MENU UTAMA 

def tampilkan_menu(role):
    print("\n=====================================")
    print("   SISTEM PENGELOLAAN JADWAL WORKOUT")
    print(f"   (Login sebagai: {role})")
    print("=====================================")
    print("1. Tambah Jadwal Workout")
    if role == "admin":
        print("2. Lihat Semua Jadwal (semua user)")
        print("3. Ubah Jadwal Workout")
        print("4. Hapus Jadwal Workout")
    else:
        print("2. Lihat Jadwal Workout Saya")
    print("5. Keluar")
    print("=====================================")


def menu_utama(username, role):
    """Looping menu utama, berhenti kalau user pilih Keluar (5)."""
    while True:
        tampilkan_menu(role)
        pilihan = input("Pilih menu: ").strip()

        if pilihan not in AKSES_MENU[role]:
            print(">> Pilihan tidak valid atau Anda tidak memiliki akses ke menu ini!")
            continue

        if pilihan == "1":
            tambah_data(username)
        elif pilihan == "2":
            tampilkan_data(username, role)
        elif pilihan == "3":
            ubah_data()
        elif pilihan == "4":
            hapus_data()
        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
            break


def main():
    print("Selamat datang di Sistem Pengelolaan Jadwal Workout!")
    while True:
        username, role = login()

        if username is None:
            break   

        menu_utama(username, role)

        lagi = input("\nMau login sebagai akun lain? (y/n): ").strip().lower()
        if lagi != "y":
            print("\nSampai jumpa!")
            break


if __name__ == "__main__":
    main()
