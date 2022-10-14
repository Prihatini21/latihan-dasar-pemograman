# deskriptif
# membuat variabel nama barang
# membuat variabel harga barang
# membuat variabel persen harga
# input nama barang
# input harga barang
# menghitung harga barang
# harga barang * persen \ 100
# print harga barang beserta nama barang

while(True):
    nama_barang = input('masukan nama barang ')
    harga_barang = input('masukan harga barang')
    persen = 10
    harga_keuntungan = int(harga_barang) * int(persen) / 100
    harga_jual = int(harga_barang) + harga_keuntungan
    print(harga_barang,' dijual dengan: ',harga_jual)

    apakahlanjut = input('apakah ingin input barang lain? y lanjut n tidak') 
    if(apakahlanjut != 'y') :
        break



