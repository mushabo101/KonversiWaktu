def timeConverter(seconds):
    if a.isnumeric():
        seconds = int(a)
        if seconds <= 359999:
            mins, seconds = divmod(seconds, 60)
            hours, mins = divmod(mins, 60)
            return '%02d:%02d:%02d' % (hours, mins, seconds)
        elif type(a) == str or type(a) == float:
            return'Invalid Input !'


a = input('Masukkan detik : ')
print(timeConverter(a))