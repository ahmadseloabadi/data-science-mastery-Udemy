# ====================================
# REGRESI LINIER - PENJELASAN & IMPLEMENTASI
# ====================================

# 1. Regresi linier adalah metode dalam aljabar linier yang bertujuan 
#    untuk menyesuaikan garis atau bidang hiper agar kesalahan 
#    antara nilai prediksi dan nilai aktual diminimalkan.
#    Model matematikanya adalah:
#    y_cap = X * theta
#    - X adalah matriks fitur (termasuk bias)
#    - theta adalah parameter (bobot dan bias)
#    - y_cap adalah nilai prediksi.

# 2. Dalam kalkulus, optimasi theta melibatkan meminimalkan fungsi kerugian.
#    Fungsi kerugian (Loss Function) didefinisikan sebagai:
#    J(theta) = (1 / 2m) * Σ (y_cap_i - y_i)^2
#    Gradien dari J(theta) adalah:
#    ∇J(theta) = (1 / m) * X^T * (X * theta - y)

# 3. Statistik:
#    Untuk mengevaluasi performa model, digunakan metrik seperti:
#    - Mean Squared Error (MSE):
#      MSE = (1 / m) * Σ (y_cap_i - y_i)^2
#    - R-squared (R^2):
#      R^2 = 1 - (SS_res / SS_tot)
#      Mengukur seberapa baik garis regresi menjelaskan variansi dalam data.

# ====================================
# IMPLEMENTASI DENGAN GRADIENT DESCENT
# ====================================

# 1. Penurunan gradien (Gradient Descent) digunakan untuk optimasi parameter.
#    Rumus iteratif untuk memperbarui theta adalah:
#    theta = theta - alpha * ∇J(theta)
#    - alpha adalah learning rate, mengontrol ukuran langkah optimasi.

# 2. Langkah-langkah utama:
#    a. Inisialisasi parameter theta secara acak.
#    b. Hitung gradien: ∇J(theta).
#    c. Perbarui parameter theta menggunakan aturan penurunan gradien.

# ====================================
# METRIK EVALUASI MODEL
# ====================================

# 1. Mean Squared Error (MSE):
#    - Mengukur rata-rata kesalahan kuadrat.
#    - MSE = (1 / m) * Σ (y_cap_i - y_i)^2

# 2. R-squared (R^2):
#    - Mengukur seberapa baik garis regresi menjelaskan variansi data.
#    - R^2 = 1 - (SS_res / SS_tot)
#    - SS_res: Jumlah kuadrat sisa (residual sum of squares).
#    - SS_tot: Jumlah kuadrat total (total sum of squares).

# ====================================
# TUGAS HANDS-ON
# ====================================

# Tugas 1: Implementasi rumus matematika regresi linier dari awal.
# Tugas 2: Menggunakan penurunan gradien untuk optimasi parameter model.
# Tugas 3: Menghitung metrik evaluasi (MSE dan R^2).

