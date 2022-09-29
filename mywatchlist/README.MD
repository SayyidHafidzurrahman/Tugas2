# My Watchlist
[Deployment Link for Assignment 3](http://tugas2yudi.herokuapp.com/mywatchlist/)

# Perbedaan JSON, XML, dan HTML
* HTML (Hypertext Markup Language) merupakan sebuah sistem yang sudah distandarisasi yang digunakan untuk membuat struktur sebuah laman web dan isinya.

* JSON (JavaScript Object Notation) adalah sebuah lightweight format yang digunakan untuk menyimpan dan menyalurkan data. JSON berbentuk JavaScript sehingga mudah dibaca dan diketik. JSON biasa digunakan untuk menserialisasi data yang terstruktur dan menggantinya melalui sebuah network, biasanya diantara server dan aplikasi web.

* XML (Extensive Markup Language) adalah sebuah bahasa pemrograman yang bertujuan untuk menspesifikasi custom markup languages, dan menyediakan lebih banyak dari hanya sekedar pertukaran data. 

# Alasan data delivery diperlukan dalam pengimplementasian sebuah platform
Pada platform, terjadi pertukaran data user dengan data yang ada di server. Data delivery disini berfungsi untuk mempermudah proses pengiriman data. HTML, XML, JSON merupakan beberapa format yang dipakai dalam data delivery, karena mudah dipahami dan juga mudah dalam mengembangkannya.

# Implementasi
1. Menjalankan perintah `python manage.py startapp mywatchlist` pada cmd setelah mengganti direktori ke folder main (Tugas2), untuk memmbuat aplikasi django 'mywatchlist'
2. Menambahkan `path('mywatchlist/', include('mywatchlist.urls'))` pada urls.py pada folder project_django untuk menghubungkan urlpatterns yang ada pada project_django dengan mywatchlist serta menambahkan mywatchlist pada `installed_app` yang ada di settings.py. Selanjutnya, melakukan pathing route pada mywatchlist/urls.py agar terhubung dengan fungsi-fungsi yang akan dijalankan pada mywatchlist/views.py
3. Membuat model data pada mywatchlist/models.py dengan fields `watched_movie, movie_name, movie_rating, release_date, movie_review`. Setelah itu, mengetik command `python manage.py makemigrations` dan `python manage.py migrate` pada cmd untuk mempersiapkan dan melakukan migrasi. Membuat text file initial_mywatchlist_data.json untuk menampung 10 set dari fields yang sudah dibuat. Jalankan `python manage.py loaddata initial_watchlist_data.json` untuk memasukkan data ke dalam database.
