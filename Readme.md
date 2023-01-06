<p align="center">
<img width="100" src="https://user-images.githubusercontent.com/81756856/210927351-7f000fa7-70b1-4557-bc59-7677d9d3161f.png" alt="SiBangkit">
</p>


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
    
## Dokumentasi
<p align="center">
<img width="500" src="https://user-images.githubusercontent.com/81756856/210928207-5dd27701-f012-40a6-8da0-dcd4c2463aae.png" alt="SiBangkit">
<img width="500" src="https://user-images.githubusercontent.com/81756856/210928204-3173d69e-a35f-45a3-8b10-4d2b387007a8.png" alt="SiBangkit">
<img width="500" src="https://user-images.githubusercontent.com/81756856/210928203-20e7f2b5-70a0-491c-821a-f618b89a6771.png" alt="SiBangkit">
<img width="500" src="https://user-images.githubusercontent.com/81756856/210928198-1bb18089-c00f-4ae2-9fdd-f386d206b4ae.png" alt="SiBangkit">
<img width="500" src="https://user-images.githubusercontent.com/81756856/210928195-dec06a43-3a04-4dcb-b40c-e83866caf918.png" alt="SiBangkit">
<img width="500" src="https://user-images.githubusercontent.com/81756856/210928194-6f075692-573d-4d9c-865e-b87e335e96c2.png" alt="SiBangkit">
<img width="500" src="https://user-images.githubusercontent.com/81756856/210928193-92cab2da-b6c7-449e-9390-73fe07ca443d.png" alt="SiBangkit">
<img width="500" src="https://user-images.githubusercontent.com/81756856/210928188-4cc8e475-a8a3-44be-9908-1a7e3d8fc5cb.png" alt="SiBangkit">
</p>

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
