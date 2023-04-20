


print('Buah yang tersedia : ')
file='buah.txt'
handle=open(file,'r') 
for buah in handle:
    print(buah.strip())

handle.close()

pers_buah=[]
handle=open(file,'r') 
for kata in handle:
    pers_buah.append(kata.strip())

    
del_fruit=input('Buah yang ingin dihapus : ')

if del_fruit in pers_buah:
    pers_buah.remove(del_fruit)
    print(f'Buah {del_fruit} telah dihapus')
else :
    print(f'Buah {del_fruit} tidak terdaftar')
    
handle=open(file,'w') 
for laim in pers_buah:
        handle.write(laim+ '\n')

handle.close()
        

