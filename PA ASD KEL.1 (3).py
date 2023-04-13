import time
from termcolor import colored
from time import sleep
from datetime import datetime
from datetime import date
from typing import Deque
import os
from prettytable import PrettyTable

today = date.today()
day = today.strftime("%d-%m-%Y")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

tabel = PrettyTable()
users = PrettyTable()

# data

data_admin = {"nama":"kelompok", "password":"1"}

pelanggan =  [
            {
                "nama":"angel",
                "password":"2004",
                "saldo":50000000,
            },
            {
                "nama":"bertha",
                "password":"2003",
                "saldo":50000000,
                
            },
            {

                "nama":"amel",
                "password":"2002",
                "saldo":50000000,
            },
        ]
beli_film = [
            {

                "jenis":"",
                "jam_tayang":"",
                "harga":0,
                "jumlah":0,
                "kembalian":0,
            },
        ]

# functions
def clear():
    time.sleep(1.5)
    os.system('cls')
  

class tambah:
    def __init__(self):
        self._jenisfilm = ''
        self._jam_tayang = ''
        self._harga = 0
    def addfilm(self):
        try:
            self._jenisfilm = input('Masukkan nama film: ')
            self._jam_tayang = input('Masukkan jam_tayang : ')
            self._harga = int(input('Masukkan harga film: '))
            queue.enqueue(self._jenisfilm)
            jb.append(self._jenisfilm)
            link.addLast(self._jenisfilm)
            kusus_jenis.append(self._jenisfilm)
            kusus_jam_tayang.append(self._jam_tayang)
            kusus_harga.append(self._harga)
            return True
        except ValueError:
            print('film Tidak Dapat Ditambahkan')
            print('Mohon Memasukkan harga film Hanya Menggunakan Angka')
            return False
    
    def __str__(self):
        return '\t'.join(str(x) for x in [self._jenisfilm, self._jam_tayang, self._harga])

class penyimpanan:
    def __init__(self):
        self.films = []
        self._jenisfilm = ''
        self._jam_tayang = ''
        self._harga = 0
    def addfilm(self):
        film = tambah()
        if film.addfilm() == True:
            self.films.append(film)
            print ()
            print('film Telah Ditambahkan')
    def membeli_film(self):
        tabel.field_names = ['No.', 'nama film', 'jam_tayang','harga']
        tabel.clear_rows()
        for idx, film in enumerate(self.films) :
            tabel.add_row([idx + 1, film._jenisfilm, film._jam_tayang, film._harga])
        print(tabel)

        pilih = int(input('Pilih nomor film yang ingin dibeli: '))
        if pilih > len(self.films):
            print('film Tidak Ditemukan')
            return False
        else:
            uang = int(input('Masukkan uang anda: '))
            nama_film = self.films[pilih - 1]._jenisfilm
            jam_tayang = self.films[pilih - 1]._jam_tayang
            harga = self.films[pilih - 1]._harga
        
            if uang < harga:
                print('uang tidak cukup')
                return False
            else:
                beli_film.append({
                'jenis': nama_film,
                'jam_tayang': jam_tayang,
                'harga': harga,
                'jumlah': uang,
                'kembalian': uang - harga
            })
                print ()
                pelanggan[0]["saldo"] = pelanggan[0]["saldo"] - harga - uang
                print("film Yang Anda Pilih Telah Dibeli")
                time.sleep(1.5)
                return True


    
    def lihatdata(self):
        tabel.field_names = ['No.', 'nama film', 'jam_tayang','harga']
        tabel.clear_rows()
        for idx, film in enumerate(self.films) :
            tabel.add_row([idx + 1, film._jenisfilm, film._jam_tayang, film._harga])
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
    print("sabar atuhhh.")
    clear()
    print("sabar atuhhh..")
    clear()
    print("sabar atuhhh...")
    clear()
    isi = searching(jb, x, n)
    if isi >= 0:
        print("Ditemukan di no urut ke :",isi)
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
jb = ["0"]             
kusus_jenis = []              
kusus_jam_tayang = []             
kusus_harga = []             
kusus_nama_user = []


for i in pelanggan:
    i = i["nama"]
    kusus_nama_user.append(i)


