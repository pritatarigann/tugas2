# **Todo List**
## Tugas 6 PBP 

#### :rocket: [Heroku Link](https://mykatalog.herokuapp.com/todolist/login/) 

### :sunny:**Perbedaan antara *asynchronous programming* dengan *synchronous programming***:sunny:

Synchronous programming adalah suatu konsep pemrograman di mana kode-kode program dijalankan secara sekuensial, yakni dijalankan satu-satu secara berurutan menurut urutan pada antrian eksekusi program. Hal ini menyebabkan jika dilakukan modifikasi pada web maka website akan meblokir client (tidak responsif). Proses akan dijalankan satu-per-satu secara bergantian.

Sedangkan, asynchronous programming adalah suatu konsep di mana kode-kode program dapat dieksekusi secara bersamaan tanpa perlu menunggu hingga eksekusi kode yang sebelumnya selesai. Dengan kata lain, web akan tetap responsif selama proses modifikasi berlangsung di web. Jadi selagi loading, dapat dikirim request lain tanpa harus menunggu proses yang sebalumnya selesai.

### :umbrella:**Paradigma *Event-Driven Programming*** :umbrella:

*Event Driven Programming* merupakan suatu paradigma pemrograman di mana objek dapat berkomunikasi secara tidak langsung dengan mengirimkan pesan satu sama lain melalui perantara. Pada *Event Driven Programming*, alur jalannya program ditentukan oleh *event* tertentu. *Event* ini dapat berupa aksi dari user, sensor spesifik, dan sebagainya. Pengiriman pesan tersebut dilakukan melalui event stream. Paradigma ini bergantung pada event dengan memperhatikan operasi apa yang akan diimplementasikan dari adanya event. Penerapan paradigma dalam tugas ini terdapat pada implementasi `Add Task`. Apabila tombol ditekan, maka akan terdapat event yang di trigger dan ditangani oleh AJAX sebagai perantara untuk mengirim data yang diisi dari form ke server.

## :maple_leaf: ***Asynchronous programming* pada AJAX** :maple_leaf:
AJAX merupakan suatu tool untuk menerapkan asynchronous programming pada halaman web. Dalam hal ini, AJAX dapat membuat halaman web ter-update secara asynchronous, yaitu browser tidak akan melakukan loading ulang keseluruhan halaman web jika hanya sebagian kecil dari halaman web yang mengalami perubahan, cukup bagian tersebut saja yang di-update. Untuk penerapannya dapat dilakukan dengan membuat fungsi di `view ` dan menambahkan url path baru di `urls` yang akan mereturn response JSON. Terapkan `get` dan `post` untuk mengakses, mengedit, dan mengirimkan data dari JSON ke server.

### :snowflake:**Implementasi *checklists***:snowflake:

[x] Membuat fungsi `show_json` pada *view* yang mereturn data task yang dimiliki user tertentu dalam bentuk JSON, fungsi `show_todolist_ajax` untuk merelende file `todolist.html`.
[x] Menambahkan `path('json/', show_json, name='show-json')` ke dalam urlpatterns di file *urls* 
[x] Mengubah *main path* pada urlpatterns ke `path('', show_todolist_ajax, name='show_todolist_ajax')`.
[x] Menambahkan *modal* menggunakan Bootstrap untuk menampung input data *task* dari user yang akan dimasukkan ke database pada `todolist.html`
[x] Menerapkan AJAX untuk menampilkan data di webpage (*asynchronous*) dengan membuat tag `script` berisi JavaScript. Dalam tag tersebut termuat fungsi `getData` untuk mengembalikan data JSON dari list user. Data tersebut menjadi argumen `show_data`. Pada fungsi ini akan dicek isi dari data dan melakukan *append*. Pada `$(document).ready(function(){})` akan dipanggil `getData` untuk mengupdate halaman secara *asynchronous*.
[x] Menghubungkan tombol `Add Task` dengan *modal*
[x] Membuat fungsi `create_task_ajax()` pada *views* untuk menambahkan input *task* ke database dan mengembalikan `JsonResponse`. 
[x] Menambahkan `path('add/', create_task_ajax, name='create-task-ajax')` di *urlpatterns*.

[x] Membuat fungsi `clearFields()` pada `<script>` di `todolist.html` untuk menghapus isi dari fields pada *modal*. 

**BONUS**
[x] Membuat fungsi `delete_ajax(id,request)` pada *views* untuk menghapus *task* yang spesifik dari id. 
