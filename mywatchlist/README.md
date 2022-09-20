# **My Watch List**
## Tugas 3 PBP 


### :sparkles: [HTML Page](https://mykatalog.herokuapp.com/mywatchlist/html/) 

### :sparkles: [JSON Page](https://mykatalog.herokuapp.com/mywatchlist/json/)

### :sparkles: [XML Page](https://mykatalog.herokuapp.com/mywatchlist/xml/)

#### **Perbedaan HTML, JSON, dan XML**
* HTML (HyperText Markup Language) digunakan untuk markup standar data di website dan tidak memiliki sintaks penyimpanan dan pertukaran data seperti JSON dan XML. 
* JSON (JavaScript Object Notation) adalah format pertukaran data yang ringan dan mudah dibaca. JSON dinilai memiliki sintaks yang lebih mudah dibandingkan XML dan juga lebih mudah dipahami serta dimanipulasi. 
* XML (Extensible Markup Language) adalah format pertukaran data yang digunaka untuk menyimpan dan mengangkut data dari satu aplikasi ke aplikasi lain melalui internet.

#### **Mengapa perlu ***Data delivery***?**
Aplikasi membutuhkan cara untuk menyimpan data yang didapat dari user ke dalam database. Data tersebut perlu dikirimkan secara aman dan cepat, tetapi antar bagian depan halaman dan bagian backend tidak dapat berkomunikasi secara langsung. OLeh karena itu, diperlukanlah perantara pertukaran data seperti JSON dan XML. Kehadiran perantara ini memudahkan user dan server untuk mengolah dan mengambil data yang ada dengan cepat.

#### **Pengimplementasian ***checklists*** **
1. Memulai app dengan 'startnewapp' baru di local respository tugas 2 bernama 'mywatchlist' yang secara otomatis mengenerate rangkaian file py awal.
2. Menambahkan path aplikasi mywatchilst ke 'urls.py' yang ada di project_django dan mywatchlist.
3. Membuat models di 'mywatchlist/models.py' berisi Class dan atribut yang yang dibutuhkan untuk setiap tipe data 'watched', 'title', 'rating', 'release_date', dan 'review'.
4. Migrate data menggunakan 'makemigrations' dan 'migrate'.
5. Membuat 'fixtures' berisi 'intial_mywatchlist_data.json' yang didalamnya memuat daftar movies. Setelah itu lakukan 'loaddata' pada file untuk menyimpan isinya ke database.
6. Membuat fungsi 'show_mywatchlist', 'show_mywatchlist_json', dan 'show_mywatchlist_xml'. Setalh itu tambahkan path tersebut ke file 'urls.py'.
7. Selanjutnya, di file 'Procfile' yang sudah ada, saya menambahkan potongan kode untk melakukan load data yang ada pada 'fixtures' dari aplikasi mywatchlist saya agar dapat di-*deploy"* ke Herokuapp.

#### POSTMAN
1. ![postman html](https://user-images.githubusercontent.com/88421618/191184714-a683f356-2b3d-4059-b460-591f117339f2.jpg)
2. ![postman json](https://user-images.githubusercontent.com/88421618/191184813-623cc4ba-c3db-43c2-80ad-9d01b0b026b5.jpg)
3. ![postman xml](https://user-images.githubusercontent.com/88421618/191184874-c0faefcc-6099-468e-929d-55e46bba5b70.jpg)
