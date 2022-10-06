# Tugas 5
[Deployment Link for Assignment 5](http://tugassayyid.herokuapp.com/todolist/)

## Inline, Internal, and External CSS

CSS dapat ditulis sebagai inline, internal, atau external. Inline CSS sederhananya adalah CSS yang ditulis langsung pada elemen khusus. Cara ini nyaman untuk digunakan jika ingin merubah sedikit atribut dari beberapa elemen pada website. Ex:
```html
<div style="width: 200vw; height: 100vh; ...">GigaChad</div>
```
Internal CSS is adalah sebuah cara untuk mengaplikasikan css untuk satu halaman saja. Hal ini dapat diterapkan dengan menaruh `<style>` tag yang membawa atribut styles pada CSS. Karena hanya teraplikasikan pada satu halaman, itu juga menjadi kelemahannya. Tapi untuk website yang hanya memeiliki satu halaman, atau memang hanya ingin diedit satu halaman saja, kita tidak perlu membuat file CSS tambahan sehingga lebih simple. Ex:
```html
<style>
    .GigaChad {
        color: goldrose;
        ...
    }
</style>
```
External CSS merupakan CSS yang ditulis di sebuah file css dengan format `.css`. Untuk mengakses file tersebut, sebuah laman harus menulis `<link>` tag. External CSS merupakan cara menulis CSS yang paling terstruktur. Karena satu external css bisa diakses oleh beberapa page sekaligus, bila ada suatu masalah, kita tidak perlu mengedit setiap page satu persatu. For example:
`styles.css`
```css
body {
    margin: 0.75;
    padding: 1;
}
```
`index.html`
```html
...
<link rel="stylesheet" href="styles.css" type="text/css">
...
```
## Perbedaan CSS Inline, Internal, dan External

| Inline | Internal | External |
|:- |:- |:- |
| Berupa atribut `style` pada *tag* suatu elemen. | Berupa *tag* `<style>` pada suatu *file* HTML. | Berupa *file* `.css` yang di-*import* ke *file* HTML. |
| Hanya mengatur *style* satu elemen. | Mengatur *style* semua elemen pada satu *file* HTML. | Mengatur *style* semua elemen pada satu *file* HTML dan *file* `.css` yang sama bisa digunakan di banyak *file* HTML. |

# HTML5 Tags Example

- `<div>`, sebuah elemen block yang mendefinisikan divisi.
- `<h(1-6)>`, sebuah elemen block yang mendefinisikan headings.
- `<p>`, mendefinisikan sebuah elemen paragraf.
- `<a>`, tag yang membuat hyperlink.
- `<body>`: Isi konten atau badan dari *file* HTML.
- `<table>`: Tabel.
- `<thead>`: Kepala tabel.
- `<tbody>`: Isi konten atau badan tabel.
- `<tr>`: Baris tabel.
- `<td>`: Data tabel.
- `<input>`: Elemen yang bisa diinteraksikan oleh pengguna untuk memberi data masukan.
- `<nav>`: sebuah elemen block yang mendefinisikan *Navigation bar*.
- `<br>`: *Line-break*.
- `<input>`, sebuah line yang menunjukkan bahwa *file* HTML menerima input dari user.
- `<footer>`, HTML semantic yang mendefinisikan footer dari sebuah halaman.
- dsb ...

# CSS Selectors

- `*`, menyeleksi semuanya
- `.gigachad`, sebuah class selector (Menyeleksi elemen yang `class`-nya adalah `gigachad`)
- `#sigma`, sebuah ID selector (Menyeleksi elemen yang `ID`-nya adalah `gigachad`)
- `huxithegod`: Menyeleksi elemen yang *tag*-nya adalah `huxithegod`.
- `body`, sebuah group selector (menyeleksi semua elemen yang tag nya sesuai)
- `::before`, mengembalikan konten yang ada sebelum referenced element
- dsb ...

# Implementation
1. Membuat folder static, mencari *file* `bootstrap.css` dan `bootstrap.css.map` di internet dan taruh di dalam *folder* `css` yang dibuat di *folder* `static`. Lalu membuat file style.css di folder css untuk menampung style jumbotron dan card.
2. *Import* `bootstrap.css` dan style.css ke `base.html`.
3. Melakukan modifikasi dengan menambahkan `nav`, `class`, `body`, `style` pada *file html* yang ada pada *todolist\templates\*
4. Memberi *style* seperti warna pada setiap elemen.
5. Menambahkan gambar latar belakang dengan mencantumkan gambar pada *folder* `images` yang ada di dalam *folder* `static` dan meng-*import* gambar tersebut pada `base.html` sebagai gambar latar belakang.
6. Menambahkan `<card>` untuk merepresentasikan setiap *task* sebagai satu *card* dengan *card*-*card* tersebut tersusun dari atas ke bawah pada *file* `todolist.html`.
7. Tambahkan *style* dan `container` untuk *card*-*card* tersebut supaya lebih bagus.
8. Tambahkan `.card:hover` pada `style.css` untuk yang membesarkan ukuran *card* apabila *cursor* menyentuh *card* tersebut.

