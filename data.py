import sqlite3

# Membuat / membuka database
db = sqlite3.connect("login.db")
cursor = db.cursor()

# Membuat tabel
cursor.execute("""
CREATE TABLE IF NOT EXISTS login (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sosmed TEXT,
    username TEXT,
    password TEXT
)
""")

db.commit()


# =========================
# TAMBAH DATA
# =========================
def tambah():
    sosmed = input("Masukkan nama sosmed: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    cursor.execute(
        "INSERT INTO login (sosmed, username, password) VALUES (?, ?, ?)",
        (sosmed, username, password)
    )

    db.commit()
    print("✅ Data berhasil ditambahkan!")


# =========================
# LIHAT DATA
# =========================
def lihat():
    cursor.execute("SELECT * FROM login")
    data = cursor.fetchall()

    if not data:
        print("Belum ada data.")
        return

    print("\n===== DATA LOGIN =====")

    for row in data:
        print(f"ID       : {row[0]}")
        print(f"Sosmed   : {row[1]}")
        print(f"Username : {row[2]}")
        print(f"Password : {row[3]}")
        print("-" * 25)


# =========================
# EDIT DATA
# =========================
def edit():
    lihat()

    id_data = input("Masukkan ID yang ingin diedit: ")

    sosmed = input("Sosmed baru: ")
    username = input("Username baru: ")
    password = input("Password baru: ")

    cursor.execute("""
        UPDATE login
        SET sosmed = ?, username = ?, password = ?
        WHERE id = ?
    """, (sosmed, username, password, id_data))

    db.commit()

    if cursor.rowcount > 0:
        print("✅ Data berhasil diubah!")
    else:
        print("❌ ID tidak ditemukan.")


# =========================
# HAPUS DATA
# =========================
def hapus():
    lihat()

    id_data = input("Masukkan ID yang ingin dihapus: ")

    cursor.execute(
        "DELETE FROM login WHERE id = ?",
        (id_data,)
    )

    db.commit()

    if cursor.rowcount > 0:
        print("✅ Data berhasil dihapus!")
    else:
        print("❌ ID tidak ditemukan.")


# =========================
# MENU UTAMA
# =========================
while True:

    print("\n" + "=" * 30)
    print("       DATA LOGIN SOSMED")
    print("=" * 30)

    print("1. Tambah data")
    print("2. Lihat data")
    print("3. Edit data")
    print("4. Hapus data")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah()

    elif pilihan == "2":
        lihat()

    elif pilihan == "3":
        edit()

    elif pilihan == "4":
        hapus()

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("❌ Pilihan tidak tersedia.")


db.close()