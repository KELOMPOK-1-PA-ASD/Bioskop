# Bioskop

## **Nama Anggota**
- **Amalia Kartika Sari** - 2209116013
- **Angelia Cristin** - 2209116015
- **Bertha Joy Rodo Saragi** - 2209116047

## **Dokumentasi Kelompok 1** 
<img width="960" alt="Screenshot 2023-04-29 112342" src="https://user-images.githubusercontent.com/121868323/235307274-c52a6a0e-9058-4713-9955-e28432ab5509.png">

## **Deskripsi Program**
Bioskop merupakan wadah bagi masyarakat untuk menikmati pertunjukkan film, dimana penonton mencurahkan segenap perhatiannya dan perasaannya kepada gambar hidup yang disaksikan. Bioskop dapat menenangkan, menyenangkan, maupun memberikan experience baru kepada setiap penontonnya. Film ditampilkan pada sebuah layar lebar dengan efek suara yang menjadi salah satu daya tarik masyarakat untuk menyaksikan sebuah film di tempat ini. film yang ditampilkan dalam bioskop juga dapat mencakup berbagai kalangan usia, mulai dari anak-anak, remaja, dewasa, maupun lansia. tak jarang bioskop juga menjadi opsi date untuk berbagai pasangan!.

Program ini merupakan program bioskop dimana terdapat fitur login untuk admin dan pelanggan dengan masing-masing fitur yang ada didalamnya yang fungsi utamanya adalah untuk memudahkan admin untuk menambah, mengupdate, menghapus dan melihat data film yang ada, juga memudahkan pelanggan dalam melakukan pembelian film bahkan pengeditan akun pelanggan tersebut.

## **Modul Implementasi**
Adapun modul yang digunakan dalam proyek ini yaitu:

* **OS** : menyediakan fungsi untuk berinteraksi dengan sistem operasi.
* **Time** : fungsi ini membawa parameter berupa angka yang menyatakan detik (lama) penundaan. Misalkan, ingin menunda selama 2 detik: time.sleep(2)
* **Date time** : digunakan untuk mengolah variabel bernilai tanggal/date dan waktu/time.
* **Typing** : 
* **Pretty table** : fitur yang digunakan untuk membuat table di bahasa pemrograman python. Fitur tersebut merupakan bagian dari library dan digunakan dalam pembuatan tabel khusus pemrograman ini.
* **Mysql connector** : digunakan untuk membuat Koneksi Database MySQL/MariaDB dan Python dengan MySQL Connector

## **Instalasi Modul**
```bash
pip install prettytable
```

```bash
pip install python-time
```

```bash
pip install DateTime
```

```bash
pip install mysql-connector-python
```

```bash
pip install pwinput
```

## **Struktur Program** 
Struktur Program yang kami gunakan pada project yang berjudul “Bioskop” kali ini adalah:
### 1.	Pretty Table

Pada kesempatan Big Project kali ini, kami menggunakan Pretty table untuk menyimpan serta menampilkan data pada bentuk tabel agar tampilan terlihat lebih rapih dan mempermudah pembaca untuk mencari data yang diinginkan. 
``` python
from prettytable import PrettyTable

tabel = PrettyTable()
users = PrettyTable()

tabel.field_names = ['No.', 'nama film', 'jam_tayang','harga']

def membeli_film(self):
    tabel.field_names = ['No.', 'nama film', 'jam_tayang','harga']
    tabel.clear_rows()
    for idx, film in enumerate(self.films) :
        tabel.add_row([idx + 1, film._jenisfilm, film._jam_tayang, film._harga])
    print(tabel)

```
### 2. Singly Linked list

Penerapan Singly Linked list pada Big Project kami ditujukan agar dapat mengimplementasi struktur data lain. alasan kami menggunakan singly linked list adalah karna singly linked list adalah struktur data yang termudah untuk di cocokkan ke struktur data lain.
``` python

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
```

### 3. Sort with Quick Sort

Kami menggunakan Quick Sort dalam menyorting data yang masuk pada Penyimpanan data User. kami memilih Quick Sort daripada sorting yang lain adalah karna Quick Sort lebih mudah di implementasikan pada Big Project kami

