import sqlite3
import types

from flask import session


def connect():
    con = sqlite3.connect('./data.db')
    return con

#cur.execute("CREATE TABLE NetworkSetting(key text,data text);")
#cur.execute("CREATE TABLE playerdata(session text,email text,money integer);")
#cur.execute("CREATE TABLE tr(f text,t text,m integer);")
def get(con,key):
    cur = con.cursor()
    cur.execute(f"SELECT data FROM NetworkSetting WHERE key = '{key}'")
    data=cur.fetchone()
    print(data[0])
    return data[0]

def getplayerdata(con,session):
    cur = con.cursor()
    cur.execute(f"SELECT money FROM playerdata WHERE session = '{session}'")
    data = cur.fetchone()
    try:
        print(type(data))
        if type(data) == types.NoneType:
            return "NID"
        else:
            return data[0]
    except:
        return "err"

def crpld(con,session,email):
    cur = con.cursor()
    cur.execute(f"INSERT INTO playerdata VALUES('{session}','{email}',0)")
    con.commit()

def s2e(con,session):
    cur=con.cursor()
    cur.execute(f"SELECT email FROM playerdata WHERE session = '{session}'")
    data = cur.fetchone()
    return data[0]
def send(con,session,to,aug):
    cur=con.cursor()
    cur.execute(f"SELECT money FROM playerdata WHERE email = '{to}'")
    data = cur.fetchone()
    if type(data) == types.NoneType:
        return "tNID"
    elif getplayerdata(con, session) < int(aug):
        return "NM"
    elif 0 >= int(aug):
        return "NZ"
    else:
        fm=getplayerdata(con,session)
        cur.execute(f"SELECT money FROM playerdata WHERE email = '{to}'")
        tm=cur.fetchone()
        cur.execute(f"UPDATE playerdata SET money={int(fm)-int(aug)} WHERE session = '{session}'")
        cur.execute(f"UPDATE playerdata SET money={int(tm[0])+int(aug)} WHERE email = '{to}'")
        con.commit()
        cur.execute(f"INSERT INTO tr VALUES('{s2e(con,session)}','{to}',{int(aug)})")
        con.commit()
        return "sended"