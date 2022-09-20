# **My Katalog**
## Tugas 2 PBP 


:sparkles: [HTML Page](https://mykatalog.herokuapp.com/mywatchlist/html/) 

:sparkles: [Json Page](https://mykatalog.herokuapp.com/mywatchlist/json/)

:sparkles: [XML Page](https://mykatalog.herokuapp.com/mywatchlist/xml/)


1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

    **Jawab**  
![Group 1 (1)](https://user-images.githubusercontent.com/88421618/190133499-471edc0d-0e9f-4d88-9247-6a18084f1382.png)


2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

    **Jawab**  
Virtual environment berguna untuk pengisolasian proyek agar tidak tercampur dengan proyek-proyek lain. Virtual environment juga menginstall library yang dibutuhkan oleh proyek spesifik yang kita inginkan saja. Kita otomatis menginstall packages dan dependencies yang diperlukan dalam framework yang tidak diinstall secara global. Hal ini membuat package leih terorganisir, modul tidak tumpang tindih, konsisten, dan penggunaannya memungkinkan banyak versi environment.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

    **Jawab**  
- Pertama-tama, saya menambahkan fungsi *show_catalog* pada *views.py* untuk mengambil semua data dari json menggunakan syntax CatalogItem.objects.all(). Data tersebut akan di-return ke template html menggunakan render(). Di dalam fungsi saya juga menyertakan nama dan npm saya. 
- Selanjutnya, saya menambahkan path pada urls.py di folder katalog dan project_django menggunakan instruksi path() untuk routing fungsi *views.py*. 
- Setelah itu, dilakukan loaddata json untuk iterasi dari list untuk memetakan semua data dari fungsi show_katalog (disimpan di variabel context semua datanya) yang ada di *views.py* dengan syntax {{<key>}}. Pemetaan dilakukan di katalog.html dengan perintah render(request, "katalog.html", context).
- Langkah terakhir adalah untuk mendeploy ke Heroku. Buat respository secret mengandung nama app dan API key. Selanjutnya jalankan kembali deploy program yang awalnya gagal. Untuk mengakses laman katalog, tambahkan /katalog di akhir url herokuapp.