``` python
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
```

### 4. Search with Fibonacci search

Untuk serach, kami menggunakan Fibonacci search karna cocok untuk Big Project kami kali ini. Fibonacci search ini juga lebih cepat mengakses data pada suatu storage algoritma. implementasinya adalah saat mencari film yang ingin di beli, maka program akan mencari terlebih dahulu agar film dapat di cari

``` python
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
```

### 5. Struktur data dengan Queue

Struktur data yang kami terapkan pada Big Project ini adalah Struktur data Queue. dengan Struktur data ini, kita dapat menambah data dengan sesuai antrian yang dimana bertujuan agar data yang masuk teratur. dan kita juga dapat menghapus data sesuai antrian.

```python
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
```

### 6. List untuk menyimpan data

kami juga menggunakan list penyimpanan biasa yang dimana dapat menyimpan data yang ingin di tambah, ubah, edit, bahkan menghapus data yang ada di list tersebut

``` python
tempat = penyimpanan()         
film = tambah()          
queue = Queue()           
link = LinkedList()                          
jb = []             
kusus_jenis = []              
kusus_jam_tayang = []             
kusus_harga = []             
kusus_nama_user = []
```
### 7. Database Menggunakan Mysql

Kami menggunakan Database Mysql karena sebelumnya kami telah mempelajari database tersebut dan juga karna database ini lebih simple dan mudah untuk di terapkan dalam Big project kami.

``` python
import mysql.connector

mydb = mysql.connector.connect(
  host="db4free.net ",
  user="kelompok_1",
  password="kelompoksatu",
  database="bioskop_1"
)

print("film Yang Anda Pilih Telah Dibeli")
sql = "INSERT INTO invoice (nama_film, jam_tayang, studio, harga, uang, kembalian) VALUES (%s, %s,%s,%s,%s,%s)"
val = (nama_film, jam_tayang, studio, harga, uang, kembalian)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

username = input('Masukan Nama Baru: ')
password = input('Masukan Password Baru: ')

ceknama = "SELECT * FROM data_pelanggan WHERE username = %s and password = %s"
values = (username, password)

cursor = mydb.cursor()
cursor.execute(ceknama, values)

pelanggan = cursor.fetchone()
if pelanggan:
    print('Maaf, Username ini sudah digunakan')
    register()
else:
    sql = "INSERT INTO data_pelanggan (username, password) VALUES (%s,%s)"
    val = (username, password)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "record inserted.")
    
cek = "SELECT * FROM data_admin WHERE username = %s AND password = %s"
values = (username, password)

cursor = mydb.cursor()
cursor.execute(cek, values)

pegawai = cursor.fetchone()

```

## Fitur dan Fungsionalitas
Terdapat 3 bagian besar fitur di dalam Big Project kami. yaitu Menu Login, Menu Admin, dan Menu Pelanggan.

### A. Menu login
```python
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
```
Fitur yang ada di dalam codingan menu login di atas ada 4 yaitu Login sebagai Admin, Pelanggan, Pelanggan Baru, dan Keluar Aplikasi. untuk outputnya dapat dilihat pada gambar di bawah ini.

