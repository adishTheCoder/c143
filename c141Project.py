from bs4 import BeautifulSoup as bs
import pandas as pd
import requests


page = requests.get("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")
soup = bs(page.content, "html.parser")
star_table=soup.find('table')

temp_list = []
table_rows=star_table.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    my_row=[]
    for i in td:
        print(i.contents[0])
        my_row.append(i.contents[0].text.strip())
    temp_list.append(my_row)


print(temp_list)
star_names=[]
distance=[]
mass=[]
lum=[]
radius=[]
for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    lum.append(temp_list[i][7])
    radius.append(temp_list[i][6])
df2 = pd.DataFrame(list(zip(star_names,distance,mass,radius,lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df2)

