nama = input("Nama : ")
umur = input("Umur : ")
tinggi = input("tinggi : ")

print(f"Nama saya {nama}, umur saya {umur} tahun dan tinggi saya {tinggi} cm.")

teori = input("Nilai ujian teori : ")
praktek = input("Nilai ujian praktek : ")

t = float(teori)
p = float(praktek)

if (t >= 70) and (p >= 70 )  :
    print("Selamat, anda lulus!")
elif (t < 70) and (p < 70 )  :
    print("Anda harus mengulang ujian teori dan praktek.")
elif (t >= 70) :
     print("Anda harus mengulang ujian praktek.")
else :
    print("Anda harus mengulang ujian teori.")

phi = input( "π : ")
r = input("jari-jari : ")


p = float(phi)
j = float(r)

L = float(p * j**2)


print(f"Luas lingkaran dengan jari jari {r} cm adalah {L} cm\u00b2")
print(f"Luas lingkaran dengan jari jari {r} cm adalah {L:.2f} cm\u00b2")