# log in and menus
username = ''
password = ''
def login():
    global username
    global password
    username = input("Masukkan Nama: ")
    password = input("Masukkan password: ")
    for each in pelanggan:
        if username == each["nama"] and password == each["password"]:
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
            break
    else:
        print(colored("username dan password anda salah", 'red'))
        welcome()

def register():
    nama = input('Masukan Nama Baru: ')
    for each in pelanggan:
        if  nama in each["nama"]:
            print("Nama sudah ada")
            welcome()
            break
    else:
        password = input('Masukan Password Baru: ')
        pelanggan.append(
            {
            'nama':(nama),
            'password':(password)}
        )
        kusus_nama_user.append(nama)
        clear()
        print("tunggu sebentar.")
        clear()
        print("tunggu sebentar..")
        clear()
        print("tunggu sebentar...")
        clear()
        print("akun baru berhasil dibuat")
        clear()
        welcome()
    
        

 
def admin():
    nama = input("Masukkan Nama: ")
    password = input("Masukkan password: ")
    if nama == data_admin['nama'] and password == data_admin['password']:
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
        print(colored("username dan password anda salah", 'red'))
        welcome()

        
def ubah_pw():
    pw = input("Masukkan password Lama: ")
    for each in pelanggan:
        if pw == each["password"] and password == each["password"]:
            each["password"] = input("Masukkan password Baru: ")
            clear()
            print("password Anda Berhasil Diganti")
            print("Login Kembali")
            login()
            break
    else:
        print(colored("password anda salah", 'red'))
        edit_akun()
        
def ubah_nama():
    lama = input("Masukkan Nama Lama: ")
    for each in pelanggan:
        if lama == each["nama"] and username == each["nama"]:
            each["nama"] = input("Masukkan Nama Baru: ")
            kusus_nama_user.append(each["nama"])
            kusus_nama_user.pop(kusus_nama_user.index(lama))
            clear()
            print("Nama Anda Berhasil Diganti")
            print("Login Kembali")
            login()
            break
    else:
        print(colored("nama anda salah", 'red'))
        edit_akun()

def edit_akun():
    print('Pilihan')
    print('1. Edit Nama')
    print('2. Edit password')
    print('3. Menu')
    while True:
        try:
            pilih = int(input('Masukkan Pilihan: '))
            break
        except:
            print("Masukan Dengan Angka")
    if pilih == 1:
        clear()
        ubah_nama()
    elif pilih == 2:
        clear()
        ubah_pw()
    elif pilih == 3:
        welcome()
    else:
        print('Pilihan Tidak Ada')
        edit_akun()

def welcome():
    print(colored('+===============================================+', 'cyan'))
    print(colored('|', 'cyan'), colored('Selamat datang di bioskop xxi                ', 'yellow'), colored('|', 'cyan'))
    print(colored('|', 'cyan'), colored('silakan login sesuai role anda               ', 'yellow'), colored('|', 'cyan'))
    print(colored('|===============================================|', 'cyan'))
    print(colored('|', 'cyan'), colored('1. Admin                                     ', 'yellow'), colored('|', 'cyan'))
    print(colored('|', 'cyan'), colored('2. pelanggan                                 ', 'yellow'), colored('|', 'cyan'))
    print(colored('|', 'cyan'), colored('3. register                                  ', 'yellow'), colored('|', 'cyan'))
    print(colored('|', 'cyan'), colored('4. Keluar aplikasi                           ', 'yellow'), colored('|', 'cyan'))
    print(colored('+===============================================+', 'cyan'))
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
        print("Terima Kasih Telah Mengunjungi Bioskop kami")
        raise SystemExit
    else:
        print("Pilihan Tidak Ada")
        
        welcome()

