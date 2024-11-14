API_KEY="testkey" #API의 Key
port=5000 #Port
Currency="won" #화폐 단위
name="Network" #Network의 이름





























######################################################################################################
import sqlite3,os
if os.path.exists("./data.db"):
    os.remove("./data.db")
con = sqlite3.connect('./data.db')
cur=con.cursor()
cur.execute("CREATE TABLE NetworkSetting(key text,data text);")
cur.execute("CREATE TABLE playerdata(session text,email text,money integer);")
cur.execute("CREATE TABLE tr(f text,t text,m integer);")
cur.execute(f"INSERT INTO NetworkSetting VALUES('cur','{Currency}')")
cur.execute(f"INSERT INTO NetworkSetting VALUES('name','{name}')")
con.commit()
con.close()
######################################################################################################