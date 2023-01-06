# SiBangkit
##### Aplikasi untuk Klasifikasi Penyakit dan Rekomendasi Obat

Digunakan untuk mendeteksi penyakit pada kulit atau mata penderita. Cukup dengan mengambil gambar penyakit, aplikasi ini akan memberikan informasi mengenai penyakit, pencegahan dan rekomendasi obat.

## Fitur
- #### Diabetes
    - Input beberapa fitur sesuai dataset dan akan diprediksi. Bila terdeteksi diabetes, maka akan diarahkan menuju halaman obat-obatan mengenai diabetesnya
- #### Kulit (kurap, biduran (bentol-bentol), panu, kudis)
    - Input gambar melalui photo, dapat hasil prediksi, arahkan ke halaman obat-obatan sesuai dengan penyakit kulit yang diprediksi.
- #### Mata (iritasi, bercak darah, kelopak mata bengkak)
    - Input gambar melalui photo, dapat hasil prediksi, arahkan ke halaman obat-obatan sesuai dengan penyakit mata yang diprediksi.

## Dibangun dengan
- Scikit-Learn
- Tensorflow
- Bootstrap
- Flask

## Dataset
- [Kulit](https://drive.google.com/drive/u/0/folders/1SbMWB53o0CLYfMFhnoMzFt7LkW6PqrPp)
- [Mata](https://drive.google.com/drive/u/0/folders/1fwxlYc-uD1lNk1GGOpZfykTzH2qbmczx)
- [Diabetes](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

## Install
Clone
```sh
git clone https://github.com/mdhkrmd/uprak-deployment-ds.git
```

Create Environment with Conda
```sh
conda create -n your_env_name python=3.8.5
```

Activate Environment
```sh
conda activate your_env_name
```

Buka terlebih dahulu direktori yang telah di clone sebelumnya, kemudian install library
```sh
pip install -r requirement.txt
```
