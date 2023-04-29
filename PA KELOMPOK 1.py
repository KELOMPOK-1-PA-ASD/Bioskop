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
    
class tambah:

    def __init__(self):
        self._jenisfilm = ''
        self._jam_tayang = ''
        self._harga = 0
        self._studio = 0

    def addfilm(self):
        try:
            self._jenisfilm = input('Masukkan nama film: ')
            self._jam_tayang = input('Masukkan jam_tayang : ')
            self._harga = int(input('Masukkan harga film: '))
            print("""
            =========================================
            ||             kode studio 1-5         ||
            =========================================
            """)
            self._studio = int(input("masukkan nomor studio : "))
            if self._studio > 5:
                print("mohon masukkan sesuai pilihan")
                return False
            elif self._jam_tayang in kusus_jam_tayang and self._studio in kusus_studio:
                print("maaf jadwal bertabrakan")
                os.system("pause")
                time.sleep(2)
                clear()
                return False
            else:
                kusus_jam_tayang.append(self._jam_tayang)
                queue.enqueue(self._jenisfilm)
                jb.append(self._jenisfilm)
                link.addLast(self._jenisfilm)
                kusus_jenis.append(self._jenisfilm)
                kusus_harga.append(self._harga)
                kusus_studio.append(self._studio)
                return True
        except ValueError:
            print('film Tidak Dapat Ditambahkan')
            print('Mohon Memasukkan harga film Hanya Menggunakan Angka')
            return False

    def str(self):
        return '\t'.join(str(x) for x in [self._jenisfilm, self._jam_tayang, self._harga, self._studio])

