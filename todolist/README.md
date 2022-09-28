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
- [x]**Membuat sebuah model Task yang memiliki atribut user, date, title, description**
 Akses 'models.py' dan tambahkan class dan atribut yang dibutuhkan. Setalah itu, lakukan migration data.
 ```
 ...
 class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=225)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)

 ```
- [x]**Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.**
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
- [x]**Membuat halaman utama todolist.**
 Membuat folder 'templates' dan membuat file HTML 'todolist.html' yang memuat daftar todo, tambah task, delete, dan logout button

- [x]**Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.**
 Pada app 'todolist', buat 'task_form.py' dan 'class TaskForm' untuk input user.
 ```
 ...
 class TaskForm(forms.Form):
    judul = forms.CharField()
    deskripsi = forms.CharField(widget=forms.Textarea)
 ...
 ```
- [x]**Membuat routing sehingga beberapa fungsi dapat diakses melalui URL**
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
- [x]**Melakukan _deployment_ ke Heroku**
 Melakukan 'add', 'commit', dan 'push' ke respository github. Karena respository adalah respository yang sudah terhubung ke Herokuapp dan sudah memuat semua file yang dibutuhkan untuk 'deplyment', app akan langsung dapat diakses melalui Heroku.
- [x]**Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.**
 ![First Acc](https://user-images.githubusercontent.com/88421618/192875988-f1b17c43-2e9c-4f64-ac4b-ce27e4e7950d.jpg)
![Second Acc](https://user-images.githubusercontent.com/88421618/192876155-8d8a3623-08e7-4c1e-9a3a-275ba22e15db.jpg)



