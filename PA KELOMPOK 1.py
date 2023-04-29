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

# sort with quickSort
def partition(arr, low, high):
    i = (low-1)      
    pivot = arr[high]    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

# search with fibonacci search
def searching(isi, x, n):
    fibonaci2 = 0 
    fibonaci1 = 1 
    fibonaci = fibonaci2 + fibonaci1 
    while (fibonaci < n):
        fibonaci2 = fibonaci1
        fibonaci1 = fibonaci
        fibonaci = fibonaci2 + fibonaci1
    offset = -1
    while (fibonaci > 1):
        i = min(offset+fibonaci2, n-1)
        if (isi[i] < x):
            fibonaci = fibonaci1
            fibonaci1 = fibonaci2
            fibonaci2 = fibonaci - fibonaci1
            offset = i
        elif (isi[i] > x):
            fibonaci = fibonaci2
            fibonaci1 = fibonaci1 - fibonaci2
            fibonaci2 = fibonaci - fibonaci1
        else:
            return i
    if(fibonaci1 and isi[n-1] == x):
        return n-1
    return -1

def search():
    n = len(jb)
    x = input("Masukan judul film Yang anda cari : ")
    clear()
    print("tunggu sebentar.")
    clear()
    print("tunggu sebentar..")
    clear()
    print("tunggu sebentar...")
    clear()
    isi = searching(jb, x, n)
    if isi >= 0:
        print("Ditemukan di no urut ke :",isi + 1)
    else:
        print(x,"Tidak ada di no urut atau tidak ada di daftar")

# Queue
class Queue:
    def __init__(self): 
        self.items = []
    def isEmpty(self): 
        return self.items == []
    def enqueue(self, item): 
        self.items.insert(0, item)
    def dequeue(self): 
        return self.items.pop()
    def size(self): 
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]
    def semua(self): 
        return self.items
      
tempat = penyimpanan()         
film = tambah()          
queue = Queue()           
link = LinkedList()                          
jb = []             
kusus_jenis = []              
kusus_jam_tayang = []             
kusus_harga = [] 
kusus_studio = []  

# log in and menu
username = ''
password = ''
def login():
    global username
    global password
    username = input("Masukkan Nama: ")
    password = pwinput.pwinput(prompt= "Masukkan password: ")
    cek = "SELECT * FROM data_pelanggan WHERE username = %s AND password = %s"
    values = (username, password)

    cursor = mydb.cursor()
    cursor.execute(cek, values)

    pelanggan = cursor.fetchone()
    if pelanggan:
        clear()
        print("tunggu sebentar.")
        clear()
        print("tunggu sebentar..")
        clear()
        print("tunggu sebentar...")
        clear()
        print("login berhasil")
        clear()
        menu_member()
    else:
        print(("username dan password anda salah"))
        os.system("pause")
        time.sleep(2)
        welcome()

def register():
    try:
        username = input('Masukan Nama Baru: ')
        print("||   HARAP MASUKKAN ANGKA    ||")
        password = pwinput.pwinput(prompt = 'Masukan Password Baru: ')

        ceknama = "SELECT * FROM data_pelanggan WHERE username = %s and password = %s"
        values = (username, password)

        cursor = mydb.cursor()
        cursor.execute(ceknama, values)

        pelanggan = cursor.fetchone()
        if pelanggan:
            print('Maaf, Username ini sudah digunakan')
            time.sleep(3)
            clear()
            register()
        else:
            sql = "INSERT INTO data_pelanggan (username, password) VALUES (%s,%s)"
            val = (username, password)
            cursor.execute(sql, val)
            mydb.commit()
            print(cursor.rowcount, "record inserted.")
            clear()
            print("tunggu sebentar.")
            clear()
            print("tunggu sebentar..")
            clear()
            print("tunggu sebentar...")
            clear()
            print("akun baru berhasil dibuat")
            welcome() 
    except:
        print("akun telah tersedia")
        os.system("pause")
        time.sleep(3)
        clear()
        register()

def admin():
    username = input("Masukkan Nama: ")
    password = pwinput.pwinput(prompt="Masukkan password: ")

    cek = "SELECT * FROM data_admin WHERE username = %s AND password = %s"
    values = (username, password)

    cursor = mydb.cursor()
    cursor.execute(cek, values)

    pegawai = cursor.fetchone()
    if pegawai:
        clear()
        print("tunggu sebentar.")
        clear()
        print("tunggu sebentar..")
        clear()
        print("tunggu sebentar...")
        clear()
        print("login berhasil")
        clear()
        menu_admin()
    else:
        print(("username dan password anda salah"))
        input(">>>Tekan enter untuk kembali ke menu<<<")
        time.sleep(0.5)
        clear()
        welcome()

