from re import I
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sqlite3
conn = sqlite3.connect('kse100psxjsb.db')
c = conn.cursor()
conn.execute('''CREATE TABLE IF NOT EXISTS Shows
              (Item TEXT, Indx INT)''')
print("Database created and Successfully Connected to SQLite")
while True:
    c.execute('''DELETE FROM Shows ''')
    conn.commit()    
    try:
            options=webdriver.ChromeOptions()
            options.add_argument("--log-level=3")
            options.add_argument("--start-maximized")
            driver=webdriver.Chrome(chrome_options=options)
            driver.get("https://www.psx.com.pk/")
            page=driver.page_source
            soup=BeautifulSoup(str(page),'html.parser')
            rates=soup.find_all('div',{'class':'rates'})
            Spansoup=BeautifulSoup(str(rates),'html.parser')
            spans=soup.find_all('span',{'class':"symbolName"})
            spans2=soup.find_all('span',{'class':"symbolRate"})
            for span1,span2 in zip(spans,spans2):
                   spanA=span1.text
                   print(spanA)
                   spanB=span2.text
                   print(spanB)
                   c.execute('''INSERT INTO Shows VALUES(?,?)''',(spanA,spanB))
                   conn.commit()
                   
                   
            print("Completed")
            time.sleep(7)
    except Exception as e:
        spanA=None
        spanB=None
    print()
    #To see the updated results from database
    c.execute ('''SELECT * FROM Shows''' )
    results = c.fetchall ( )
    print ( results )
    
  
