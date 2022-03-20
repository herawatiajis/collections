#Membuat dictionary dan mengisi value/nilai ke dalamnya
bio = {'Nama' : 'Herawati','NIM' : 'D0221069','Hobby' : 'Menghalu'}

#menampilkan dictionary menggunakan perulangan
for i in bio:
    print(i, '->',bio[i])


#mengupdate  nilai/value dalam dictionary
bio ['Nama'] = 'Hera'
print(bio)

#menghapus salah satu nilai/value dalam dictionary
bio.pop('Hobby')
print(bio)
#menambahkan  nilai/value kedalam dictionary
bio ['Alamat'] = 'Dungkait'
print(bio)



