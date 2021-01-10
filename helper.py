import sqlite3
from sqlite3 import Error
from dbcon import db

def create_ptable():
    conn = db().connection.cursor()
    conn.execute(""" CREATE TABLE IF NOT EXISTS portfolio (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL UNIQUE,
                                        high_risk integer,
                                        low_risk integer
                                    ); """)
    print("created")

def insert_ptable(p_name,hrisk_amount,lrisk_amount):
    conn = db().connection
    conn.cursor().execute("INSERT INTO portfolio(name,high_risk,low_risk) VALUES( ?, ?, ?);",(p_name,hrisk_amount,lrisk_amount))
    conn.commit()
    print("portfolio created")

def update_ptable(p_name,hrisk_amount,lrisk_amount):
    conn = db().connection
    curr_portfolio = check_ptable(p_name)
    for record in curr_portfolio:
        updated_hrisk = update_pdata(record[2],hrisk_amount)
        updated_lrisk = update_pdata(record[3],lrisk_amount)

    conn.cursor().execute("UPDATE portfolio SET high_risk = ?,low_risk = ? WHERE name = ? ;",(updated_hrisk,updated_lrisk,p_name))
    conn.commit()
    print("updated potfolio")

def update_pdata(existing_amount, increament):
    return sum([existing_amount,increament])

def check_ptable(p_name):
    conn = db().connection.cursor()
    data = conn.execute("SELECT * FROM portfolio WHERE name = ? ;",(p_name,))
    x = data.fetchall()
    if x == []:
        print ("First Deposit for : "+p_name)
        return False
    else:
        return x