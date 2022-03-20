#Membuat set dan mengisi value/nilai ke dalamnya
data = {'hera',19,1.48,False}

#menampilkan set menggunakan perulangan
for i in data:
    print(i)


#mengupdate  nilai/value dalam set


#menghapus salah satu nilai/value dalam set
data.remove('hera')
print(data)
data.pop()
print(data)
#menambahkan  nilai/value kedalam set
data.add(True)
print(data)
data.update({'kucing','ipa',7})
print(data)


