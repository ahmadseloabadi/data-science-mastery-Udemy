from statistics import mode 

print('\n ---basic statistics---\n')
data = [10,20,30,40,50]

mean = sum(data)/len(data)

print('\n initial data:',data)
print('\n mean of data:',mean)

sorted_data = sorted(data)
median = sorted_data[len(data) // 2] if len(data) % 2 != 0 else \
    (sorted_data[len(data) // 2 - 1] + sorted_data[len(data) // 2]) / 2

print('\n median of data:',median)

print('\n mode of data:',mode(data))

variance = sum((x-mean) ** 2 for x in data) / len(data)

print('\n varience of data:',variance)

std_dev = variance ** 0.5

print('\n standard deviation of data:',std_dev)

# hypothesis testing

# Pengujian Hipotesis
# Pengujian hipotesis adalah metode statistik untuk menentukan apakah suatu hasil signifikan atau terjadi secara kebetulan.
# Langkah-langkah pengujian hipotesis:
# 1. Formulasikan hipotesis
#    - Hipotesis nol (H0): Tidak ada efek atau perbedaan yang tercipta.
#    - Hipotesis alternatif (Ha): Ada efek atau perbedaan yang tercipta.
# 2. Hitung statistik uji yang mengukur perbedaan.
# 3. Tentukan nilai p, yaitu probabilitas pengamatan data yang ekstrem seperti statistik uji di bawah hipotesis nol.
# 4. Interpretasikan hasil:
#    - Jika nilai p < alpha (tingkat signifikansi), kita menolak hipotesis nol.
#    - Jika nilai p >= alpha, kita gagal menolak hipotesis nol.

# Contoh pengujian hipotesis: 
# Membandingkan rata-rata nilai tes antara dua kelompok menggunakan uji t.

# Confidence Intervals dan Signifikansi Statistik

# Interval Kepercayaan (Confidence Interval - CI):
# Interval kepercayaan adalah rentang nilai yang diharapkan mencakup parameter populasi yang sebenarnya.
# Rumus untuk menghitung CI adalah:
# CI = x̄ ± z * (s / √n)
# Dimana:
# x̄ : Rata-rata sampel (sample mean)
# z  : Skor Z (Z-score), terkait dengan tingkat kepercayaan
# s  : Standar deviasi (standard deviation)
# n  : Ukuran sampel (sample size)

# Skor Z (Z-Score):
# Skor Z digunakan untuk menentukan berapa standar deviasi sebuah data dari rata-rata.

# Interpretasi:
# Contoh untuk tingkat kepercayaan 95%, nilai Z-score yang umum digunakan adalah 1.96.

# Catatan:
# Formula ini digunakan untuk memperkirakan parameter populasi berdasarkan data sampel.
print('\nConfidence Intervals dan Signifikansi Statistik\n')
import scipy.stats as stats

data = [10, 20, 30, 40, 50]
mean =sum(data) / len(data)

variance = sum((x-mean) ** 2 for x in data) / len(data)
std_dev = variance ** 0.5

sample_mean = mean
z_score = 1.96


ci = (sample_mean - z_score * (std_dev / len(data) ** 0.5),
        sample_mean + z_score * (std_dev/len (data) ** 0.5))

print('\n 95% confidence intervals:',ci)

# exercise
print('\n ----exercise---\n')
import numpy as np
# Dataset
data = [10, 20, 30, 40, 50]
# Calculate Stats
mean = np.mean(data)
variance = np.var(data)
std_dev = np.std(data)
print("\nMean: ", mean)
print("\nVariance: ", variance)
print("\nStandard Deviation: ", std_dev)

# perform a T-test

import scipy.stats as ttest_ind

# sample dataset

group1 = [2.1, 2.5, 2.8, 3.0, 3.2]
group2 = [1.8, 2.0, 2.4, 2.7, 2.9]
# Perform t-test
t_stat, p_value = ttest_ind(group1, group2)

print(' T-statistics : ', t_stat)
print(' P_value : ', p_value)

# interpretation

alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: significant difference")
else:
    print("Failt to reject the null hypothesis: no significant difference")

    