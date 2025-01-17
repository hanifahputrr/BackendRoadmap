from pydantic import BaseModel

class Buku(BaseModel):
    id: int
    judul: str
    penulis: str
    genre: str
    halaman: int
    review: str