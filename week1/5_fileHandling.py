# Fungsi untuk menulis data ke file
def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print(f"Data berhasil ditulis ke file {file_name}")
    except Exception as e:
        print(f"Terjadi error saat menulis ke file: {e}")

# Fungsi untuk membaca data dari file
def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Isi file {file_name}:")
            print(content)
            return content
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi error saat membaca file: {e}")

# Fungsi untuk menambahkan data ke file
def append_to_file(file_name, content):
    try:
        with open(file_name, 'a') as file:
            file.write(content)
            print(f"Data berhasil ditambahkan ke file {file_name}")
    except Exception as e:
        print(f"Terjadi error saat menambahkan data ke file: {e}")

# Fungsi untuk membaca file baris per baris
def read_file_line_by_line(file_name):
    try:
        with open(file_name, 'r') as file:
            print(f"Membaca file {file_name} baris per baris:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi error saat membaca file: {e}")

# Fungsi utama untuk demonstrasi file handling
def main():
    file_name = "week1/data/example.txt"
    
    # Menulis data ke file
    write_to_file(file_name, "Ini adalah baris pertama.\nIni adalah baris kedua.")
    
    # Membaca data dari file
    read_from_file(file_name)
    
    # Menambahkan data ke file
    append_to_file(file_name, "\nIni adalah baris tambahan.")
    
    # Membaca file baris per baris
    read_file_line_by_line(file_name)

# Jalankan fungsi utama
if __name__ == "__main__":
    main()
