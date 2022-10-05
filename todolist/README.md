# **Todo List**
## Tugas 4 PBP 

#### :sparkling_heart: [Registration Page](https://mykatalog.herokuapp.com/todolist/register/) 

#### :rocket: [Login Page](https://mykatalog.herokuapp.com/todolist/login/) 

#### :carousel_horse: [Todolist Page](https://mykatalog.herokuapp.com/todolist/)

#### :ferris_wheel: [Add Task Page](https://mykatalog.herokuapp.com/todolist/create-task/)

### :question:**Kegunaan '{% csrf_token %}' pada elemen '<form>' dan apa yang terjadi apabila tidak ada potongan kode**:question:
Kegunaan 'csrf_token' pada potongan kode tersebut adalah sebagai pelindung dari data form dengan method POST dari *breach attacks*. Situs web rawan terkena serangan jika tidak diproteksi dengan benar, dan salah satu jenis serangan yang rawan adalah CSRF sendiri. oleh karena itu digunakanlah 'csrf_token'. Kode ini akan menghasilkan token di server saat melakukan render *page* yang menjadi tolak ukur eksekusi.

### **Apakah kita dapat membuat elemen '<form> 'secara manual?** :information_desk_person:
Hal ini dapat dilakukan dengan langkah sebagai berikut.
1. Membuat form di file HTML dengan tag '<form>' 
2. Tambahkan atribut 'action' dan 'method="<http-request>"' sebagai pengarah alur data form dan bagaimana input akan dikirim.
3. Untuk dapat menerima input dari user, tambahkan tag '<input>' 
4. Menambahkan atribut 'name' pada tag '<input>' agar data dapat diakses oleh 'views.py' dengan melakukan call 'request'.

### :roller_coaster:**Proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML**:roller_coaster:
1. User melakukan input data pada form HTML.
2. Input data dari user terebut  diterima oleh fungsi tujuan yang sesuai di 'views.py' dan disimpan dalam suatu variabel dengan mengeksekusi perintah 'request.POST.get("<name>")'.
3. Jika data pada form valid, maka fungsi tersebut akan menginisiasi object baru.
4. Melakukan penyimpanan Data object Task ke *database* dengan command '<object>.save()'.
5. Menggunakan 'Task.objects.filter(user_id=request.user.id)' untuk mengambil semua object Task sesuai dengan data milik user tertentu, fungsi utama pada 'views.py'.
6. Semua data object Task akan dirender atau dikirimkan ke template HTML sebagai context.
7. UMelakukan iterasi pada 'todolist' untuk menampilkan setiap data Task di template HTML.

### :trumpet:**Implementasi CheckList** :trumpet:**
- [x] **Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.**
 
 Masuk ke direktori Tugas 2 PBP di _command prompt_ dan memberikan perintah berikut ini. 
 ```
 python manage.py startapp todolist

 ```
- [x] **Menambahkan _path_ `todolist` sehingga pengguna dapat mengakses http://localhost:8000/todolist.**
 
 Akses file `urls.py` yang berada pada folder `project-django` dan memasukkan _path_ `todolist` ke `urlpattern`
 ```
 urlpatterns = [
 path('todolist/', include('todolist.urls')),
 ]
 ```
- [x] **Membuat sebuah model Task yang memiliki atribut user, date, title, description**
 
 Akses 'models.py' dan tambahkan class dan atribut yang dibutuhkan. Setalah itu, lakukan migration data.
 ```
 ...
 class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=225)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
 ...
 ```
- [x] **Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.**
 
 Membuat fungsi 'register' pada 'views.py'
 ```
 ...
 def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # add to database
            messages.success(request, 'Account has been created successfully!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)
 ...
 ```
 Membuat fungsi 'login_user' pada 'views.py'
 ```
 ...
 def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # login
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # Membuat response
            timezone = pytz.timezone('Asia/Jakarta')
            response.set_cookie('last_login', str(datetime.datetime.now(tz = timezone))) # create cookie last_login 
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
 ...
 ```
 Membuat fungsi 'logout_user' pada 'views.py' 
 ```
 ...
 def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
 ...
 ```
- [x] **Membuat halaman utama todolist.**
 
 Membuat folder 'templates' dan membuat file HTML 'todolist.html' yang memuat daftar todo, tambah task, delete, dan logout button

