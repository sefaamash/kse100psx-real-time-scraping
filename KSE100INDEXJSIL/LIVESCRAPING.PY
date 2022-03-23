from re import I
from numpy import append
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sqlite3
conn = sqlite3.connect('kse100psxjsb.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Shows
              (Item TEXT, Indx INT)''')
print("Database created and Successfully Connected to SQLite")

Item=[]
Index=[]
while True:
    try:
           
            loc='C:\chrome\chromedriver.exe'

            options=webdriver.ChromeOptions()
            options.add_argument("--log-level=3")
            options.add_argument("--start-maximized")
            driver=webdriver.Chrome(loc,chrome_options=options)
            driver.get("https://www.psx.com.pk/")
            page=driver.page_source
            soup=BeautifulSoup(str(page),'html.parser')
            rates=soup.find_all('div',{'class':'rates'})
            Spansoup=BeautifulSoup(str(rates),'html.parser')
            spans=soup.find_all('span',{'class':"symbolName"})
            spans2=soup.find_all('span',{'class':"symbolRate"})
            for span1,span2 in zip(spans,spans2):
                   
                    Item.append(span1.text)
                    print(Item)
                   
                    Index.append(span2.text)
                    print(Index)
            for i,j in zip(Item,Index):
                c.execute ( '''UPDATE Shows SET Item=?,Indx=?''',(i,j)) 
                conn.commit()  
                print('completed')
                
           
           
            time.sleep(7)
    except Exception as e:
        spanA=None
        spanB=None
    print()
    c.execute ( '''SELECT * FROM Shows''' )
    results = c.fetchall ( )
    print ( results )
   
    # close connection
    #conn.close ( )
    #UPDATE Shows SET Item=? WHERE Indx=?