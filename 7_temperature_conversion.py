#latihan konversi satuan temperatur

#program konversi celcius ke satuan lain 

print('\nPROGRAM KONVERSI TEMPERATUR\n')

celcius = float(input('masukan suhu dalam celcius: '))
print('suhu adalah', celcius, 'Celcius')

#Reamur 
reamur = (4/5) * celcius
print('suhu dalam reamur', reamur, 'Reamur')

#Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print('suhu dalam fahrenheit', fahrenheit, 'Fahrenheit')

#Kelvi 
kelvin = celcius + 273
print('suhu dalam kelvin', kelvin, 'Kelvin')