- [x] **Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.**
 
 Pada app 'todolist', buat 'task_form.py' dan 'class TaskForm' untuk input user.
 ```
 ...
 class TaskForm(forms.Form):
    judul = forms.CharField()
    deskripsi = forms.CharField(widget=forms.Textarea)
 ...
 ```
- [x] **Membuat routing sehingga beberapa fungsi dapat diakses melalui URL**
 
 Menambahkan 'path' pada 'urls.py' di folder app 'todolist'
 ```
 ...
 urlpatterns = [
    path('', show_todolist, name="show_todolist"),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('create-task/', create_task, name='create_task'),
    path('update-status/<int:id>', update_state, name='update_status'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('logout/', logout_user, name='logout'),
 ]
 ...
 ```
- [x] **Melakukan _deployment_ ke Heroku**
 
 Melakukan 'add', 'commit', dan 'push' ke respository github. Karena respository adalah respository yang sudah terhubung ke Herokuapp dan sudah memuat semua file yang dibutuhkan untuk 'deplyment', app akan langsung dapat diakses melalui Heroku.
- [x] **Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.**
    
 ![First Acc](https://user-images.githubusercontent.com/88421618/192875988-f1b17c43-2e9c-4f64-ac4b-ce27e4e7950d.jpg)

 ![Second Acc](https://user-images.githubusercontent.com/88421618/192876155-8d8a3623-08e7-4c1e-9a3a-275ba22e15db.jpg)


# **Todo List**
## Tugas 5 PBP 

### :palm_tree: Perbedaan dari *Inline, Internal,* dan *External* CSS :palm_tree:
1. ***Inline CSS*** adalah kode CSS yang ditulis langsung pada atribut elemen HTML. *Inline CSS* ditulis di atribut  *style*dari setiap elemen HTML. 
**Kelebihan:**
- Efisien digunakan jika ingin menguji dan melihat perubahan pada satu elemen.
- Memiliki prioritas lebih tinggi sehingga berguna untuk memperbaiki kode dengan cepat.
- Proses *request* HTTP lebih kecil dan proses *load websit* akan berjalan lebih cepat.
**Kekurangan:**
- Tidak efektif untuk penerapan *style* pada banyak tag HTML.
- Penerapan banyak *style* dengan metode ini dapat menyebabkan struktur file terlihat berantakan.

2. ***Internal CSS*** adalah kode CSS yang ditulis dalam `tag <style>` di `<head>` HTML. Untuk merujuk pada kode CSS, kita bisa menggunakan ID, class, atau hanya element saja.
**Kelebihan:**
- Perubahan hanya berlaku pada halaman saja sehingga memungkinkan membuat halaman yang unik dan berbeda-beda.
- Tidak memerlukan *upload* beberapa file karena HTML dan CSS berada dalam satu file.
- Class dan ID dapat digunakan oleh `internal stylesheet`.
**Kekurangan:**
- Tidak efisien jika ingin menerapkan CSS yang sama dalam beberapa file.
- Menurunkan performa web karena CSS yang berbeda-beda memaksa dilakukannya *reloading* setiap ganti page di situs web.

3. ***External CSS*** adalah kode CSS yang ditulis terpisah dengan HTML. Kode eksternal disimpan dalam file berekstensi `.css`. Untuk menghubungkan file HTML dan CSS, pada HTML perlu ditambahkan `<link>`, yang menyertakan referensi ke path dimana file berada, di tag `<head>`.
**Kelebihan:**
- Mengecilkan ukuran file HTML dan membuat struktur kode HTML lebih rapi.
- Loading website lebih cepat.
- Efisien untuk penerapan CSS yang sama di beberapa halaman website.
**Kekurangan:**
- Halaman website akan butuh waktu untuk mengakses *styling* yang digunakan dari file CSS sehingga halaman belum tampil dengan sempurna hingga file CSS diakses.

### :leaves: Tag HTML5 :leaves:
Berikut adalah tag-tag yang ada di HTML5.
1. `<article>`     : Menambahkan text independen, seperti sebuah blog atau artikel koran
2. `<audio>`        : Menyisipkan audio
3. `<canvas>`       : Menyisipkan area yang dapat digunakan untuk menggambar grafik
4. `<dialog>`       : Menyisipkan dialog box atau subwindow
5. `<figcaption>`   : Menyisipkan caption untuk sebuah figure
6. `<figure>`       : Menyisipkan gambar yang diilustrasikan
7. `<footer>`       : Mendefinisikan bagian footer dari halaman
8. `<header>`       : Mendefinisikan bagian header dari halaman
9. `<menuitem>`     : Mendefinisikan list command yang dapat dipilih user
10. `<main>`        : Mendefinisikan bagian utama atau dominant content dari halaman
11. `<nav>`          : Mendefinisikan link navigasi

## :maple_leaf: Tipe-Tipe CSS Selector :maple_leaf:
Terdapat 3 tipe CSS selector, antara lain:
1. **CSS Element Selector** adalah selector yang memilih elemen HTML berdasarkan nama elemen terebut.
Contoh:
```
p {
  text-align: center;
  color: blue;
}
```
Keterangan: Semua elemen dengan tag `<p>` akan *center-aligned* dengan warna teks biru.
2. **CSS ID Selector** adalah selector yang menggunakan atribut dari elemen HTML untuk memilih elemen yang spesifik. Untuk memilih elemen dengan id yang spesifik, gunakan karakter `hash (#)` diikuti dengan id elemen.
Contoh:
Contoh:
```
#elem1 {
  text-align: left;
  color: yellow;
}
```
Keterangan: Rule CSS tersebut akan diaplikasikan ke elemen HTML yang memiliki id="elem1".
3. **CSS Class Selector** adalah selector yang memilih elemen HTML dengan atribut kelas yang spesifik. Untuk memilih elemen dengan class yang spesifik, gunakan karakter `period (.)` diikuti dengan nama kelas.
Contoh:
```
.wizzle {
  text-align: center;
  color: red;
}
```
Keterangan: Rule CSS tersebut akan diaplikasikan ke elemen yang berada di class="wizzle".

### :blossom: Implementasi *checklists* :blossom:
Berikut langkah-langkah implementasi yang saya terapkan:
- [x] **Membuat file `.css` untuk mengkostumisasi halaman.**
Saya menerapkan *Eksternal CSS*, dimana saya membuat folder static berisi file `.css`. Di dalam file tersebut terdapat *styling* (berupa class, element, hingga font) CSS untuk mesing-masing halaman, sehingg terdapat total 4 files. Setelah itu, agar file dapat diakses oleh HTML, saya menambahkan potongan kode untuk melakukan load pada file static. Potongan kodenya adalah sebagai berikut.
```
<head>
    {% load static %}
    <link rel="stylesheet" href="{% static '<nama-file>.css' %}">
</head>
```
- [x] **Membuat cards untuk menampilkan task.**
Pada file `todolist.css`, saya menambahkan kelas `.card` dengan potongan kode sebagai berikut.
```
.card {
    box-shadow: 0 10px 8px 5px rgb(12, 33, 100);
    background-color: #ECD5BB;;
    transition: 0.8s;
    border-radius: 10px;
    padding: 10px; 
    margin: 10px;
    margin-bottom: 40px;
    backdrop-filter: blur(6px);
    outline-style: groove;
    outline-color: #0B1C48;
    outline-width: 3px;
}
```
Dan karena kita akan menampilkan beberapa task dengan format penampilan yang sama, maka pada `todolist.html`, buat for-loop sebagai berikut.
```
{% for task in todolist %}
   ...
   <div class="card">
         <p class="task-date">{{task.date}}</p>
         <p class="task-title">{{task.title}}</p><hr>
         ...
            <a href="/todolist/delete-task/{{task.id}}">
               <button class="button3" type="submit">Delete</button>
            </a>
         </div>
   </div> 
   ... 
```
- [x] **Membuat keempat halaman menjadi *responsive*.**
Untuk membuat halaman web menjadi responsive, perlu diatur viewport. Nah, tag `viewport` ini sendiri telah terdapat di `base.html` yang diextends oleh file-file HTML yang dikostumisasi. Berikut potongan kode pada `base.html`.
```
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
  {% block meta %}
  {% endblock meta %}
</head>
```
Dengan extend di file HTML keempat laman yang dikostumisasi dilakukan dengan menambahkan `{% extends 'base.html' %}` setelah tag `<html>`.

Pada file `.css`, tambahkan class `.container` flexbox agar menyesuaikan dengan layar user.
```
.container {
    display: flex;
    justify-content: center;
}
```
Selain itu, saya juga menambahkan hover pada elemen-elemen dengan membuat class `<nama class>:hover`. Salah satunya adalah `.card:hover`.
 ```
.card:hover {
    box-shadow: 0 8px 16px 0 #3e8baf;
    background-color: #cbaaaa;
}
```
Dan `button:hover`
```
.button:hover {
    background-color: #0B1C48;
}
```
