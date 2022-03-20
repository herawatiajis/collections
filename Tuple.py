#Membuat Tuple dan mengisi value/nilai ke dalamnya
nama = ('sakina','merry','virna','ainum','wajida')

#menampilkan Tuple menggunakan perulangan
print('='*10,'perulangan for','='*10)
for i in nama:
    print(i)
print('='*10,'perulangan while','='*10)
i = 0
while i < len(nama):
    print(nama[i])
    i += 1
#mengupdate salah satu nilai/value dalam Tuple
n = list(nama)
n [3] = 'intan'
nama = tuple(n)
print(nama)

#menghapus salah satu nilai/value dalam Tuple
n = list(nama)
n.remove('virna')
nama = tuple(n)
print(nama)

n = list(nama)
del n [3]
nama = tuple(n)
print(nama)

n = list(nama)
n.pop()
nama = tuple(n)
print(nama)

#menambahkan salah satu nilai/value kedalam Tuple
n = list(nama)
n.append('herawati')
nama = tuple(n)
print(nama)

n = list(nama)
n.insert(1,'fanni')
nama = tuple(n)
print(nama)

