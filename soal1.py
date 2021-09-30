nama = "Ai Oktari"
umur = 28
tinggi = 153.1

print(f"Nama saya {nama}, umur saya {umur} tahun dan tinggi saya {tinggi} cm.")

teori = 80
praktek = 89

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

phi = 22/7
r = 10
L = phi * (r * r)

print(f"Luas lingkaran dengan jari jari {r} cm adalah {L} cm\u00b2")
print(f"Luas lingkaran dengan jari jari {r} cm adalah {L:.2f} cm\u00b2")