![menu login](https://user-images.githubusercontent.com/122262846/234256985-1852bb45-ac7c-4f34-946c-2a80efac4f08.png)

#### 1. Menu Login Admin
```python
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
```
pada menu login admin kita diminta untuk memasukkan nama dan password agar dapat masuk ke dalam menu admin. jika nama dan password salah, maka akan mengulang saat memasukkan nama dan password, tetapi jika benar akan masuk ke dalam menu admin. untuk data akun admin, data tersebut telah diatur di dalam database dimana data admin hanya bisa ditambahkan dari database dan tidak bisa ditambahkan sendiri melalui program. 

![login admin](https://user-images.githubusercontent.com/122262846/235283478-4d90dbdd-38d3-463f-a918-8480c52c518f.png)

#### 2. Menu Login Pelanggan
```python
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
```
Pada menu ini, kita juga akan diminta untuk memasukkan nama dan password kita.jika nama dan password benar maka akan masuk ke menu pengguna. dan jika gagal maka akan berulang saat memasukkan nama dan password. sama dengan data admin sebelumnya, data yang terdapat pada data pelanggan juga terdapat pada disimpan didalam database.

![pengguna](https://user-images.githubusercontent.com/122262846/235283488-a2e17f15-6651-4fe7-ba8f-5ac3835730dd.png)


#### 3. Menu Pelanggan baru
```python
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
```
Pada menu Pengguna baru, akan diarahkan untuk membuat akun baru dengan memasukkan nama dan password seperti gambar di bawah ini. lalu data yang baru dibuat akan masuk ke database yang dimana semua akun pengguna disimpan.

![register](https://user-images.githubusercontent.com/122262846/235283499-ff3fc6bf-0676-4b15-8ac4-03d3f00c5f5b.png)


#### 4. Keluar Aplikasi
```python
 print(">>>Terima Kasih Telah Mengunjungi Bioskop kami<<<")
        raise SystemExit
```
menu ini diperuntukan saat pengguna telah selesai menggunakan program.

![KA Login](https://user-images.githubusercontent.com/122262846/234490420-3c7a8d2b-64b3-42ac-80ac-24179e0b0d9f.png)


### B. Menu Admin
```python
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
```
Fitur yang digunakan pada menu admin ada 9 yaitu:

![menu admin](https://user-images.githubusercontent.com/122262846/234257046-5ac4cc22-182f-45d5-9df2-3851fe1f91a1.png)

#### 1. Tambah Film
```python
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
```
pada bagian ini data film akan disimpan sementara pada class tambah yang kemudian akan disimpan di class penyimpanan.
```python
    def addfilm(self):
        film = tambah()
        if film.addfilm() == True:
            self.films.append(film)
            print ()
            print('film Telah Ditambahkan')
```
```python
if pilih == 1:
                clear()
                tempat.addfilm()
                input(">>>Tekan enter untuk kembali ke menu<<<")
                time.sleep(0.5)
                clear()
```
Fitur ini berfungsi untuk menambah data film yang dapat dibeli oleh pelanggan. Dalam menambah film, admin harus menginput data film berupa nama atau judul film, jam tayang film, studio dan harga film. 

![tambah film](https://user-images.githubusercontent.com/122262846/235283507-a930203a-fb35-4103-986e-c65547219c14.png)



#### 2. Lihat Film
```python
    def lihatdata(self):
        tabel.field_names = ['No.', 'nama film', 'jam_tayang', 'studio', 'harga']
        tabel.clear_rows()
        for idx, film in enumerate(self.films) :
            tabel.add_row([idx + 1, film._jenisfilm, film._jam_tayang, film._studio, film._harga])
        print(tabel)
```
```python
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
```
Fitur ini berfungsi untuk menampilkan data film yang tersedia. Dalam fitur lihat film ini, admin dapat melihat film apa saja yang terdata dengan jam tayang dan harga film tersebut.

![lihat film](https://user-images.githubusercontent.com/122262846/235283516-ee1562ed-ca00-4d6f-9ac6-0b2a49bada79.png)


#### 3. Cari Film
```python
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
```
```python
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
```
Fitur ini digunakan untuk mencari film, untuk mengetahui apakah film itu tersedia atau tidak tersedia. Untuk menggunakan fitur ini admin harus menginput judul film yang akan dicari dengan benar. Apabila admin sudah mengiput data yang diminta oleh program dengan benar, maka program akan memberikan output berupa letak dari film yang dicari oleh admin tersebut. Apabila data yang diinput oleh admin tidak ada dalam data film, maka program akan memberitahukan bahwa data yang dicari tidak tersedia atau tidak ada dalam data film tersebut.

![cari film](https://user-images.githubusercontent.com/122262846/235283523-f956a78d-2e0b-42e6-a020-3e15b0750931.png)


Namun, Apabila admin sudah mengiput data yang diminta oleh program dengan benar, maka program akan memberikan output berupa letak dari film yang dicari oleh admin tersebut. 

![hasil cari](https://user-images.githubusercontent.com/122262846/235283532-9bbc7035-0939-4f11-a17e-4290b8e55808.png)


#### 4. Hapus Film
```python
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
```
Fitur ini berfungsi untuk menghapus data film yang tersedia. Penggunaanya adalah dengan menginput indeks dari film yang akan dihapus dengan tepat dan benar. Apabila inputan salah, maka admin tidak dapat menggunakan fitur ini. Namun apabila inputan admin benar dan tepat, yaitu indeks film yang akan dihapus ada dalam data film, maka program ini akan menghapus data film tersebut sesuai inputan admin dan artinya program ini berhasil.

![hapus film](https://user-images.githubusercontent.com/122262846/235283543-0a56f227-e9bb-4c85-8629-de91bb4acee4.png)



#### 5. Ubah Film
```python
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
```
Fitur ubah film digunakan untuk mengubah atau meng-update data film yang ada menjadi sebuah data film yang baru, baik untuk mengubah nama atau judul film, jam tayang film, studio maupun mengubah harga film. Dalam mengubah film, admin harus menginput indeks dari film yang akan di update atau diubah dengan benar. Karena apabila inputan tidak sesuai maka fitur ini tidak dpat berfungsi. 

![update](https://user-images.githubusercontent.com/122262846/235283553-5f6b6fbf-962c-45f1-b458-861cb534b3a4.png)


Apabila inputan benar, yaitu indeks yang di-input admin tersedia, maka dapat menginput data baru daru sebuah film. Admin harus menginput kembali nama film, jam tayang serta harga film untuk mengubah dan menyimpan data film terbaru.

![ubah 2](https://user-images.githubusercontent.com/122262846/235283558-21f031a2-b5bd-438f-a5db-dfa92056c8d2.png)


#### 6. Data Film yang Masuk
```python
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
```
Fitur ini berfungsi untuk melihat history dari data film. artnya, semua film yang pernah di input atau ditambah, akan di masukkan ke history film walaupun sudah dihapus dari data film yang tersedia.

![film yg masuk](https://user-images.githubusercontent.com/122262846/235283567-c4753d24-3a21-432d-bdc9-efb2864ddae1.png)


Jadi output dari program ini adalah semua film yang pernah ditambah oleh admin, baik yang sekarang tersedia maupun yang sudah tidak tersedia karena dihapus oleh admin. Dalam program ini juga, admin dapat mengetahui jumlah dari keseluruhan data film yang pernah ditambah.

#### 7. Urutkan Film
```python
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
```
```python
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
```
Fitur ini berfungsi untuk mengurutkan data film dilihat dari nama atau judul film. Dalam fitur ini, pengurutan dapat dilakukan secara ascending dan descending.
mengurutkan film secara ascending:
```python
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
```

![ascending](https://user-images.githubusercontent.com/122262846/235283586-3b3ea47f-159e-47f5-97a7-ad8d1d5aa990.png)

Pengurutan secara ascending dilakukan dengan mengurutkan film dari abjad awal sampai abjad akhir (a-z).

mengurutkan secara descending:
```python
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
```

![descending](https://user-images.githubusercontent.com/122262846/235283593-0e367d4b-2441-46eb-9a24-dcec90f417f9.png)

Sedangkan pengurutan descending adalah kebalikan dari pengurutan ascending, yaitu mengurutkan film dari abjad akhir sampai abjad awal (z-a).

#### 8. Log Out
```python
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
```
Fitur ini digunakan untuk keluar dari akun yang saat ini sedang digunakan. Pada fitur ini, Ketika admin berhasil log out maka program akan memberitahukan waktu log out admin berupa tanggal dan jam log out.

![log out](https://user-images.githubusercontent.com/122262846/234489949-674ae054-d609-46a9-9485-2e8bc18c245d.png)

#### 9. Keluar Aplikasi
```python
elif pilih == 9:
    print(">>>Terima Kasih Telah Mengunjungi Bioskop kami<<<")
    raise SystemExit
```
Fitur keluar aplikasi digunakan untuk keluar dari program atau dapat dikatakan untuk mengakhiri semua proses program yang terjadi. Apabila admin keluar aplikasi, maka program akan memberikan output yaitu “Terima Kasih Telah Mengunjungi Bioskop kami”, maka berakhirlah proses program bioskop ini.

![KA Admin](https://user-images.githubusercontent.com/122262846/234490070-41683d59-88ea-4e10-b860-0600282d1fed.png)


### C. Menu Pelanggan
```python
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
```
Pada menu Pelanggan ini, terdapat 4 fitur diantaranya ada struk pembelian, beli film, log out, dan keluar aplikasi seperti gambar di bawah ini. untuk pengisian username akan disesuaikan dengan username yang digunakan saat login dan yang tersimpan pada database.

![menu pelanggan](https://user-images.githubusercontent.com/122262846/234257139-90b88f65-90e7-4cb1-8586-a6a1dc748bb2.png)

Fungsionalitas dari Fitur di atas antara lain:

#### 1. struk pembelian
```python
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
```
Setelah membeli Film, maka akan ada struk pembelian yang disimpan pada database. maka setiap ada pembelian, maka akan tercatat data film yang telah di beli pada database. tampilan invoice ada pada gambar di bawah ini

![invoice](https://user-images.githubusercontent.com/122262846/235283600-0e279563-404d-4473-a853-ccba8fa6f778.png)


#### 2. Beli Film
```python
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
```
```python
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
    time.sleep(2)
    clear()
```
Fitur Beli Film ini berfungsi agar kita bisa membeli film yang ada. jika memilih fitur beli film, maka akan muncul isi film yang ada. lalu pilih film dan masukkan nominal uang. jika pembayaran berhasil, maka data pembelian film akan tersimpan pada database invoice.

![beli film](https://user-images.githubusercontent.com/122262846/235283607-2ec61b63-4e98-41cc-9f04-fe3badfa45f5.png)


#### 3. Log Out
```python
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
```
Fitur log out berfungsi untuk keluar dari akun saat ini. jika memiliki 2 akun, maka kita akan bisa memasukkan akun tersebut lagi.

![log out](https://user-images.githubusercontent.com/122262846/234488589-d166a83b-df6f-467c-ab5d-91a209eaaaa6.png)

#### 4. Keluar Aplikasi
```python
elif pilih == 4:
    print(">>>Terima Kasih Telah Mengunjungi Bioskop kami<<<")
    raise SystemExit
```
Fitur Keluar Aplikasi ini fungsinya untuk memberhentikan program.

![KA Pengguna](https://user-images.githubusercontent.com/122262846/234490460-0118fa9c-8293-44e2-bc32-59402e342fbe.png)

## **Cara Penggunaan**
Program bioskop ini diawali dengan fungsi welcome dimana terdapat 4 pilihan menu yaitu admin, pelanggan, pelanggan baru atau register dan keluar aplikasi. Pada menu ini user dapat melakukan pemilihan untuk login sesuai role user yaitu admin atau pelanggan.

### Pilihan 1: Admin 
- Ketika user menginput **‘1’** artinya user **login sebagai admin**.
- Untuk login, admin harus menginput nama dan password yang telah ada
- Apabila username dan/atau password salah maka program akan memberitahukan bahwa username dan password salah.
- Namun, apabila username dan password yang diinput admin benar, maka tunggu beberapa saat maka login berhasil.
- Apabila berhasil login, maka admin akan masuk ke menu admin dengan berbagai fitur atau pilihan yang dapat dipilih oleh admin untuk melanjutkan program yang akan dijalankan oleh admin.
- Fitur yang ada pada menu admin sebanyak 9 fitur, sehingga ketika admin menginput pilihan menu lebih dari 9 maka outputnya adalah "Pilihan Hanya 1-9! Jika Ingin Kembali Ketik ya atau Jika Tidak Tekan Enter. Ingin Kembali?".
- Input **pilihan ‘1’** adalah menu **tambah film**, dimana pada fitur ini admin dapat menambah data film dengan menginput judul film, jam tayang, harga tiket dan studia dimana studio yang tersedia ada 5 studio, sehingga admin dapat memilih satu studio dari 5 studio yang dapat digunakan.
- Harga harus bertipe data int yaitu berupa angka. apabila admin menginput harga berupa str atau hutuf, maka penambahan film tidak akan berhasil dengan pemberitahuan "Mohon Memasukkan harga film Hanya Menggunakan Angka" dan mengulang ke menu pilihan admin.
- Setelah berhasil menambah data film, maka program aka membawa admin ke menu admin kembali sehingga dapat lanjut ke menu yang lainnya.
- Input **pilihan ‘2’** adalah menu **lihat film** yaitu untuk melihat daftar film yang tersedia. Ketika admin menginput ‘2’ maka program akan menampilkan data film yang tersedia seperti nama film, jam tayang, studio dah harga dari film tersebut.
- Tekan enter untuk melanjutkan program, maka program akan kembali ke menu admin.
- Input **pilihan'3'** adalah menu **cari film** dimana admin dapat mencari film dengan menginput judul film yang ingin dicari.
- Apabila judul yang diinput tidak ada dalam daftar film maka akan ada pemberitahuan program bahwa judul yang dicari tidak ada di nomor urut dan tidak ada di daftar.
- Namun apabila judul yang input ada dalam daftar film maka pemberitahuan berupa judul yang diinput terdapat dinomor urut berikut. Setelah itu kembali ke menu admin lagi.
- Input **pilihan ‘4’** adalah untuk **menghapus data film** yang tersedia. Dalam hal ini admin dapat menginput nomor film yang akan dihapus.
- Dalam menginput nomor film yang akan dihapus, admin harus menginput data bertipe int atau angka. jika tidak maka akan ada pemberitahuan "Masukan Dengan Angka".
- Apabila nomor film yang akan dihapus tidak tersedia di daftar film, maka akan ada output pemberitahuan bahwa pilihan nomor tidak ada.
- Selanjutnya program akan mengulang ke menu admin sehingga admin bisa kembali menginput ‘4’ untuk masuk ke program hapus film. 
- Apabila nomor film yang diinput ada dalam daftar data film maka ketika klik ‘Enter’ data akan terhapus sesuai dengan index inputan admin.
- Input **pilihan ‘5’** adalah menu untuk **mengupdate data film** yang ada. Dalam hal ini admin dapat mengupdate dengan menginput index film yang akan diupdate.
- Dalam menginput nomor film yang akan diubah atau diupdate, admin harus menginput data bertipe int atau angka. jika tidak maka akan ada pemberitahuan "Masukan Dengan Angka".
- Apabila admin menginput nomor film yang tidak ada dalam daftar film, maka outputnya adalah pilihan nomor tidak ada dan program akan menuntun admin ke menu admin sehingga admin dapat kembali masuk ke menu update film.
- Apabila admin menginput nomor film yang ada dalam daftar film selanjutnya admin akan menginput nama atau nama film yang beru, jam tayang, studio dan harga film.
- Inputan harga film harus berupa angka. apabila user menginput data berupa huruf, maka update tidak berhasil dan program akan memberitahu bahwa harga film yang dimasukkan harus berupa angka dan admin akan kembali ke menu admin.
- Apabila harga film yang diinput berupa angka maka update akan berhasil dan secra otomatis data dari index film yang diinput untuk diupdate akan terupdate secara otomatis.
- Input **pilihan ‘6’** adalah menu untuk masuk ke tempat **penyimpanan history film**. Pada menu ini output program adalah daftar film dan banyak film yang pernah masuk.
- Input **pilihan ‘7’** adalah menu yang digunakan untuk **melihat daftar film**. Dalam pilihan ini akan ditampilkan nama film yang ada, dimana bisa diurutkan secara ascending maupun descending.
    - Pada inputan ‘7’ terdpat **3 menu pilihan**. **Pilihan ‘1’** merupakan program untuk mengurutkan judul film secara **ascending** yaitu dari a sampai z.
    - **Pilihan ‘2’** merupakan program untuk mengurutkan judul film secara **descending** yaitu pengurutan dari huruf z sampai a.
    - **Pilihan ‘3’** akan membawa admin ke menu admin **kembali**.
- Pilihan selanjutnya pada menu admin adalah input **pilihan ‘8’**. Dimana pilihan ini digunakan untuk **logout** dari program dan kembali awal yaitu fungsi welcome untuk pemilihan role yang akan digunakan untuk log in program bioskop.
- Input **pilihan ‘9’** adalah menu **keluar aplikasi**. Ketika admin menginput 9 maka artinya admin keluar aplikasi dan outputnya adalah “terima kasih telah mengunjungi bioskop kami”.

### Pilihan 2: Pelanggan
- Ketika user menginput **‘2’** artinya user **login sebagai pelanggan**.
- Untuk login, pelanggan harus menginput nama dan password yang telah ada.
- Apabila username dan/atau password salah maka program akan memberitahukan bahwa username dan password salah.
- Namun, apabila username dan password yang diinput pelanggan benar, maka tunggu beberapa saat maka login berhasil.
- Apabila berhasil login, maka admin akan masuk ke menu pelanggan dengan berbagai fitur atau pilihan yang dapat dipilih oleh pelanggan untuk melanjutkan program yang akan dijalankan pelanggan.
- Fitur yang ada pada menu admin sebanyak 4 fitur, sehingga ketika admin menginput pilihan menu lebih dari 4 maka outputnya adalah "Pilihan Hanya 1-4! Jika Ingin Kembali Ketik ya atau Jika Tidak Tekan Enter. Ingin Kembali?".
- **Pilihan ‘1**’ adalah **struk pembelian** atau invoice. Dalam menu ini, pelanggan dapat melihat invoice dari pembelian yang kita lakukan.
- Apabila belum melakukan pembelian film, maka utuk invocenya kosong sehingga pelanggan harus terlebih dahulu membeli film.
- Apabila pelanggan sudah melakukan pembelian, maka akan ditampilan data pembelian seperti nama film, jam tayang, harga, uang pelanggan serta kembalian.
- **Pilihan ‘2’** adalah menu **beli film**. Dalam menu ini, pelanggan dapat meliht data film yang tersedia dan dapat membelinya.
- Apabila tidak ada film yang tersedia, maka outputnya adalah film tidak tersedia sehingga pelanggan akan dibawa kembali ke menu pelanggan.
- Apabila terdapat film dalam data film, maka pelanggan akan diperintah untuk menginput indeks film yang akan di beli kemudian menginput uang pelanggan.
- Apabila pelanggan menginput uang berupa huruf maka akan terjadi looping ke penginputan uang pelanggan kembali.
- Ketika uang < harga film maka akan ada pemberitahuan bahwa uang tidak cukup dan pelanggan akan dibawa kembali ke menu pelanggan.
- Namun, apabila uang >= harga film, maka pembelian akan berhasil dan data pembelian akan di insert ke data invoice. Untuk melihat struk pembelian maka dapat memilih kembali pilihan ‘1’ pada menu pelanggan. Dalam struk pembelian akan diberitahukan nama film, jam tayang, harga, uang pelanggan serta kembalian. 
- Pilihan selanjutnya pada menu pelanggan adalah input **pilihan ‘3’**. Dimana pilihan ini digunakan untuk **logout** dari program dan kembali awal yaitu fungsi welcome untuk pemilihan role yang akan digunakan untuk log in program bioskop.
- Input **pilihan ‘4’** adalah menu **keluar aplikasi**. Ketika pelanggan menginput 3 maka artinya admin keluar aplikasi dan outputnya adalah “terima kasih telah mengunjungi bioskop kami”.

### Pilihan 3: pelanggan baru
- Apabila user menginput **pilihan ‘3’** pada menu log in atau welcome, maka program akan menuntun ke **pembuatan akun baru bagi pelanggan atau register**. 
- Dalam menu regis ini, user harus menginput nama dan password yang ingin di daftarkan.
- Apabila nama yang diinput sudah ada dalam data pelanggan, maka regis tidak akan berhasil dan aka nada pemberitahuan “maaf, username sudah digunakan”, sehingga user harus menginput kembali data username dan password.
- Setelah user menginput username dan password untuk membuat akun baru untuk pelanggan, maka data yang diinput akan masuk ke database data pelanggan, sehingga dapat melakukan login dengan akun tersebut.

### Pilihan 4: Keluar aplikasi
- **Pilihan ‘4’** adalah menu **keluar aplikasi**, dimana pilihan ini adalah untuk mengakhiri semua program yang berjalan. Outputnya adalah “terimakasih sudah mengunjungi bioskop kami”.
