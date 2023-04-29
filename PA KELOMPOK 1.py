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

class penyimpanan:

    def __init__(self):
        self.films = []
        self._jenisfilm = ''
        self._jam_tayang = ''
        self._harga = 0
        self._studio = 0

    def addfilm(self):
        film = tambah()
        if film.addfilm() == True:
            self.films.append(film)
            print ()
            print('film Telah Ditambahkan')

    def membeli_film(self):
        tabel.field_names = ['No.', 'nama film', 'jam_tayang','studio', 'harga']
        tabel.clear_rows()
        for idx, film in enumerate(self.films) :
            tabel.add_row([idx + 1, film._jenisfilm, film._jam_tayang, film._studio, film._harga])
        print(tabel)
        while True:
            try:   
                pilih = int(input('Pilih nomor film yang ingin dibeli: '))
                time.sleep(2)
                break
            except:
                print("!!! Masukan Dengan Angka !!!")

        if pilih > len(self.films):
            print('Film Tidak Ditemukan')
            return False

        else:
            while True:
                try:
                    uang = int(input('Masukkan uang anda: '))
                    harga = self.films[pilih - 1]._harga
        
                    if uang < harga:
                        print('uang tidak cukup')
                        return False
                    else:
                        nama_film = self.films[pilih - 1]._jenisfilm
                        jam_tayang = self.films[pilih - 1]._jam_tayang
                        studio = self.films[pilih - 1]._studio
                        kembalian = uang - harga

                        beli_film.append({
                        'jenis': nama_film,
                        'jam_tayang': jam_tayang,
                        'studio': studio,
                        'harga': harga,
                        'jumlah': uang,
                        'kembalian': kembalian
                        })
                        print("film Yang Anda Pilih Telah Dibeli")
                        sql = "INSERT INTO invoice (nama_film, jam_tayang, studio, harga, uang, kembalian) VALUES (%s, %s,%s,%s,%s,%s)"
                        val = (nama_film, jam_tayang, studio, harga, uang, kembalian)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        print(mycursor.rowcount, "record inserted.")
                        clear()
                        menu_member()
                        return True
                except:
                    print("!!!Masukan Dengan Angka!!!")


    def lihatdata(self):
        tabel.field_names = ['No.', 'nama film', 'jam_tayang', 'studio', 'harga']
        tabel.clear_rows()
        for idx, film in enumerate(self.films) :
            tabel.add_row([idx + 1, film._jenisfilm, film._jam_tayang, film._studio, film._harga])
        print(tabel)

    def __str__(self):
        return '\t'.join(str(x) for x in [self.films])

     
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    
    def addLast(self, data):
        if self.head is None:
            self.head = Node(data)
            self.count += 1
        else:
            nodeAkhir = self.head
            while nodeAkhir.next is not None:
                nodeAkhir = nodeAkhir.next
            nodeAkhir.next = Node(data)
            self.count += 1
            
    def deleteNode(self,position):
        if self.head == None:
            return
        temp = self.head
        
        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        for i in range (position,-1):
            temp = temp.next
            if temp is None:
                break
        if temp is None :
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next
        
    def printList(self):
        if self.head is None:
            print('Linked List Kosong')
        else:
            nodeTampil = self.head
            print("film Yang Pernah Masuk: ")
            while nodeTampil is not None:
                print('-> ', nodeTampil.data)
                nodeTampil = nodeTampil.next
        print()
        
    def iterate_item(self):
        # Iterate the list.
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
        yield val
