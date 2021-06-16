# -*- coding: utf-8 -*-
"""Tugas Besar Fuzzy Logic

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lwKHvU2SjwXK5iE_W_8wxskQ8Zmx02_D
"""

import pandas as pd
import numpy as np

data_pemohon = pd.read_excel('masukan.xlsx')

data_pemohon

def fuzzification_pinjaman(pinjaman):
  if pinjaman >= 25:
    Banyak = 1
  elif pinjaman >= 10 and pinjaman < 25:
    Banyak = (pinjaman - 10) / (25 - 10)
  else:
    Banyak = 0

  if pinjaman < 2 and pinjaman > 0:
    Sedikit = 1
  elif pinjaman >= 2 and pinjaman < 4:
    Sedikit = (pinjaman - 2) / (4 - 2)
  else:
    Sedikit = 0

  if pinjaman > 5 and pinjaman <= 8:
    Sedang = 1
  elif pinjaman >= 2.5 and pinjaman < 15:
    Sedang = (pinjaman - 2.5) / (15 - 2.5)
  else:
    Sedang = 0
  list1 = [Banyak, Sedang, Sedikit]
  return list1

hasil_fuzzy_pinjaman = []

for i in range (100):
  hasil_fuzzy_pinjaman.append(fuzzification_pinjaman(data_pemohon["pinjaman"][i]))

print(hasil_fuzzy_pinjaman)

array = [6]

array[0] = 'a'
print(array)

def fuzzification_pemasukan(pemasukan):
  if pemasukan >= 30:
    Besar = 1
  elif pemasukan >= 18 and pemasukan < 30:
    Besar = (pemasukan - 18) / (30 - 18)
  else:
    Besar = 0

  if pemasukan <= 1.5 and pemasukan > 0:
    Kecil = 1
  elif pemasukan >= 2 and pemasukan < 6:
    Kecil = (pemasukan - 2) / (4 - 2)
  else:
    Kecil = 0

  if pemasukan > 8 and pemasukan <= 15:
    Menengah = 1
  elif pemasukan >= 3 and pemasukan < 22:
    Menengah = (pemasukan - 2.5) / (22 - 3)
  else:
    Menengah = 0
  list2 = [Besar, Menengah, Kecil]
  return list2 

hasil_fuzzy_pemasukan = []

for q in range (100):
  hasil_fuzzy_pemasukan.append(fuzzification_pemasukan(data_pemohon["pemasukan"][q]))

print(hasil_fuzzy_pemasukan)

arr = [1,5,7,8,3,12,41,9,10,11]
for x in range (10):
   arr[x] = x
print(arr)

var1 = float(hasil_fuzzy_pinjaman[0][1]) 
 var2 = float(hasil_fuzzy_pemasukan[0][1])
 #min((hasil_fuzzy_pinjaman[0][1]),(hasil_fuzzy_pemasukan[0][1]))

print(min(var1,var2))

hasil_perbandingan = hasil_fuzzy_pemasukan
def inference(hasil_fuzzy_pinjaman, hasil_fuzzy_pemasukan):
    hasil_fuzzy_pemasukan
    hasil_fuzzy_pinjaman
    

    for i in range(len(hasil_fuzzy_pinjaman)):
      for j in range(len(hasil_fuzzy_pinjaman[i])):
        hasil_perbandingan[i][j] = min(hasil_fuzzy_pinjaman[i][i],hasil_fuzzy_pemasukan[i][j])
    return hasil_perbandingan

hasil_perbandingan
print(hasil_perbandingan)

batas_Accepted = 100
batas_Considered = 50
batas_Rejected = 30

hasil_perbandingan

score = []
def defuzifikasi(hasil_perbandingan):
  for i in range(len(hasil_perbandingan)):
    score.append(((hasil_perbandingan[i][0] * 100) + (hasil_perbandingan[i][1] * 50) + (hasil_perbandingan[i][2] * 30)) / (hasil_perbandingan[i][0] + hasil_perbandingan[i][1] + hasil_perbandingan[i][2])) 
 
 

defuzifikasi(hasil_perbandingan)
#print(hasil_perbandingan[0][0])
#print(hasil_perbandingan[0][1])
#print(hasil_perbandingan[0][2])
print(score)

score
print(score)

data_pemohon['status'] = score
data_pemohon

dataExcel = data_pemohon.copy()
dataExcel.sort_values('status', ascending=False, inplace=True)
dataExcel

dataExcel = dataExcel[:10]
dataExcel['id'].to_excel('luaran.xls', index=False)

