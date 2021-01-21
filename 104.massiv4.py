# massiv elementlari soni 
n=int(input('n='))
# list olamiz
listcha=[]
# endi massiv elementlariga qiymat olamiz
for i in range(n):
    print('listcha[',i,']=',end='')
    uzatgich=int(input())
    listcha.append(uzatgich)
# endi massivning eng kichik elementini topamiz.
eng_kichik=min(listcha)
# endi eng oxirgi eementni olib bir o'zgarchiga beramiz
# buni ko'rganmiz
oxirgi_element=listcha[-1] 
# endi eng kichik element indeksini topamiz
kichik_element_indeksi=listcha.index(eng_kichik)
# endi oxirgi qadam qiymatlarni joylashtiramiz
listcha[kichik_element_indeksi]=oxirgi_element
listcha[-1]=eng_kichik
print(listcha)
# mana bolajonlar ertagimiz o'z nihoyasiga yetdi!
# agar tushunmagan joyi chiqib qolsa 
# birdaniga derazadan sakrashni maslahat 
# beraman albatta 2 yoki undan yuqoriqavatga chiqib
