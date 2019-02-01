from bs4 import BeautifulSoup
import requests
import csv
import time
import urllib
# Baglanacagimiz site
url = "https://www.imdb.com/chart/top"
# Siteye baglanti kurmak icin istekte bulunuyoruz
sayfa = urllib.request.urlopen(url)
soup = BeautifulSoup(sayfa,"html.parser")
#print(soup.prettify)
print("https://www.imdb.com/chart/top >>> HTML KODU CEKILDI")

#film listesi
film_list=[]
d_film_l=[]
#parse islemleri
table=soup.find("table",{"class":"chart full-width"})
tbody=table.find("tbody",{"class":"lister-list"})

for i in tbody.findAll("tr"):
    film_list.append(i)
print("SAYFA BOLUMLENDIRILDI")
   
for i in range(len(film_list)):
    film_name=film_list[i].a.img
    film_year=film_list[i].find("span",{"class":"secondaryInfo"})
    film_imdb=film_list[i].find("strong")
    print(i+1,".",film_name["alt"],film_year.text,film_imdb.text,"İnfo::",film_list[i].strong["title"])
    
print("Liste basarili bir sekilde olusturuldu")    
    
   

print("Yazma islemi tamamlandi")    

exit=input("Cikmak icin herhangi bir tusa basiniz.")
