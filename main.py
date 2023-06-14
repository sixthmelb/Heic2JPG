from PIL import Image
import os
import pyheif

def convert_heic_folder(input_folder, output_folder):
    # Memeriksa apakah direktori input valid
    if not os.path.isdir(input_folder):
        print("Direktori input tidak valid.")
        return

    # Memeriksa apakah direktori output valid
    if not os.path.isdir(output_folder):
        print("Direktori output tidak valid.")
        return 

    # Mendapatkan daftar file dalam direktori input
    files = os.listdir(input_folder)

    # Loop melalui setiap file dalam direktori input
    for file in files:
        file_path = os.path.join(input_folder, file)

        # Memeriksa apakah file merupakan file .HEIC
        if os.path.isfile(file_path) and file.lower().endswith('.heic'):
            try:
                # Membaca gambar .HEIC menggunakan library pyheif
                heif_file = pyheif.read(file_path)
                image = Image.frombytes(
                    heif_file.mode, 
                    heif_file.size, 
                    heif_file.data,
                    "raw",
                    heif_file.mode,
                    heif_file.stride,
                )

                # Mendapatkan path output untuk file .jpg
                output_path = os.path.join(output_folder, os.path.splitext(file)[0] + '.jpg')

                # Mengkonversi gambar .HEIC ke format .jpg dan menyimpannya
                image.save(output_path, 'JPEG')

                print("Konversi selesai. Gambar", file, "telah disimpan sebagai", output_path)
            except Exception as e:
                print("Terjadi kesalahan saat mengkonversi gambar", file + ":", str(e))

# Meminta input direktori input dan direktori output
input_folder = input("Masukkan direktori input: ")
output_folder = input("Masukkan direktori output: ")

# Menjalankan fungsi untuk mengkonversi semua file .HEIC dalam folder
convert_heic_folder(input_folder, output_folder)
