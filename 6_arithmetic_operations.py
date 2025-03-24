#operasi aritmatika

a = 10
b = 3

#operasi tambah + 
hasil = a + b
print(a,'+', b,'=', hasil)

#operasi pengurangan - 
hasil = a - b
print(a,'-',b,'=', hasil)

#operasi perkalian *
hasil = a * b
print(a,'*',b,'=', hasil)

#operasi pembagian
hasil = a / b
print(a,'/',b,'=', hasil)

#operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=', hasil)

#operasi modulus (sisa pembagian) %
hasil = a % b
print(a,'%',b,'=', hasil)

#operasi floor division (pembagian dibulatkan kebawah) //
hasil = a // b
print(a,'//',b,'=', hasil)

#prioritas operasi, operation precedence

"""
1. ()
2. eksponen **
3. perkalian dan kawannya * / % //
4. pertambahsn dan pengurangan
"""

x = 3
y = 2
z = 4

hasil = x * y + z - x ** y * x 
print(hasil)

#kurung akan mengambil langkang paling pertama
hasil = (x + z) * y
print('(', x, '+', z, ')', '*', y, '=', hasil)


