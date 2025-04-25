# Program untuk menghitung jumlah kata dalam sebuah teks

def hitung_kata(teks):
    # Menghapus spasi ekstra dan membagi teks berdasarkan spasi
    kata = teks.split()
    return len(kata)

# Meminta input dari pengguna
teks_input = input("Masukkan teks: ")

# Menghitung jumlah kata
jumlah_kata = hitung_kata(teks_input)

print(f"Jumlah kata dalam teks: {jumlah_kata}")
