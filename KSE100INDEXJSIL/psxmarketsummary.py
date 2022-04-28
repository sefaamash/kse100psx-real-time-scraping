from selenium import webdriver
from bs4 import BeautifulSoup
import time
import sqlite3
options=webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument("--start-maximized")
driver=webdriver.Chrome(r'C:\Users\aamash.khan\Desktop\kse100\chromedriver.exe',chrome_options=options)
driver.get("https://www.psx.com.pk/market-summary/")

def AutoMobileAssembler():
    conn = sqlite3.connect('kse100psxjsb.db')
    c = conn.cursor()
    conn.execute('''CREATE TABLE IF NOT EXISTS AutoMobileAssembler
                (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
    print("Database created and Successfully Connected to SQLite")
    c.execute('''DELETE FROM AutoMobileAssembler  ''')
    conn.commit()   
    try:
                   
                    page=driver.page_source
                    soup=BeautifulSoup(str(page),'html.parser')
            
                    AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                    Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                    table=Spansoup.find_all('div',{'class':'table-responsive'})[0]
                    Spansoup2=BeautifulSoup(str(table),'html.parser')
                    #print(Spansoup2)
                    print("*******************",Spansoup2.th.h4.text,'**********************')
                    scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                    Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                    scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                    for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
                        
                
                    #.......................GREEN..........................
                    print('**************************GREEN***************************')
                    for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                        print(date)
                        print(time)
                        scripg=det.find_all('td')[0].text
                        print(scripg)
                        ldcg=det.find_all('td')[1].text
                        print(ldcg)
                        openg=det.find_all('td')[2].text
                        print(openg)
                        highg=det.find_all('td')[3].text
                        print(highg)
                        lowg=det.find_all('td')[4].text
                        print(lowg)
                        currg=det.find_all('td')[5].text
                        print(currg)
                        chng=det.find_all('td')[6].text
                        print(chng)
                        volg=det.find_all('td')[7].text
                        print(volg)
                        
                      
                        c.execute('''INSERT INTO AutoMobileAssembler VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time ,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                        conn.commit()

                        #.......................RED..........................
                    print('**************************RED***************************') 
                    for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                        
                        print(date)
                        print(time)
                        scripr=det.find_all('td')[0].text
                        print(scripr)
                        ldcr=det.find_all('td')[1].text
                        print(ldcr)
                        openr=det.find_all('td')[2].text
                        print(openr)
                        highr=det.find_all('td')[3].text
                        print(highr)
                        lowr=det.find_all('td')[4].text
                        print(lowr)
                        currr=det.find_all('td')[5].text
                        print(currr)
                        chnr=det.find_all('td')[6].text
                        print(chnr)
                        volr=det.find_all('td')[7].text
                        print(volr)
                        c.execute('''INSERT INTO AutoMobileAssembler VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time ,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                        conn.commit()
                        #.......................BLUE..........................
                    print('**************************BLUE***************************') 
                    for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                        print(date)
                        print(time)
                        scripb=det.find_all('td')[0].text
                        print(scripb)
                        ldcb=det.find_all('td')[1].text
                        print(ldcb)
                        openb=det.find_all('td')[2].text
                        print(openb)
                        highb=det.find_all('td')[3].text
                        print(highb)
                        lowb=det.find_all('td')[4].text
                        print(lowb)
                        currb=det.find_all('td')[5].text
                        print(currb)
                        chnb=det.find_all('td')[6].text
                        print(chnb)
                        volb=det.find_all('td')[7].text
                        print(volb)
                        c.execute('''INSERT INTO AutoMobileAssembler VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time ,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                        conn.commit()
                        #print("Completed")
                    
    except  Exception as e:
                    date=None
                    time=None
                    scripg=None
                    ldcg=None
                    openg=None
                    highg=None
                    lowg=None
                    currg=None
                    chng=None
                    volg=None
                    scripr=None
                    ldcr=None
                    openr=None
                    highr=None
                    lowr=None
                    currr=None
                    chnr=None
                    volr=None
                    scripb=None
                    ldcb=None
                    openb=None
                    highb=None
                    lowb=None
                    currb=None
                    chnb=None
                    volb=None
                    print(" exception is "+e)
            
                    
                


    c.execute ('''SELECT * FROM AutoMobileAssembler''' )
    results = c.fetchall ( )
    print ( results )

        
            
def AutoMobileParts():
    conn = sqlite3.connect('kse100psxjsb.db')
    c = conn.cursor()
    conn.execute('DROP TABLE IF EXISTS AutoMobileParts  ')
    conn.execute('''CREATE TABLE IF NOT EXISTS AutoMobileParts
              (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
    print("Database created and Successfully Connected to SQLite")

    try:
                
        
               
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
            
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[0]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                    #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})    
        
                        
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO AutoMobileParts VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO AutoMobileParts VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO AutoMobileParts VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
                
    except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


    c.execute ('''SELECT * FROM AutoMobileParts''' )
    results = c.fetchall ( )
    print ( results )
def CableAndElectGoods():
        conn = sqlite3.connect('kse100psxjsb.db')
        c = conn.cursor()
        conn.execute('DROP TABLE IF EXISTS CableElecGoods ')
        conn.execute('''CREATE TABLE IF NOT EXISTS CableElecGoods
                (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
        print("Database created and Successfully Connected to SQLite")
    
        try:
                    page=driver.page_source
                    soup=BeautifulSoup(str(page),'html.parser')
            
                    AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                    Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                    table=Spansoup.find_all('div',{'class':'table-responsive'})[2]
                    Spansoup2=BeautifulSoup(str(table),'html.parser')
                    #print(Spansoup2)
                    print("*******************",Spansoup2.th.h4.text,'**********************')
                    scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                    Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                    scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                    for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
                
                    #.......................GREEN..........................
                    print('**************************GREEN***************************')
                    for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                        print(date)
                        print(time)
                        scripg=det.find_all('td')[0].text
                        print(scripg)
                        ldcg=det.find_all('td')[1].text
                        print(ldcg)
                        openg=det.find_all('td')[2].text
                        print(openg)
                        highg=det.find_all('td')[3].text
                        print(highg)
                        lowg=det.find_all('td')[4].text
                        print(lowg)
                        currg=det.find_all('td')[5].text
                        print(currg)
                        chng=det.find_all('td')[6].text
                        print(chng)
                        volg=det.find_all('td')[7].text
                        print(volg)
                        c.execute('''INSERT INTO CableElecGoods VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                        conn.commit()

                        #.......................RED..........................
                    print('**************************RED***************************') 
                    for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                        print(date)
                        print(time)

                        scripr=det.find_all('td')[0].text
                        print(scripr)
                        ldcr=det.find_all('td')[1].text
                        print(ldcr)
                        openr=det.find_all('td')[2].text
                        print(openr)
                        highr=det.find_all('td')[3].text
                        print(highr)
                        lowr=det.find_all('td')[4].text
                        print(lowr)
                        currr=det.find_all('td')[5].text
                        print(currr)
                        chnr=det.find_all('td')[6].text
                        print(chnr)
                        volr=det.find_all('td')[7].text
                        print(volr)
                        c.execute('''INSERT INTO CableElecGoods VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                        conn.commit()
                        #.......................BLUE..........................
                    print('**************************BLUE***************************') 
                    for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                        print(date)
                        print(time)

                        scripb=det.find_all('td')[0].text
                        print(scripb)
                        ldcb=det.find_all('td')[1].text
                        print(ldcb)
                        openb=det.find_all('td')[2].text
                        print(openb)
                        highb=det.find_all('td')[3].text
                        print(highb)
                        lowb=det.find_all('td')[4].text
                        print(lowb)
                        currb=det.find_all('td')[5].text
                        print(currb)
                        chnb=det.find_all('td')[6].text
                        print(chnb)
                        volb=det.find_all('td')[7].text
                        print(volb)
                        c.execute('''INSERT INTO CableElecGoods VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                        conn.commit()
                        print("Completed")
                    
        except  Exception as e:
                    date,time=None
                    scripg=None
                    ldcg=None
                    openg=None
                    highg=None
                    lowg=None
                    currg=None
                    chng=None
                    volg=None
                    scripr=None
                    ldcr=None
                    openr=None
                    highr=None
                    lowr=None
                    currr=None
                    chnr=None
                    volr=None
                    scripb=None
                    ldcb=None
                    openb=None
                    highb=None
                    lowb=None
                    currb=None
                    chnb=None
                    volb=None
            
                    
                


        c.execute ('''SELECT * FROM CableElecGoods''' )
        results = c.fetchall ( )
        print ( results )
    
def Cement():
 
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS Cement')
            conn.execute('''CREATE TABLE IF NOT EXISTS Cement
              (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
              
        
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[3]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)

                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO Cement VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO Cement VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO Cement VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
          
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM Cement''' )
            results = c.fetchall ( )
            print ( results )
def Chemical():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS Chemical')
            conn.execute('''CREATE TABLE IF NOT EXISTS Chemical
              (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
              
        
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[4]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO Chemical VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO Chemical VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO Chemical VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
              
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM Chemical''' )
            results = c.fetchall ( )
            print ( results )
def MutualFunds():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS MutualFunds')

            conn.execute('''CREATE TABLE IF NOT EXISTS MutualFunds
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                
               
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[5]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO MutualFunds VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO  MutualFunds VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO  MutualFunds VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
              
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM  MutualFunds''' )
            results = c.fetchall ( )
            print ( results )
    
        
         
        
def CommercialBank():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS CommercialBanks')

            conn.execute('''CREATE TABLE IF NOT EXISTS CommercialBanks
              (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                
        
                
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[6]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO CommercialBanks VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO CommercialBanks VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO CommercialBanks VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
                
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM   CommercialBanks''' )
            results = c.fetchall ( )
            print ( results )
    
        
def Engineering():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS Engineering')
            conn.execute('''CREATE TABLE IF NOT EXISTS Engineering
                        (Date TEXT,Tim TEXT,
Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
               
               
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[7]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)

            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO Engineering VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO Engineering VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO  Engineering VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
                
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM  Engineering''' )
            results = c.fetchall ( )
            print ( results )
def Fertilizers():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS Fertilizer ')
            conn.execute('''CREATE TABLE IF NOT EXISTS Fertilizer
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
               
        
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[8]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)

            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO Fertilizer VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO Fertilizer VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO Fertilizer VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
           
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM Fertilizer''' )
            results = c.fetchall ( )
            print ( results )
    
        
         
    
def FoodAndPersonal():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS FoodAndPersonal ')
            conn.execute('''CREATE TABLE IF NOT EXISTS FoodAndPersonal
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                
              
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[9]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO FoodAndPersonal VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO  FoodAndPersonal VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO FoodAndPersonal VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
             
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM FoodAndPersonal''' )
            results = c.fetchall ( )
            print ( results )
    
        
         
          
def GlassAndCeramics():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS GlassAndCeramic  ')
            conn.execute('''CREATE TABLE IF NOT EXISTS GlassAndCeramic
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                
        
             
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[10]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO GlassAndCeramic VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO GlassAndCeramic VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO  GlassAndCeramic VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
            
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM GlassAndCeramic''' )
            results = c.fetchall ( )
            print ( results )
    
        
def Insurance():
    
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS Insurance ')
            conn.execute('''CREATE TABLE IF NOT EXISTS Insurance
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                    
        
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[11]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO Insurance VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO  Insurance VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO Insurance VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM Insurance''' )
            results = c.fetchall ( )
            print ( results )
def InvBanks():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS InvBanks  ')
            conn.execute('''CREATE TABLE IF NOT EXISTS InvBanks
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
               
        
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[12]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO InvBanks VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO  InvBanks VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO InvBanks VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM InvBanks''' )
            results = c.fetchall ( )
            print ( results )
    
def LeasingCompanies():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS LeasingCompany ')
            conn.execute('''CREATE TABLE IF NOT EXISTS LeasingCompany
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:    
        
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[13]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)

            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO LeasingCompany VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO  LeasingCompany VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO LeasingCompany VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM LeasingCompany''' )
            results = c.fetchall ( )
            print ( results )
def LeatherTannery():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS LeatherTannery  ')
            conn.execute('''CREATE TABLE IF NOT EXISTS LeatherTannery
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
               
        
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[14]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO LeatherTannery VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO  LeatherTannery VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO LeatherTannery VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM LeatherTannery''' )
            results = c.fetchall ( )
            print ( results )
def MISCELLANEOUS():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS Miscellaneous ')
            conn.execute('''CREATE TABLE IF NOT EXISTS Miscellaneous
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                
        
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[15]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO  Miscellaneous VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO  Miscellaneous VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO  Miscellaneous VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM  Miscellaneous''' )
            results = c.fetchall ( )
            print ( results )
def MODARABAS():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS Modarabas  ')
            conn.execute('''CREATE TABLE IF NOT EXISTS Modarabas
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                 
        
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[16]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO  Modarabas VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO  Modarabas VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO Modarabas VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM Modarabas''' )
            results = c.fetchall ( )
            print ( results )
def OilAndGasExplore():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS OilAndGas ')
            conn.execute('''CREATE TABLE IF NOT EXISTS OilAndGas
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[17]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO  OilAndGas VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO  OilAndGas VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO OilAndGas VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM OilAndGas''' )
            results = c.fetchall ( )
            print ( results )
def OilAndGasM():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS OilAndGasMar ')
            conn.execute('''CREATE TABLE IF NOT EXISTS OilAndGasMar
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
               
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[18]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO  OilAndGasMar VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO  OilAndGasMar VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO OilAndGasMar VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM OilAndGasMar''' )
            results = c.fetchall ( )
            print ( results )
    
def PaperAndBoard():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS PaperAndBoard ')
            conn.execute('''CREATE TABLE IF NOT EXISTS PaperAndBoard
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[19]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO  PaperAndBoard VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO  PaperAndBoard VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO PaperAndBoard VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM PaperAndBoard''' )
            results = c.fetchall ( )
            print ( results )
def Pharma():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS Pharma ')

            conn.execute('''CREATE TABLE IF NOT EXISTS Pharma
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                
        
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[20]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)

            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)

                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO  Pharma VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO  Pharma VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO Pharma VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM Pharma''' )
            results = c.fetchall ( )
            print ( results )
def PowerGenAndDis():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS  PowerGeneratorAndDistributor ')
            conn.execute('''CREATE TABLE IF NOT EXISTS PowerGeneratorAndDistributor
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[21]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)

                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO  PowerGeneratorAndDistributor VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO PowerGeneratorAndDistributor VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO PowerGeneratorAndDistributor VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM PowerGeneratorAndDistributor''' )
            results = c.fetchall ( )
            print ( results )
    
def Refinery():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS Refinery  ')
            conn.execute('''CREATE TABLE IF NOT EXISTS Refinery
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[22]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)

            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO Refinery VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO Refinery VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO Refinery VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM Refinery''' )
            results = c.fetchall ( )
            print ( results )
def SugarAndAllied():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS SugarAllied  ')
            conn.execute('''CREATE TABLE IF NOT EXISTS SugarAllied
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[23]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO SugarAllied VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO SugarAllied VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO SugarAllied VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM SugarAllied''' )
            results = c.fetchall ( )
            print ( results )
    
    
def SyntheticAndRayon():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            
            conn.execute('DROP TABLE IF EXISTS SyntheticRayon  ')
            conn.execute('''CREATE TABLE IF NOT EXISTS SyntheticRayon
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[24]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO SyntheticRayon VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO SyntheticRayon VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO SyntheticRayon VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM SyntheticRayon''' )
            results = c.fetchall ( )
            print ( results )
def TechnologyAndCommunication():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS TechComm ')
            conn.execute('''CREATE TABLE IF NOT EXISTS TechComm
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[25]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO TechComm VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO TechComm VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO TechComm VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM TechComm''' )
            results = c.fetchall ( )
            print ( results )
def TextileComposite():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS TexttileComposit  ')
            conn.execute('''CREATE TABLE IF NOT EXISTS TexttileComposit
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
                
        
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[26]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)

                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO TexttileComposit VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO TexttileComposit VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO TexttileComposit VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM TexttileComposit''' )
            results = c.fetchall ( )
            print ( results )
def TextileSpinning():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS TexttilSpinning')
            conn.execute('''CREATE TABLE IF NOT EXISTS TexttilSpinning
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[27]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO TexttilSpinning VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO TexttilSpinning VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO TexttilSpinning VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM TexttilSpinning''' )
            results = c.fetchall ( )
            print ( results )
def TextileWeaving():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS Texttilweaving ')
            conn.execute('''CREATE TABLE IF NOT EXISTS Texttilweaving
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[28]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO Texttilweaving VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO Texttilweaving VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO Texttilweaving VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM Texttilweaving''' )
            results = c.fetchall ( )
            print ( results )
def Tobacco():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS TOBBACO  ')
            conn.execute('''CREATE TABLE IF NOT EXISTS TOBBACO
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[29]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO TOBBACO VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO TOBBACO VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO TOBBACO VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM TOBBACO''' )
            results = c.fetchall ( )
            print ( results )
def Transport():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS TRANSPORT  ')
            conn.execute('''CREATE TABLE IF NOT EXISTS TRANSPORT
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[30]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)

            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO  TRANSPORT VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO  TRANSPORT VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO  TRANSPORT VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM  TRANSPORT''' )
            results = c.fetchall ( )
            print ( results )
def VanaspatiAndAllied():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS VanasAndallied ')
            conn.execute('''CREATE TABLE IF NOT EXISTS VanasAndallied
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[31]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)

                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO VanasAndallied VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO VanasAndallied VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO VanasAndallied  VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM  VanasAndallied''' )
            results = c.fetchall ( )
            print ( results )
def wollen():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS Woolen ')
            conn.execute('''CREATE TABLE IF NOT EXISTS Woolen
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[32]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO  Woolen VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO  Woolen VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO  Woolen VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM  Woolen''' )
            results = c.fetchall ( )
            print ( results )
def RealStateInvestmentTrust():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS REALSTATEINV')
            conn.execute('''CREATE TABLE IF NOT EXISTS REALSTATEINV
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[33]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)

                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO REALSTATEINV VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO REALSTATEINV VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO REALSTATEINV  VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM REALSTATEINV''' )
            results = c.fetchall ( )
            print ( results )
def EXTradeFunds():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS ExchangeTradeFunds ')
            conn.execute('''CREATE TABLE IF NOT EXISTS ExchangeTradeFunds
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[34]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)
                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO ExchangeTradeFunds VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO ExchangeTradeFunds VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO  ExchangeTradeFunds VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM  ExchangeTradeFunds''' )
            results = c.fetchall ( )
            print ( results )
def FutureContracts():
            conn = sqlite3.connect('kse100psxjsb.db')
            c = conn.cursor()
            conn.execute('DROP TABLE IF EXISTS FutureContracts  ')
            conn.execute('''CREATE TABLE IF NOT EXISTS FutureContracts
                        (Date TEXT,Tim TEXT,Scrip TEXT, Ldcp TEXT,Oppen TEXT ,High TEXT,Low TEXT,Current TEXT,Change TEXT,Volume TEXT)''')
            print("Database created and Successfully Connected to SQLite")

            try:
            
                page=driver.page_source
                soup=BeautifulSoup(str(page),'html.parser')
        
                AutoAssembl=soup.find_all('div',{'id':'marketmainboard'})
                Spansoup=BeautifulSoup(str(AutoAssembl),'html.parser')
                table=Spansoup.find_all('div',{'class':'table-responsive'})[35]
                Spansoup2=BeautifulSoup(str(table),'html.parser')
                #print(Spansoup2)
                print("*******************",Spansoup2.th.h4.text,'**********************')
                scrig=Spansoup2.find_all('tr',{'class':'green-text-td'})
                Spansoupg=BeautifulSoup(str(scrig),'html.parser')
                scrir=Spansoup2.find_all('tr',{'class':'red-text-td'})
                for dt in soup.find_all('div',{'class':'col-sm-12 inner-content-table'}):
                        dati=dt.h4.text
                        date=dati[0:10]
                        
                        time=dati[11:16]
                        print(date)
                        print(time)
            
                #.......................GREEN..........................
                print('**************************GREEN***************************')
                for det in Spansoup2.find_all('tr',{'class':'green-text-td'}):
                    print(date)
                    print(time)

                    scripg=det.find_all('td')[0].text
                    print(scripg)
                    ldcg=det.find_all('td')[1].text
                    print(ldcg)
                    openg=det.find_all('td')[2].text
                    print(openg)
                    highg=det.find_all('td')[3].text
                    print(highg)
                    lowg=det.find_all('td')[4].text
                    print(lowg)
                    currg=det.find_all('td')[5].text
                    print(currg)
                    chng=det.find_all('td')[6].text
                    print(chng)
                    volg=det.find_all('td')[7].text
                    print(volg)
                    c.execute('''INSERT INTO FutureContracts VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripg,ldcg,openg,highg,lowg,currg,chng,volg))
                    conn.commit()

                    #.......................RED..........................
                print('**************************RED***************************') 
                for det in Spansoup2.find_all('tr',{'class':'red-text-td'}):
                    print(date)
                    print(time)
                    scripr=det.find_all('td')[0].text
                    print(scripr)
                    ldcr=det.find_all('td')[1].text
                    print(ldcr)
                    openr=det.find_all('td')[2].text
                    print(openr)
                    highr=det.find_all('td')[3].text
                    print(highr)
                    lowr=det.find_all('td')[4].text
                    print(lowr)
                    currr=det.find_all('td')[5].text
                    print(currr)
                    chnr=det.find_all('td')[6].text
                    print(chnr)
                    volr=det.find_all('td')[7].text
                    print(volr)
                    c.execute('''INSERT INTO FutureContracts VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripr,ldcr,openr,highr,lowr,currr,chnr,volr))
                    conn.commit()
                    #.......................BLUE..........................
                print('**************************BLUE***************************') 
                for det in Spansoup2.find_all('tr',{'class':'blue-text-td'}):
                    print(date)
                    print(time)
                    scripb=det.find_all('td')[0].text
                    print(scripb)
                    ldcb=det.find_all('td')[1].text
                    print(ldcb)
                    openb=det.find_all('td')[2].text
                    print(openb)
                    highb=det.find_all('td')[3].text
                    print(highb)
                    lowb=det.find_all('td')[4].text
                    print(lowb)
                    currb=det.find_all('td')[5].text
                    print(currb)
                    chnb=det.find_all('td')[6].text
                    print(chnb)
                    volb=det.find_all('td')[7].text
                    print(volb)
                    c.execute('''INSERT INTO FutureContracts VALUES(?,?,?,?,?,?,?,?,?,?)''',(date,time,scripb,ldcb,openb,highb,lowb,currb,chnb,volb))
                    conn.commit()
                    print("Completed")
      
            except  Exception as e:
                 date,time=None
                 scripg=None
                 ldcg=None
                 openg=None
                 highg=None
                 lowg=None
                 currg=None
                 chng=None
                 volg=None
                 scripr=None
                 ldcr=None
                 openr=None
                 highr=None
                 lowr=None
                 currr=None
                 chnr=None
                 volr=None
                 scripb=None
                 ldcb=None
                 openb=None
                 highb=None
                 lowb=None
                 currb=None
                 chnb=None
                 volb=None
           
                 
             


            c.execute ('''SELECT * FROM FutureContracts''' )
            results = c.fetchall ( )
            print ( results )
while True:
    AutoMobileAssembler()
    time.sleep(3)
    AutoMobileParts()
    time.sleep(3)
    CableAndElectGoods()
    time.sleep(3)
    Cement()
    time.sleep(3)
    Chemical()
    time.sleep(3)
    MutualFunds()
    time.sleep(3)
    CommercialBank()
    time.sleep(3)
    Engineering()
    time.sleep(3)
    Fertilizers()
    time.sleep(3)
    FoodAndPersonal()
    time.sleep(3)
    GlassAndCeramics()
    time.sleep(3)
    Insurance()
    time.sleep(3)
    InvBanks()
    time.sleep(3)
    LeasingCompanies()
    time.sleep(3)
    LeatherTannery()
    time.sleep(3)
    MISCELLANEOUS()
    time.sleep(3)
    MODARABAS()
    time.sleep(3)
    OilAndGasExplore()
    time.sleep(3)
    OilAndGasM()
    time.sleep(3)
    PaperAndBoard()
    time.sleep(3)
    Pharma()
    time.sleep(3)
    PowerGenAndDis()
    time.sleep(3)
    Refinery()
    time.sleep(3)
    SugarAndAllied()
    time.sleep(3)
    SyntheticAndRayon()
    time.sleep(3)
    TechnologyAndCommunication()
    time.sleep(3)
    TextileComposite()
    time.sleep(3)
    TextileSpinning()
    time.sleep(3)
    TextileWeaving()
    time.sleep(3)
    Tobacco()
    time.sleep(3)
    Transport()
    time.sleep(3)
    VanaspatiAndAllied()
    time.sleep(3)
    wollen()
    time.sleep(3)
    RealStateInvestmentTrust()
    time.sleep(3)
    EXTradeFunds()
    time.sleep(3)
    FutureContracts()
    time.sleep(86400)


         
         
