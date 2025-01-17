**Project 1**
--

1. Import dan Inisialisasi

    from fastapi import Body, FastAPI

    app = FastAPI()

FastAPI: Framework untuk membuat API dengan cepat dan mudah.
Body: Digunakan untuk menerima input JSON dalam request body.
app = FastAPI(): Membuat instance aplikasi FastAPI yang digunakan untuk mendefinisikan endpoint.

2. Data Dummy

    BOOKS = [
        {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
        ...
    ]

BOOKS: Sebuah list yang berisi dictionary tentang buku. Setiap dictionary memiliki atribut title, author, dan category.

3. Endpoint untuk Mendapatkan Semua Buku

    @app.get("/books")
    async def read_all_books():
        return BOOKS

HTTP Method: GET.
URL: /books.
Fungsi: Mengembalikan semua data buku yang ada dalam list BOOKS.

4. Endpoint untuk Mendapatkan Buku Berdasarkan Judul

    @app.get("/books/{book_title}")
    async def read_book(book_title: str):
        for book in BOOKS:
            if book.get('title').casefold() == book_title.casefold():
                return book

HTTP Method: GET.
URL: /books/{book_title}.
Fungsi: Mencari buku berdasarkan judul. book_title adalah parameter path yang diterima dari URL.
casefold(): Digunakan untuk perbandingan string tanpa memedulikan huruf besar/kecil.

5. Endpoint untuk Mendapatkan Buku Berdasarkan Kategori (Query Parameter)

    @app.get("/books/")
    async def read_category_by_query(category: str):
        books_to_return = []
        for book in BOOKS:
            if book.get('category').casefold() == category.casefold():
                books_to_return.append(book)
        return books_to_return

HTTP Method: GET.
URL: /books/.
Query Parameter: category (contoh: /books/?category=science).
Fungsi: Mengembalikan buku-buku yang termasuk dalam kategori tertentu.

6. Endpoint untuk Mendapatkan Buku Berdasarkan Penulis

    @app.get("/books/byauthor/")
    async def read_books_by_author_path(author: str):
        books_to_return = []
        for book in BOOKS:
            if book.get('author').casefold() == author.casefold():
                books_to_return.append(book)
        return books_to_return

HTTP Method: GET.
URL: /books/byauthor/.
Query Parameter: author.
Fungsi: Mengembalikan semua buku yang ditulis oleh penulis tertentu.

7. Endpoint untuk Mendapatkan Buku Berdasarkan Penulis dan Kategori

    @app.get("/books/{book_author}/")
    async def read_author_category_by_query(book_author: str, category: str):
        books_to_return = []
        for book in BOOKS:
            if book.get('author').casefold() == book_author.casefold() and \
                    book.get('category').casefold() == category.casefold():
                books_to_return.append(book)
        return books_to_return

HTTP Method: GET.
URL: /books/{book_author}/.
Parameter Path: book_author.
Query Parameter: category.
Fungsi: Mengembalikan buku yang sesuai dengan nama penulis dan kategori.

8. Endpoint untuk Membuat Buku Baru


    @app.post("/books/create_book")
    async def create_book(new_book=Body()):
        BOOKS.append(new_book)

HTTP Method: POST.
URL: /books/create_book.
Body Parameter: new_book.
Fungsi: Menambahkan buku baru ke dalam list BOOKS.

9. Endpoint untuk Memperbarui Buku


    @app.put("/books/update_book")
    async def update_book(updated_book=Body()):
        for i in range(len(BOOKS)):
            if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
                BOOKS[i] = updated_book

HTTP Method: PUT.
URL: /books/update_book.
Body Parameter: updated_book.
Fungsi: Memperbarui data buku berdasarkan judulnya.

10. Endpoint untuk Menghapus Buku

    @app.delete("/books/delete_book/{book_title}")
    async def delete_book(book_title: str):
        for i in range(len(BOOKS)):
            if BOOKS[i].get('title').casefold() == book_title.casefold():
                BOOKS.pop(i)
                break

HTTP Method: DELETE.
URL: /books/delete_book/{book_title}.
Parameter Path: book_title.
Fungsi: Menghapus buku dari list BOOKS berdasarkan judulnya.

**Alur Utama**
--

CRUD Operations: Aplikasi ini memungkinkan operasi CRUD (Create, Read, Update, Delete) pada data buku.
Parameter Path dan Query: Path parameter digunakan untuk mengidentifikasi entitas spesifik, sedangkan query parameter digunakan untuk filter.
JSON Body: Digunakan untuk operasi POST dan PUT, memanfaatkan Body() dari FastAPI.