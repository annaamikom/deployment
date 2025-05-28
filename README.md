# Deployment Machine Learning
# Prediksi Bunga IRIS dengan Flask dan Deployment di PythonAnywhere

Proyek ini adalah aplikasi web sederhana untuk memprediksi jenis bunga IRIS (Setosa, Versicolour, Virginica) berdasarkan panjang dan lebar sepal serta petal. Aplikasi ini dibuat menggunakan Flask dan dideploy di PythonAnywhere.

## Fitur
- Input fitur IRIS: panjang & lebar sepal dan petal
- Prediksi jenis bunga menggunakan model Machine Learning (skikit-learn)
- Antarmuka web sederhana berbasis HTML

## Requirements
- Python 3.x
- Flask
- scikit-learn
- pickle

## Struktur Proyek
├── app.py # Aplikasi Flask utama<br>
├── model/<br>
 └──model_numpy.pkl # Model Machine Learning yang telah dilatih dan disimpan<br>
├── templates/<br>
│ └── index.html # Template HTML untuk form input dan hasil, CSS sudah include <br>
└── requirements.txt # Daftar dependensi<br>
