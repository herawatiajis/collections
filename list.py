#Membuat list dan mengisi value/nilai
buah = ['mangga','apel','durian','rambutan','anggur']

#menampilkan list menggunakan perulangan
for b in buah:
    print(b)
    
b = 0
while b < len(buah):
    print(buah[b])
    b += 1

#mengupdate salah satu nilai/value dalam list
buah[0] = 'kiwi'
print(buah)

#menghapus salah satu nilai/value dalam list
buah.remove('apel')
print(buah)
del buah [2]
print(buah)
buah.pop()
print(buah)

#menambahkan salah satu nilai/value kedalam list
buah.append('cerry')
print(buah)
buah.insert(1,'pisang')
print(buah)