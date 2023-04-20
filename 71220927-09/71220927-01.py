cari_kata=input('Masukan kata yang dicari : ')
cari_kata=cari_kata.lower()

file='romeojuliet.txt'
handle=open(file,'r')

juliet=' '
for line in handle :
    line=((line.lower()).strip())
    for kata in line :
        if kata.isalpha:
            juliet=juliet+kata
        elif kata.isspace():
            juliet=juliet+' '


new=''
for word in juliet:
    if word.isalpha:
        new=new+word
    elif word.isspace():
            new=new+' '

        
new=new.split(' ')
i=0
for lit in new :
    if cari_kata==lit :
        i=i+1

print(f'Jumlah kata {cari_kata} : {i}')

handle.close()