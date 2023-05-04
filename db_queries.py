import sqlite3
from datetime import datetime
from sqlite3.dbapi2 import Cursor, Timestamp
from helper_func import *


def addVehicleCheckin(vehicle_num, fare):
    conn = sqlite3.connect('vehicles.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS vehicle(
        vehicle_num text PRIMARY KEY,
        intime timestamp,
        outtime timestamp,
        base_fare real,
        total_fare real,
        total_time text
        );''')
    conn.commit()
    conn.execute("INSERT OR IGNORE INTO vehicle (vehicle_num,intime,base_fare) \
        VALUES (?,?,?)", (vehicle_num, datetime.now(), fare))
    conn.commit()
    conn.close()
    return True


def getIntime(vehicle_num):
    conn = sqlite3.connect('vehicles.db')
    cur = conn.cursor()
    cur.execute("SELECT intime,base_fare FROM vehicle WHERE vehicle_num=?",
                (vehicle_num,))

    rows = cur.fetchall()
    conn.close()
    return rows[0]


def view_db():
    conn = sqlite3.connect('vehicles.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM vehicle ")
    rows = cur.fetchall()
    print(rows)
    conn.close()


def addVehicleCheckout(vehicle_num):
    conn = sqlite3.connect('vehicles.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS vehicle(
        vehicle_num text PRIMARY KEY,
        intime timestamp,
        outtime timestamp,
        base_fare real,
        total_fare real,
        total_time text
        );''')
    conn.commit()
    end_time = datetime.now()
    st, base_fare = getIntime(vehicle_num)
    start_time = datetime.fromisoformat(st)
    total_time, total_fare = calculate_charges(
        start_time=start_time, end_time=end_time, base_charge=base_fare)
    conn.execute("UPDATE vehicle SET total_fare = ?,outtime = ? , total_time = ? WHERE vehicle_num = ?",
                 (total_fare, end_time, total_time, vehicle_num,))
    conn.commit()
    conn.close()
    return True


def getCheckoutdetails(vehicle_num):
    conn = sqlite3.connect('vehicles.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM vehicle WHERE vehicle_num=?", (vehicle_num,))
    rows = cur.fetchall()
    conn.close()
    return rows[0]

def delete(vehicle_num):
    conn = sqlite3.connect('vehicles.db')
    cur = conn.cursor()
    conn.execute("DELETE FROM vehicle WHERE vehicle_num = ?",(vehicle_num,))
    conn.commit()
    conn.close()


# addVehicleCheckin('Mh12345', 12.5165)
# addVehicleCheckout('Mh12345')
# view_db()
# addVehicleCheckin('AIBACC', 163.6516)
# addVehicleCheckout('AIBACC')
# view_db()

# addVehicleCheckin('JNOSCUOWV', 452.65)
# addVehicleCheckout('JNOSCUOWV')
# view_db()

# addVehicleCheckin('OJCNIIEC', 10.5165)
# addVehicleCheckout('OJCNIIEC')
# view_db()
# print(getCheckoutdetails('OJCNIIEC'))
