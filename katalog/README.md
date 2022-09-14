# **My Katalog**
## Tugas 2 PBP 


:U+1F338: [Home Page](https://mykatalog.herokuapp.com/) 

:U+1F3F5: [Catalog Page](https://mykatalog.herokuapp.com/katalog/)


1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
** Jawab **
![BAGAN](https://drive.google.com/file/d/1cE0dGXoh8ZtioUknLZLvq6PmFFWbWcrW/view?usp=sharing)


2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
** Jawab **
Virtual environment berguna untuk pengisolasian proyek agar tidak tercampur dengan proyek-proyek lain. Virtual environment juga menginstall library yang dibutuhkan oleh proyek spesifik yang kita inginkan saja. Kita otomatis menginstall packages dan dependencies yang diperlukan dalam framework yang tidak diinstall secara global. Hal ini membuat package leih terorganisir, modul tidak tumpang tindih, konsisten, dan penggunaannya memungkinkan banyak versi environment.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
** Jawab **
- Pertama-tama, saya menambahkan fungsi *show_catalog* pada *views.py* untuk mengambil semua data dari json menggunakan syntax CatalogItem.objects.all(). Data tersebut akan di-return ke template html menggunakan render(). Di dalam fungsi saya juga menyertakan nama dan npm saya. 
- Selanjutnya, saya menambahkan path pada urls.py di folder katalog dan project_django menggunakan instruksi path() untuk routing fungsi *views.py*. 
- Setelah itu, dilakukan loaddata json untuk iterasi dari list untuk memetakan semua data dari fungsi show_katalog (disimpan di variabel context semua datanya) yang ada di *views.py* dengan syntax {{<key>}}. Pemetaan dilakukan di katalog.html dengan perintah render(request, "katalog.html", context).
- Langkah terakhir adalah untuk mendeploy ke Heroku. Buat respository secret mengandung nama app dan API key. Selanjutnya jalankan kembali deploy program yang awalnya gagal. Untuk mengakses k=laman katalog, tambahkan /katalog di akhir url herokuapp.