def welcome():
    os.system('cls')
    print ('+===============================================+')
    print ('|         Selamat datang di bioskop xxi         |'), 
    print ('|         silakan login sesuai role anda        |'), 
    print ('+===============================================+')
    print ('|1. Admin                                       |'), 
    print ('|2. pelanggan                                   |'), 
    print ('|3. pelanggan baru                              |'), 
    print ('|4. Keluar aplikasi                             |'), 
    print ('+===============================================+')
    while True:
        try:
            options = int(input("masukan pilihan: "))
            break
        except:
            print("Masukan Dengan Angka")
    if options == 1:
        clear()
        admin()
        clear()
    elif options == 2:
        clear()
        login()
        clear()
    elif options == 3:
        clear()
        register()
        clear()
    elif options == 4:
        print(">>>Terima Kasih Telah Mengunjungi Bioskop kami<<<")
        raise SystemExit
    else:
        print("Pilihan Tidak Ada")
        welcome()
        
def menu_admin():
    ulang = 'ya'
    while ulang == 'ya':
        print ('+==========================+')
        print ("|   Selamat Datang Admin   |")
        print ('+==========================+')
        print ("|1. Tambah film            |")
        print ("|2. Lihat film             |")
        print ("|3. cari film              |")
        print ("|4. Hapus film             |")
        print ("|5. Ubah film              |")
        print ("|6. Data film yg masuk     |")
        print ("|7. Urutkan film           |")
        print ("|8. Logout                 |")
        print ("|9. Keluar aplikasi        |")
        print ('+==========================+')
        while True:
            try:
                pilih = int(input("Masukkan Pilihan Anda: "))
                break
            except:
                print("Masukan Dengan Angka")
        if __name__ == '__main__':
            if pilih == 1:
                clear()
                tempat.addfilm()
                input(">>>Tekan enter untuk kembali ke menu<<<")
                time.sleep(0.5)
                clear()
            elif pilih == 2:
                if len(tempat.films) < 1:
                    clear()
                    print('!!! tidak ada film yg tersedia !!!')
                    input(">>>Tekan enter untuk kembali ke menu<<<")
                    time.sleep(0.5)
                    clear()
                    continue
                clear()
                tempat.lihatdata()
                input(">>>Tekan enter untuk kembali ke menu<<<")
                time.sleep(0.5)
                clear()
                time.sleep(2)
            elif pilih == 3:
                if len(tempat.films) < 1:
                    clear()
                    print('!!! tidak ada film yg tersedia !!!')
                    input(">>>Tekan enter untuk kembali ke menu<<<")
                    time.sleep(0.5)
                    clear()
                    continue
                clear()
                tempat.lihatdata()
                search()
                input(">>>Tekan enter untuk kembali ke menu<<<")
                time.sleep(0.5)
                clear()
                    
            elif pilih == 4:
                if len(tempat.films) < 1:
                    clear()
                    print('!!! tidak ada film yg tersedia !!!')
                    input(">>>Tekan enter untuk kembali ke menu<<<")
                    time.sleep(0.5)
                    clear()
                    continue
                clear()
                tempat.lihatdata()
                while True:
                    try:   
                        item = int(input('Pilih Nomor film Yang Ingin Dihapus: '))
                        time.sleep(2)
                        break
                    except:
                        print("!!! Masukan Dengan Angka !!!")
                if item  > len(tempat.films):
                    clear()
                    print('!!! Pilihan Nomor Tidak Ada !!!')
                    input(">>>Tekan enter untuk kembali ke menu<<<")
                    time.sleep(0.5)
                    clear()
                else:
                    tempat.films.remove(tempat.films[item - 1])
                    jb.pop(item-1)
                    clear()
                    print("film Yang Anda Pilih Telah Dihapus")
                    input(">>>Tekan enter untuk kembali ke menu<<<")
                    time.sleep(0.5)
                    clear()
            elif pilih == 5:
                time.sleep(2)
                if len(tempat.films) < 1:
                    clear()
                    print('tidak ada film yg tersedia')
                    input(">>>Tekan enter untuk kembali ke menu<<<")
                    time.sleep(0.5)
                    clear()
                    continue
                clear()
                tempat.lihatdata()
                while True:
                    try:
                        item = int(input('Pilih Nomor film Yang Ingin Diupdate: '))
                        break
                    except:
                        print("Masukan Dengan Angka")
                if item  > len(tempat.films):
                    clear()
                    print('Pilihan Nomor Tidak Ada')
                    input(">>>Tekan enter untuk kembali ke menu<<<")
                    time.sleep(0.5)
                    clear()
                else:
                    clear()
                    ubah_barang = tambah()
                    if ubah_barang.addfilm() == True :
                        tempat.films.remove(tempat.films[item - 1])
                        jb.pop(item-1)
                        tempat.films.insert(item - 1, ubah_barang)
                        print('>>>film Yang Anda Pilih Telah Diupdate<<<')
                        input(">>>Tekan enter untuk kembali ke menu<<<")
                        time.sleep(0.5)
                        clear()
                if len(tempat.films) < 1:
                    clear()
                    print('tidak ada film yg tersedia')
                    input(">>>Tekan enter untuk kembali ke menu<<<")
                    time.sleep(0.5)
                    clear()
                    continue
            elif pilih == 6:
                clear()
                time.sleep(2)
                if len(tempat.films) < 1:
                    clear()
                    print('Tidak Ada film Yang Pernah Di Data atau Kosong')
                    input(">>>Tekan enter untuk kembali ke menu<<<")
                    time.sleep(0.5)
                    clear()
                    continue
                clear()
                print(link.printList())
                print("Banyaknya film Yang Pernah Masuk: ", queue.size())
                input("\nTekan Enter Untuk Kembali")
                clear()
                time.sleep(2)
            elif pilih == 7:
              clear()
              print ("============================================")
              print ("1. urutkan judul film secara ascending  ")
              print ("2. urutkan judul film secara descending ")
              print ("3. kembali                                  ")
              print ("============================================")
              while True:
                  try:
                      pilih = int(input("Masukkan Pilihan Anda: "))
                      break
                  except:
                      print("Masukan Dengan Angka")
                      clear()
              if pilih == 1:
                  clear()
                  time.sleep(2)
                  print("data film")
                  n = len(jb)
                  quickSort(jb, 0, n-1)
                  for x in jb:
                      print("~>",x)
                  input(">>>Tekan enter untuk kembali ke menu<<<")
                  time.sleep(0.5)
                  clear()

              elif pilih == 2:
                  clear()
                  time.sleep(0.5)
                  print("data film")
                  n = len(jb)
                  quickSort(jb, 0,  n-1 )
                  for i in range(0, len(jb)) :
                      jb[i] = (jb[i])
                      jb.sort(reverse = True)
                  for x in jb:
                      print("~>",x)
                  input(">>>Tekan enter untuk kembali ke menu<<<")
                  time.sleep(0.5)
                  clear()
            elif pilih == 8:
                clear()
                time.sleep(0.1)
                print((">>>anda berhasil logout<<<"))
                clear()
                print(">>>waktu anda logout<<<")
                print()
                print("~ tanggal  :",day)
                print("~ jam      :",current_time)
                print()
                input(">>>Tekan enter untuk kembali ke menu<<<")
                clear()
                welcome()
            elif pilih == 9:
                print(">>>Terima Kasih Telah Mengunjungi Bioskop kami<<<")
                raise SystemExit
            else:
                print("Pilihan Hanya 1-9!")
                print("Jika Ingin Kembali Ketik ya atau Jika Tidak Tekan Enter")
                ulang = input('Ingin Kembali? ')
    else:
        print(">>>Terima Kasih Telah Mengunjungi Bioskop kami<<<")
        raise SystemExit
        
