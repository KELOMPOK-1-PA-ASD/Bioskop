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
