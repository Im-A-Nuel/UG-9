file='nilai.txt'
handle=open(file,'r')


i=1
for line in handle:
    line=line.strip()
    if i<=6:
        print(f'Nilai Tugas {i} : {line}')
    elif i==7:
        print(f'Nilai Ujian Tengah Semester : {line}')
    else:
        print(f'Nilai Akhir Semester : {line}')
    i+=1

handle.close()

file='nilai.txt'
handle=open(file,'r')

nilai=0
j=1
for angka in handle:
    angka=angka.strip()
    angka=int(angka)
    if j==1:
        nilai=nilai+(angka*5/100)
    elif j==2:
        nilai=nilai+(angka*5/100)
    elif j==3:
        nilai=nilai+(angka*10/100)
    elif j==4:
        nilai=nilai+(angka*5/100)
    elif j==5:
        nilai=nilai+(angka*15/100)
    elif j==6:
        nilai=nilai+(angka*10/100)
    elif j==7:
        nilai=nilai+(angka*22/100)
    elif j==8:
        nilai=nilai+(angka*28/100)
    j+=1


print(f'Nilai Akhir : {nilai:.2f}')

handle.close()