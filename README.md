# Bioskop

## Nama Anggota
- Amalia Kartika Sari (2209116013)
- Angelia Cristin (2209116015)
- Bertha Joy Rodo Saragi (2209116047)

## Deskripsi Program
Bioskop merupakan wadah bagi masyarakat untuk menikmati pertunjukkan film, dimana penonton mencurahkan segenap perhatiannya dan perasaannya kepada gambar hidup yang disaksikan. Film ditampilkan pada sebuah layar lebar dengan efek suara yang menjadi salah satu daya tarik masyarakat untuk menyaksikan sebuah film di tempat ini. film yang ditampilkan dalam bioskop juga bermacam-macam baik untuk anak-anak, remaja dan dewasa.

program ini merupakan program bioskop dimana ada login untuk admin dan user atau pelanggan dengan masing-masing fitur yang ada didalamnya yang fungsi utamanya adalah untuk memudahkan admin untuk menambah, mengupdate, menghapus dan melihat data film yang ada, juga memudahkan pelanggan dalam melakukan pembelian film bahkan pengeditan akun pelanggan tersebut.

## Struktur Program 
Struktur Program yang kami gunakan pada project yang berjudul “Bioskop” kali ini adalah:
1.	Pretty Table

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
2. Singly Linked list

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

3. Sort with Quick Sort

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

4. Search with Fibonacci search

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

5. Struktur data dengan Queue

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

6. List untuk menyimpan data

kami juga menggunakan list penyimpanan biasa yang dimana dapat menyimpan data yang ingin di tambah, ubah, edit, bahkan menghapus data yang ada di list tersebut

``` python
tempat = penyimpanan()         
film = tambah()          
queue = Queue()           
link = LinkedList()                          
jb = ["0"]             
kusus_jenis = []              
kusus_jam_tayang = []             
kusus_harga = []             
kusus_nama_user = []
```
7. Database Menggunakan Mysql

Kami menggunakan Database Mysql karena sebelumnya kami telah mempelajari database tersebut dan juga karna database ini lebih simple dan mudah untuk di terapkan dalam Big project kami.

``` python
import mysql.connector

mydb = mysql.connector.connect(
host="db4free.net ",
user="kelompok_1",
password="kelompoksatu",
database="bioskop_1"
)

sql = "INSERT INTO invoice (nama_film, jam_tayang, harga, uang, kembalian) VALUES (%s,%s,%s,%s,%s)"
val = (nama_film, jam_tayang, harga, uang, kembalian)
mycursor = mydb.cursor()
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

```

