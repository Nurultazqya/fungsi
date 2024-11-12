def luaspersegipanjang (panjang, lebar):
    return panjang*lebar
def kelilingpersegipanjang(panjang,lebar):
    return 2*(panjang+lebar)
panjang=int(input("masukan panjang :"))
lebar=int(input("masukan lebar :"))
hasil_luas=luaspersegipanjang(panjang,lebar)
hasil_keliling=kelilingpersegipanjang(panjang,lebar)
hasil_luas = luaspersegipanjang(panjang, lebar)
print ("hasil luas adalah",hasil_luas)
print("keliling adalah",hasil_keliling)
