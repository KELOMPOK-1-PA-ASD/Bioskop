import time
from time import sleep
from datetime import datetime
from datetime import date
from typing import Deque
import os
from prettytable import PrettyTable
import mysql.connector
import pwinput

today = date.today()
day = today.strftime("%d-%m-%Y")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

tabel = PrettyTable()
users = PrettyTable()

mydb = mysql.connector.connect(
  host="db4free.net ",
  user="kelompok_1",
  password="kelompoksatu",
  database="bioskop_1"
)
mycursor = mydb.cursor()

print("""
==================================================================
||                  KELOMPOK 1 KELAS A1 ASD                     ||
||      AMALIA KARTIKA SARI                2209116013           ||
||      ANGELIA CRISTIN                    2209116015           ||
||      BERTHA JOY RODO SARAGI             2209116047           ||
==================================================================
""")
input(">>>Tekan enter untuk kembali ke menu<<<")
time.sleep(0.5)

beli_film = [
            {
                "jenis":"",
                "jam_tayang":"",
                "studio":0,
                "harga":0,
                "jumlah":0,
                "kembalian":0,
            },
        ]

# functions
def clear():
    time.sleep(0.5)
    os.system('cls')
    