def menu_admin():
    ulang = 'ya'
    while ulang == 'ya':
        print(colored('==========================', 'cyan'))
        print(colored("Selamat Datang Admin",'green'))
        print(colored('==========================', 'cyan'))
        print(colored("1. Tambah film",'yellow'))
        print(colored("2. Lihat film",'yellow'))
        print(colored("3. cari film",'yellow'))
        print(colored("4. Hapus film",'yellow'))
        print(colored("5. Ubah film",'yellow'))
        print(colored("6. Data film yg masuk",'yellow'))
        print(colored("7. Data pelanggan",'yellow'))
        print(colored("8. Logout",'yellow'))
        print(colored("9. Keluar aplikasi",'yellow'))
        print(colored('==========================', 'cyan'))
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
                clear()
                time.sleep(1.5)
            elif pilih == 2:
                if len(tempat.films) < 1:
                    clear()
                    print('tidak ada film yg tersedia')
                    clear()
                    time.sleep(1.5)
                    continue
                clear()
                tempat.lihatdata()
                input("Tekan Enter Untuk Kembali")
                clear()
                time.sleep(1.5)
            elif pilih == 3:
                if len(tempat.films) < 1:
                    clear()
                    print('tidak ada film yg tersedia')
                    clear()
                    time.sleep(1.5)
                    continue
                clear()
                tempat.lihatdata()
                search()
                time.sleep(1.5)
                clear()
                    
            elif pilih == 4:
                if len(tempat.films) < 1:
                    clear()
                    print('tidak ada film yg tersedia')
                    clear()
                    time.sleep(1.5)
                    continue
                clear()
                tempat.lihatdata()
                while True:
                    try:
                        
                        item = int(input('Pilih Nomor film Yang Ingin Dihapus: '))
                        time.sleep(1.5)
                        break
                    except:
                        print("Masukan Dengan Angka")
                if item  > len(tempat.films):
                    clear()
                    print('Pilihan Nomor Tidak Ada')
                    clear()
                    time.sleep(1.5)
                else:
                    tempat.films.remove(tempat.films[item - 1])
                    jb.pop(item)
                    clear()
                    print("film Yang Anda Pilih Telah Dihapus")
                    clear()
                    time.sleep(1.5)
            elif pilih == 5:
                time.sleep(1.5)
                if len(tempat.films) < 1:
                    clear()
                    print('tidak ada film yg tersedia')
                    clear()
                    time.sleep(1.5)
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
                    clear()
                    time.sleep(1.5)
                else:
                    clear()
                    ubah_barang = tambah()
                    if ubah_barang.addfilm() == True :
                        tempat.films.remove(tempat.films[item - 1])
                        tempat.films.insert(item, ubah_barang)
                        print('film Yang Anda Pilih Telah Diupdate')
                        clear()
                        time.sleep(1.5)
                if len(tempat.films) < 1:
                    clear()
                    print('tidak ada film yg tersedia')
                    clear()
                    time.sleep(1.5)
                    continue
            elif pilih == 6:
                clear()
                time.sleep(1.5)
                if len(tempat.films) < 1:
                    clear()
                    print('Tidak Ada film Yang Pernah Di Data atau Kosong')
                    clear()
                    time.sleep(1.5)
                    continue
                clear()
                print(link.printList())
                print("Banyaknya film Yang Pernah Masuk: ", queue.size())
                input("\nTekan Enter Untuk Kembali")
                clear()
                time.sleep(1.5)
            elif pilih == 7:
                clear()
                users.field_names = ['Nama', 'Password']
                users.clear_rows()
                for i in range(len(pelanggan)):
                    users.add_row([pelanggan[i]['nama'], pelanggan[i]['password']])
                print(users)
                print(colored("============================================", 'cyan'))
                print(colored("1. urutkan nama pelanggan secara ascending",'yellow' ))
                print(colored("2. urutkan nama pelanggan secara descending",'yellow'))
                print(colored("3. kembali",'yellow'))
                print(colored("============================================", 'cyan'))
                while True:
                    try:
                        pilih = int(input("Masukkan Pilihan Anda: "))
                        break
                    except:
                        print("Masukan Dengan Angka")
                        clear()
                if pilih == 1:
                    clear()
                    time.sleep(1.5)
                    print("nama pelanggan")
                    n = len(kusus_nama_user)
                    quickSort(kusus_nama_user, 0, n-1)
                    for x in kusus_nama_user:
                        print("~>",x)
                    input("Tekan enter untuk kembali ke menu")
                    time.sleep(0.5)
                    clear()
                   
                    

                elif pilih == 2:
                    clear()
                    time.sleep(0.5)
                    print("nama pelanggan")
                    n = len(kusus_nama_user)
                    quickSort(kusus_nama_user, 0, n-1 )
                    for i in range(0, len(kusus_nama_user)) :
                        kusus_nama_user[i] = (kusus_nama_user[i])
                        kusus_nama_user.sort(reverse = True)
                    for x in kusus_nama_user:
                        print("~>",x)
                    input("Tekan enter untuk kembali ke menu")
                    time.sleep(0.5)
                    clear()
                    
                elif pilih == 3:
                    clear()
                    time.sleep(0.5)
                    
                    menu_admin()
                else:
                    clear()
                    print("Pilihan Tidak Ada")
                    clear()
                    time.sleep(0.5)
                    
                    menu_admin()
            elif pilih == 8:
                clear()
                time.sleep(0.1)
                print(colored("anda berhasil logout", 'green'))
                clear()
                print("waktu anda logout")
                print()
                print("~ tanggal  :",day)
                print("~ jam      :",current_time)

                welcome()
            elif pilih == 9:
                print("Terima Kasih Telah Mengunjungi Bioskop kami")
                raise SystemExit
            else:
                print("Pilihan Hanya 1-10!")
                print("Jika Ingin Kembali Ketik ya atau Jika Tidak Tekan Enter")
                ulang = input('Ingin Kembali? ')
    else:
        print("Terima Kasih Telah Mengunjungi Bioskop kami")
        raise SystemExit

