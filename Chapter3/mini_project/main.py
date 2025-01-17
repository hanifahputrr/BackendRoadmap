from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from database import conn
from models import Buku

app = FastAPI()

# Membaca data buku
@app.get("/buku/")
def baca_buku():
    c = conn.cursor()
    c.execute("SELECT * FROM buku")
    hasil = c.fetchall()
    return hasil

# Menambahkan data buku
@app.post("/buku/")
def tambah_buku(buku: Buku):
    c = conn.cursor()
    c.execute("INSERT INTO buku (judul, penulis, genre, halaman, review) VALUES (?, ?, ?, ?, ?)",
              (buku.judul, buku.penulis, buku.genre, buku.halaman, buku.review))
    conn.commit()
    return {"message": "Buku berhasil ditambahkan"}

# Mengupdate data buku
@app.put("/buku/{id}")
def update_buku(id: int, buku: Buku):
    c = conn.cursor()
    c.execute("UPDATE buku SET judul=?, penulis=?, genre=?, halaman=?, review=? WHERE id=?",
              (buku.judul, buku.penulis, buku.genre, buku.halaman, buku.review, id))
    conn.commit()
    return {"message": "Buku berhasil diupdate"}

# Menghapus data buku
@app.delete("/buku/{id}")
def hapus_buku(id: int):
    c = conn.cursor()
    c.execute("DELETE FROM buku WHERE id=?", (id,))
    conn.commit()
    return {"message": "Buku berhasil dihapus"}
