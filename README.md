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
### Menampilkan Daftar Karyawan
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



### Menambahkan Data Karyawan
#### FITUR SUBMENU UPDATE KARYAWAN :

![image](https://github.com/user-attachments/assets/15fe4bed-6386-4bf7-8155-468caa16f5f0)

![image](https://github.com/user-attachments/assets/8cee65da-8823-4fcf-becc-94914ea7f542)

Menambahkan data karyawan baru ke dalam daftar. Pada menu ini, Anda dapat memasukkan nama, departemen, jabatan, tanggal bergabung, dan gaji bulanan karyawan. Jika terdapat kesalahan dalam penginputan, aplikasi akan meminta Anda untuk menginput ulang.


### Menghapus Data Karyawan
#### FITUR SUBMENU DELETE KARYAWAN :

![image](https://github.com/user-attachments/assets/a451daf8-efac-4eaf-93e3-427758a28f25)

![image](https://github.com/user-attachments/assets/22cfe20c-255f-4c0f-b4d7-127f3e1d3625)

![image](https://github.com/user-attachments/assets/58356cf9-7408-4a99-9fd4-c20fa02453ea)

![image](https://github.com/user-attachments/assets/f54a7989-808d-4b24-8b94-4bd9a1411a3d)

![image](https://github.com/user-attachments/assets/7d6ffc8d-35fe-4d03-a196-23d6c29af808)

Hapus Data Karyawan
Menghapus data karyawan berdasarkan ID Karyawan. Pada fitur ini, Anda hanya perlu memasukkan ID Karyawan untuk melakukan penghapusan. Jika ID Karyawan tidak sesuai, maka penghapusan akan gagal.


### Mengupdate Data Karyawan
#### FITUR SUBMENU UPDATE KARYAWAN :

![image](https://github.com/user-attachments/assets/254b771a-0ae3-4b3d-bd20-6956fba5d54f)

Edit Data Karyawan
Mengedit data karyawan yang sudah ada berdasarkan ID Karyawan. Pada fitur ini, Anda dapat mengedit data karyawan pada nama, departemen, jabatan, tanggal bergabung, dan gaji bulanan. Jika ada bagian yang tidak ingin diubah, Anda dapat menekan tombol enter untuk melewatkan perubahan tersebut.

![image](https://github.com/user-attachments/assets/8139348c-6d4d-4e77-8f04-a88616ceba5a)

![image](https://github.com/user-attachments/assets/0782d986-4a4d-4df0-adc0-7972089153ae)


### Hitung Total Gaji Karyawan 
#### FITUR SUBMENU CALCULATE KARYAWAN :

Rata-rata Gaji Karyawan
Menghitung dan menampilkan rata-rata gaji karyawan berdasarkan departemen atau keseluruhan. Pada fitur ini, Anda dapat melihat rata-rata gaji karyawan keseluruhan atau hanya berdasarkan departemen tertentu.

![image](https://github.com/user-attachments/assets/6a2ffb1f-2017-46ae-86e2-73ae7936dde8)


#### Jika memiliki pertanyaan atau saran yang ingin disampaikan untuk pengembangan lebih lanjut, saya akan sangat mengapresiasi masukannya. Silakan hubungi saya melalui email di ziattabaruk29@gmail.com. Terima kasih atas perhatiannya!
