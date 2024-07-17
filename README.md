# APLIKASI PENGELOLA DATA KARYAWAN PERUSAHAAN
Selamat Datang di Repositori GitHub Saya!
Saya ingin memperkenalkan aplikasi yang saya rancang untuk membantu perusahaan dalam mengelola data karyawan menggunakan bahasa pemrograman Python. Aplikasi ini adalah bagian dari tugas Capstone Project untuk Program Bootcamp Data Scientist di Purwadhika Digital Technology School.
Aplikasi ini mengimplementasikan fitur CRUD (Create, Read, Update, and Delete) dan fitur Rata-rata Gaji Karyawan (Average Employee Salary). Aplikasi ini merupakan versi pertama dan mungkin masih memiliki beberapa kekurangan yang akan saya perbaiki di versi selanjutnya.
Atas perhatiannya terima kasih.

![image](https://github.com/user-attachments/assets/92d8d8f8-67ad-41e7-ba0f-068d37f738e7)

## Menu Utama Aplikasi :
1. Menampilkan Daftar Karyawan : Fitur ini memudahkan menjelajahi data karyawan dengan opsi untuk melihat data lengkap,  mencari berdasarkan nama,  departemen,  jabatan,  atau rentang gaji bulanan.
2. Menambahkan Data Karyawan Baru : Menambahkan data karyawan baru ke dalam daftar
3. Menghapus Data Karyawan : Menghapus data karyawan berdasarkan ID Karyawan.
4. Mengupdate Data Karyawan : Mengedit data karyawan yang sudah ada berdasarkan ID Karyawan.
5. Rata-rata Gaji Karyawan : Menghitung dan menampilkan rata-rata gaji karyawan berdasarkan departemen atau keseluruhan.
6. Kembali ke Menu Utama


## FITUR UTAMA :
### "Menampilkan Daftar Karyawan"
#### FITUR SUBMENU READ KARYAWAN :
Dapat menginput berdasarkan pilihan Submenu. Pada fitur ini, User dapat memilih untuk menampilkan data karyawan secara keseluruhan atau mencari berdasarkan nama,  departemen,  jabatan,  atau rentang gaji bulanan.

![image](https://github.com/user-attachments/assets/75783be1-8c57-423a-ba0e-ab409d830f7b)

Jika pengguna memilih opsi "1. Tampilkan Seluruh Data Karyawan", maka output yang ditampilkan adalah sebagai berikut:

![image](https://github.com/user-attachments/assets/9bad1a4e-c2bf-49ba-87b4-441882ef387f)

Jika pengguna memilih opsi "2. Data Karyawan Tertentu", mereka akan diminta untuk memasukkan ID Karyawan yang ingin dicari. Jika ID Karyawan tersebut tidak ada atau salah, pengguna akan diminta untuk menginput ulang sampai benar. Setelah ID yang benar dimasukkan, data karyawan yang sesuai dengan ID tersebut akan ditampilkan.

![image](https://github.com/user-attachments/assets/3235d86a-2cfd-4f15-b0b4-348537f416c8)

Jika pengguna memilih opsi "3. Berdasarkan Nama", mereka akan diminta untuk memasukkan nama depan, tidak harus nama lengkapnya untuk meningkatkan efisiensi, Misalnya, jika nama yang dimasukkan diawali dengan "S" atau "SU", maka akan ditampilkan semua data karyawan yang namanya diawali dengan huruf "S" atau ""SU"".

![image](https://github.com/user-attachments/assets/dfe654ea-1556-4f54-8d3b-70c9c9b2818b)

Jika pengguna memilih opsi "4. Berdasarkan departemen", mereka akan diminta untuk memasukkan nama departemen tersebut, Misalnya, "Keuangan", maka akan ditampilkan semua karyawan yang bekerja di departemen tersebut.

![image](https://github.com/user-attachments/assets/bcb4da2d-45b7-4e24-8c8d-3412219f00ae)

Sama halnya seperti diatas jika  pengguna memilih opsi "5. Berdasarkan jabatan ", mereka akan diminta untuk memasukkan jabatan tersebut, Misalnya, "Akuntan", maka akan ditampilkan semua karyawan yang mempunyai jabatan tersebut.

![image](https://github.com/user-attachments/assets/4602d403-6d86-4a3a-85b9-513af7bc4fb5)

Jika pengguna memilih opsi "6. Berdasarkan Gaji Karyawan", mereka akan diminta untuk memasukkan minimal dan maksimal gaji bulanan yang diinginkan. Misalnya, jika minimal adalah 10 juta dan maksimalnya 15 juta, maka data karyawan dengan rentang gaji bulanan antara 10 juta hingga 15 juta akan ditampilkan.

![image](https://github.com/user-attachments/assets/7e926aad-d0f5-4b3e-9394-d6f6825b20cd)

----------

### "Menambahkan Data Karyawan"
#### FITUR SUBMENU UPDATE KARYAWAN :

![image](https://github.com/user-attachments/assets/15fe4bed-6386-4bf7-8155-468caa16f5f0)

![image](https://github.com/user-attachments/assets/8cee65da-8823-4fcf-becc-94914ea7f542)

Penambahan data karyawan melalui langkah-langkah berikut: pengguna memilih opsi "Tambah Data Karyawan", memasukkan detail karyawan (ID Karyawan dengan format ID-XXX, nama, departemen, jabatan, tanggal bergabung dengan format 1 Januari 2024, dan gaji bulanan). Setelah data dimasukkan, aplikasi menampilkan pesan konfirmasi dan tabel data karyawan untuk verifikasi. Pengguna kemudian mengonfirmasi penyimpanan data dengan memilih Y atau N. Jika Y dipilih, aplikasi menampilkan pesan bahwa data karyawan berhasil ditambahkan. Tetapi jika N dipilih maka data akan gagal disimpan

----------

### "Menghapus Data Karyawan"
#### FITUR SUBMENU DELETE KARYAWAN :

![image](https://github.com/user-attachments/assets/a451daf8-efac-4eaf-93e3-427758a28f25)

![image](https://github.com/user-attachments/assets/22cfe20c-255f-4c0f-b4d7-127f3e1d3625)

![image](https://github.com/user-attachments/assets/58356cf9-7408-4a99-9fd4-c20fa02453ea)

Hapus data karyawan melalui langkah-langkah berikut: pengguna memilih opsi "Hapus Data Karyawan", kemudian memasukkan ID karyawan yang ingin dihapus. Setelah data dimasukkan, aplikasi akan menampilkan pesan konfirmasi dan tabel data karyawan yang ingin dihapus. Pengguna kemudian mengonfirmasi penghapusan data dengan memilih Y atau N. Jika Y dipilih, aplikasi menampilkan pesan bahwa data karyawan berhasil dihapus. Jika N dipilih, aplikasi menampilkan pesan bahwa data karyawan gagal dihapus, dan pengguna akan kembali ke menu "Read Data", di mana data karyawan yang ingin dihapus tadi sudah tidak ada.

![image](https://github.com/user-attachments/assets/f54a7989-808d-4b24-8b94-4bd9a1411a3d)

![image](https://github.com/user-attachments/assets/7d6ffc8d-35fe-4d03-a196-23d6c29af808)

Jika pengguna memilih opsi "Hapus Semua Data Karyawan", akan muncul konfirmasi untuk memastikan apakah pengguna benar-benar ingin menghapus semua data karyawan. Jika Y dipilih, semua data karyawan akan terhapus secara permanen. Jika pengguna kemudian melihat ke menu "Read" dan mencoba menampilkan semua data karyawan, aplikasi akan mengonfirmasi bahwa data karyawan sudah tidak tersedia.

----------

### "Mengupdate Data Karyawan"
#### FITUR SUBMENU UPDATE KARYAWAN :

![image](https://github.com/user-attachments/assets/254b771a-0ae3-4b3d-bd20-6956fba5d54f)

Dalam tampilan sistem yang diatas, pengguna memulai dengan memilih opsi untuk memperbarui data karyawan dan memasukkan ID karyawan "id-004". Setelah sistem menampilkan detail karyawan yang relevan, termasuk nama, departemen, jabatan, tanggal bergabung, dan gaji bulanan, pengguna mengonfirmasi untuk melanjutkan pembaruan. Selanjutnya, pengguna memilih untuk memperbarui departemen dan menggantinya dengan "Quality Control". Setelah pengubahan tersebut, sistem mengonfirmasi bahwa data telah berhasil diperbarui, menampilkan informasi terkini dari karyawan tersebut, termasuk nama, ID karyawan, departemen baru, jabatan, tanggal bergabung, dan gaji bulanan. Proses ini memastikan pembaruan data berjalan lancar dan akurat, dengan langkah-langkah yang jelas untuk meminimalkan kesalahan dan memastikan keakuratan informasi dalam sistem.

----------

### "Hitung Total Gaji Karyawan"
#### FITUR SUBMENU CALCULATE KARYAWAN :

![image](https://github.com/user-attachments/assets/8139348c-6d4d-4e77-8f04-a88616ceba5a)

![image](https://github.com/user-attachments/assets/0782d986-4a4d-4df0-adc0-7972089153ae)

Menu ini juga menawarkan dua opsi tambahan yang sangat berguna: pengguna dapat melihat total gaji seluruh karyawan, serta total gaji karyawan per departemen. Fitur ini dirancang untuk mempermudah pengguna dalam memantau dan mengelola gaji karyawan secara efisien, memberikan kemudahan akses dan transparansi informasi keuangan dalam organisasi.




----------
#### Terima kasih atas perhatiannya! Jika memiliki pertanyaan atau saran yang ingin disampaikan untuk pengembangan lebih lanjut, saya akan sangat mengapresiasi masukannya. Silakan hubungi saya melalui email di ziattabaruk29@gmail.com atau bisa langsung ke linkedin saya di www.linkedin.com/in/ziatabaruk/