def menu_member():
    ulang = 'ya'
    while ulang == 'ya':
        global username
        print('=========================')
        print(f'selamat datang {username}')
        print("=========================")
        print("|1. struk pembelian     |")
        print("|2. beli film           |")
        print("|3. logout              |")
        print("|4. Keluar aplikasi     |")
        print("=========================")
        while True:
            try:
                pilih = int(input("Masukkan Pilihan Anda: "))
                break
            except:
                print("Masukan Dengan Angka")
        if __name__ == '__main__':
            if pilih == 1:
                clear()
                print("==========================================")
                print("            struk pembelian               ")
                print()
                for i in range(len(beli_film)):
                    if beli_film[i]['jumlah'] > 1:
                        print("nama film         : ",beli_film[i]['jenis'])
                        print("jam_tayang film   : ",beli_film[i]['jam_tayang'])
                        print("Harga film        : ",beli_film[i]['harga'])
                        print("uang              : ",beli_film[i]['jumlah'])
                        print("kembalian         : ",beli_film[i]['kembalian'])
                        print("\n")

                print("==========================================")
                input(">>>Tekan enter untuk kembali ke menu<<<")
                clear()
                time.sleep(2)
            elif pilih == 2:
                time.sleep(2)
                if len(tempat.films) < 1:
                    clear()
                    print('>>>film tidak tersedia<<<')
                    input(">>>Tekan enter untuk kembali ke menu<<<")
                    time.sleep(0.5)
                    clear()
                    continue
                clear()
                tempat.membeli_film()
                input(">>>Tekan enter untuk kembali ke menu<<<")
                time.sleep(0.5)
                clear()
            elif pilih == 3:
                clear()
                time.sleep(0.1)
                print((">>>anda berhasil logout<<<"))
                clear()
                print(">>>waktu anda logout<<<")
                print()
                print("~ tanggal  :",day)
                print("~ jam      :",current_time)
                print()
                input(">>>Tekan enter untuk kembali ke menu<<<")
                clear()
                welcome()
            elif pilih == 4:
                print(">>>Terima Kasih Telah Mengunjungi Bioskop kami<<<")
                raise SystemExit
            else:
                print("Pilihan Hanya 1-4!")
                print("Jika Ingin Kembali Ketik ya atau Jika Tidak Tekan Enter")
                ulang = input('Ingin Kembali? ')
                
    else:
        print(">>>Terima Kasih Telah Mengunjungi Bioskop kami<<<")
        raise SystemExit

welcome()