def menu_member():
    ulang = 'ya'
    while ulang == 'ya':
        global username
        print(colored('==========================', 'cyan'))
        print(f'\033[1;32;40mselamat datang {username}\033[0m')
        print(f"\033[1;32;40msaldo anda: {pelanggan[0]['saldo']}\033[0m")
        print(colored("========================", 'cyan'))
        print(colored("1. struk pembelian",'yellow'))
        print(colored("2. beli film",'yellow'))
        print(colored("3. Edit Akun",'yellow'))
        print(colored("4. logout",'yellow'))
        print(colored("5. Keluar aplikasi",'yellow'))
        print(colored("========================", 'cyan'))
        while True:
            try:
                pilih = int(input("Masukkan Pilihan Anda: "))
                break
            except:
                print("Masukan Dengan Angka")
        if __name__ == '__main__':
            if pilih == 1:
                clear()
                print(colored("==========================================", 'cyan'))
                print("struk pembelian")
                print()
                for i in range(len(beli_film)):
                    if beli_film[i]['jumlah'] > 1:
                        print("nama film   : ",beli_film[i]['jenis'])
                        print("jam_tayang film   : ",beli_film[i]['jam_tayang'])
                        print("Harga film  : ",beli_film[i]['harga'])
                        print("uang          : ",beli_film[i]['jumlah'])
                        print("kembalian     : ",beli_film[i]['kembalian'])
                        print("\n")

                print(colored("==========================================", 'cyan'))
                input("Tekan enter untuk kembali ke menu")
                clear()
                time.sleep(1.5)
            elif pilih == 2:
                time.sleep(1.5)
                if len(tempat.films) < 1:
                    clear()
                    print('film tidak tersedia')
                    clear()
                    time.sleep(1.5)
                    continue
                clear()
                tempat.membeli_film()
                time.sleep(1.5)
                clear()
            elif pilih == 3:
                clear()
                time.sleep(1.5)
                edit_akun()
                clear()
            elif pilih == 4:
                clear()
                time.sleep(0.1)
                print(colored("anda berhasil logout", 'green'))
                clear()
                print("waktu anda logout")
                print()
                print("~ tanggal  :",day)
                print("~ jam      :",current_time)

                welcome()
            elif pilih == 5:
                print("Terima Kasih Telah Mengunjungi Bioskop kami")
                raise SystemExit
            else:
                print("Pilihan Hanya 1-6!")
                print("Jika Ingin Kembali Ketik ya atau Jika Tidak Tekan Enter")
                ulang = input('Ingin Kembali? ')
                
    else:
        print("Terima Kasih Telah Mengunjungi Bioskop kami")
        raise SystemExit

welcome()