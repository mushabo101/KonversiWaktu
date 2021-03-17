def timeConverter(seconds): #fungsi untuk time Converter
    if a.isnumeric(): #mengecek apakah inputan adalah numeric
        seconds = int(a) #yes maka -> ubah input menjadi integer
        if seconds <= 359999: #input int kurang dari sama dengan 35999
            mins, seconds = divmod(seconds, 60) #konversi
            hours, mins = divmod(mins, 60) #konversi
            return '%02d:%02d:%02d' % (hours, mins, seconds) #simpan hasil konversi
        elif type(a) == str or type(a) == float: #check apabila inputan merupaka string atau float
            return'Invalid Input !'#hasil invalid input


a = input('Masukkan detik : ') #input pada terminal
print(timeConverter(a)) #Cetak hasil inputan
