from gpiozero import LED, Button
from datetime import datetime, timedelta
import mariadb
import time

def waterUpdate():
    mydb = mariadb.connect(
        host="localhost",
        user="admin",
        password="pace1167",
        database="last_water_change"
    )

    mycursor = mydb.cursor()
    current = datetime.datetime.now().date()
    sql = "INSERT INTO changeWater(last_date) VALUES('%s')" % (current)
    #val = (current)
    mycursor.execute(sql)

    #mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def getDate():
    mydb = mariadb.connect(
        host="localhost",
        user="admin",
        password="pace1167",
        database="last_water_change"
    )
    mycursor = mydb.cursor()

    sql = "SELECT last_date FROM changeWater ORDER BY Id DESC LIMIT 1;"
    mycursor.execute(sql)
    records = mycursor.fetchall()
    for row in records:
        last_date = row[0]
        #date_time_str = last_date
        #date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
        #print(date_time_str, date_time_obj())
        print(last_date)
        return(last_date)
    mycursor.close()
    
led = LED(27)
button = Button(3)
#time_delta = timedelta(days=10)
last_date = getDate()
last_dates = (last_date + timedelta(days=10))
current = datetime.now().date()
delta = current - last_dates


while int(delta.days)<0:
        print(int(delta.days))
        time.sleep(86400)
while True:
    led.blink
    if button.when_pressed:
        waterUpdate()
    continue


