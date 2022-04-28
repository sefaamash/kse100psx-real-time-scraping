from re import I
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sqlite3
conn = sqlite3.connect('kse100psxjsb.db')
c = conn.cursor()
conn.execute('''CREATE TABLE IF NOT EXISTS INDICES
              (Name TEXT, Rate INT,Status TEXT,Perstat Text)''')
print("Database created and Successfully Connected to SQLite")


while True:
    c.execute('''DELETE FROM INDICES ''')
    conn.commit()    
    try:
            options=webdriver.ChromeOptions()
            options.add_argument("--log-level=3")
            options.add_argument("--start-maximized")
            driver=webdriver.Chrome(chrome_options=options)
            driver.get("https://www.psx.com.pk/market-summary/")
            page=driver.page_source
            soup=BeautifulSoup(str(page),'html.parser')
            name=soup.find_all('div',{'class':'owl-item cloned'})
            name1=soup.find_all('div',{'class':'owl-item'})
            name2=soup.find_all('div',{'class':'owl-item active'})
            Spansoup=BeautifulSoup(str(name),'html.parser')
          
            for i,j,k in zip(name,name1,name2):
                  
                  name=i.h3.text
                  rate=i.h4.text
                  status=i.h5.text
                  perstat=i.h6.text
                  print(name+" "+rate+" "+status+" "+perstat)
                  c.execute('''INSERT INTO INDICES VALUES(?,?,?,?)''',(name,rate,status,perstat))
                  conn.commit()
                  name1=j.h3.text
                  rate1=j.h4.text
                  status1=j.h5.text
                  perstat1=j.h6.text
                  print(name1+" "+rate1+" "+status1+" "+perstat1)
                  c.execute('''INSERT INTO INDICES VALUES(?,?,?,?)''',(name1,rate1,status1,perstat1))
                  conn.commit()
                  name2=k.h3.text
                  rate2=k.h4.text
                  status2=k.h5.text
                  perstat2=k.h6.text
                  print(name2+" "+rate2+" "+status2+" "+perstat2)
                  c.execute('''INSERT INTO INDICES VALUES(?,?,?,?)''',(name2,rate2,status2,perstat2))
                  conn.commit()
                   
            
                   
            print("Completed")
            time.sleep(5000)
    except Exception as e:
       name=None
       rate=None
       status=None
       perstat=None
       name1=None
       rate1=None
       status1=None
       perstat1=None
       name2=None
       rate2=None
       status2=None
       perstat2=None
    print()
    c.execute ('''SELECT * FROM INDICES''' )
    results = c.fetchall ( )
    print ( results )
    
                   
