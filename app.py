'''
	Contoh Deloyment untuk Domain Data Science (DS)
	Orbit Future Academy - AI Mastery - KM Batch 3
	Tim Deployment
	2022
'''

# =[Modules dan Packages]========================

from flask import Flask,render_template,request,jsonify
from flask_mysqldb import MySQL,MySQLdb
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from joblib import load
from werkzeug.utils import secure_filename
import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, \
Flatten, Dense, Activation, Dropout,LeakyReLU
from PIL import Image, ImageTk
from fungsi_cv import make_model
from fungsi_cv_mata import make_model2
from io import BytesIO

# =[Variabel Global]=============================

app   	= Flask(__name__, static_url_path='/static',template_folder='template')
app2   	= Flask(__name__, static_url_path='/static',template_folder='template')

app.config['MAX_CONTENT_LENGTH'] = 4032 * 4032
app.config['UPLOAD_EXTENSIONS']  = ['.jpg','.JPG', '.jpeg', '.png']
app.config['UPLOAD_PATH']        = './static/images/uploads/'

model2 = make_model()
model2.load_weights("kulit-B4.h5")

model3 = make_model2()
model3.load_weights("mata-b4.h5")


# =[DB]==========================================
app.secret_key = "caircocoders-ednalan"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyek_orbit'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# =[Routing]=====================================

# [Routing untuk Halaman Utama atau Home]	
@app.route("/")
def beranda():
    return render_template('index.html')

# [Routing untuk Diabetes]	
@app.route('/diabetes', methods=['GET', 'POST'])
def diabetes():
	# # Nilai default untuk variabel input atau features (X) ke model
    model = None
    model = load('model_77_new_edit.pkl')
    input_kehamilan = 0
    input_glukosa = 0
    input_darah = 0
    input_bmi = 0
    input_umur = 0
    # return render_template('diabetes.html')
    
    if request.method == 'POST':
        # Set nilai untuk variabel input atau features (X) berdasarkan input dari pengguna
        # float(request.form['harapan']) -> harapan, pengeluaran samain di client_side
        input_kehamilan = float(request.form['kehamilan'])
        input_glukosa = float(request.form['glukosa'])
        input_darah = float(request.form['darah'])
        input_bmi = float(request.form['bmi'])
        input_umur = float(request.form['umur'])
		
		# =[Routing]=====================================	
		
		# Prediksi kelas atau spesies bunga iris berdasarkan data pengukuran yg diberikan pengguna
		# Sesuai dataset
        df_test = pd.DataFrame(data={
			"Pregnancies" 	: 	[input_kehamilan],
			"Glucose" 		: 	[input_glukosa],
			"BloodPressure" : 	[input_darah],
			"BMI"  			: 	[input_bmi],
			"Age"  			: 	[input_umur]
		})

        hasil_prediksi = model.predict(df_test[0:1])[0]

		# Set Path untuk gambar hasil prediksi
        if hasil_prediksi == 'No':
            gambar_prediksi = '/static/images/Health.png'

        elif hasil_prediksi == 'Yes':
            gambar_prediksi = '/static/images/diabetes-2.png'

        else:
            gambar_prediksi = '/static/images/emoticon.png'
		
		# Return hasil prediksi dengan format JSON
        return jsonify({
			"prediksi": hasil_prediksi,
			"gambar_prediksi" : gambar_prediksi
		})

        # return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('diabetes.html')

# [Routing untuk Kulit]
@app.route('/kulit', methods=['GET', 'POST'])
def kulit():
    NUM_CLASSES = 5
    cifar10_classes = ['Biduran', 'Bisul', 'Kudis', 'Kurap', 'Panu']
    
    # Set nilai default untuk hasil prediksi dan gambar yang diprediksi
    hasil_prediksi  = '(none)'
    gambar_prediksi = '(none)'

    if request.method == 'POST':

		# Get File Gambar yg telah diupload pengguna
	    uploaded_file = request.files['file']
	    filename      = secure_filename(uploaded_file.filename)
		
		# Periksa apakah ada file yg dipilih untuk diupload
	    if filename != '':
		
			# Set/mendapatkan extension dan path dari file yg diupload
	        file_ext        = os.path.splitext(filename)[1]
	        gambar_prediksi = '/static/images/uploads/' + filename
			
			# Periksa apakah extension file yg diupload sesuai (jpg)
	        if file_ext in app.config['UPLOAD_EXTENSIONS']:
				
				# Simpan Gambar
	            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
				
				# Memuat Gambar
	            test_image = Image.open('.' + gambar_prediksi)
				
				# Mengubah Ukuran Gambar
	            test_image_resized = test_image.resize((300,300))
				
				# Konversi Gambar ke Array
	            image_array        = np.array(test_image_resized)
	            test_image_x       = (image_array / 255) - 0.5
	            test_image_x       = np.array([image_array])
				
				# Prediksi Gambar
	            y_pred_test_single         = model2.predict(test_image_x)
	            y_pred_test_classes_single = np.argmax(y_pred_test_single, axis=1)
				
	            hasil_prediksi = cifar10_classes[y_pred_test_classes_single[0]]
				
				# Return hasil prediksi dengan format JSON
	            return jsonify({
					"prediksi": hasil_prediksi,
					"gambar_prediksi" : gambar_prediksi
				})
	        else:
				# Return hasil prediksi dengan format JSON
	            gambar_prediksi = '(none)'
	            return jsonify({
					"prediksi": hasil_prediksi,
					"gambar_prediksi" : gambar_prediksi
				})

    return render_template('kulit.html')

# [Routing untuk Mata]
@app.route('/mata', methods=['GET', 'POST'])
def mata():
    NUM_CLASSES = 4
    cifar10_classes = ['Bintitan', 'Konjungtivitis', 'Subconjunctival-Bleeding']
    
    # Set nilai default untuk hasil prediksi dan gambar yang diprediksi
    hasil_prediksi  = '(none)'
    gambar_prediksi = '(none)'

    if request.method == 'POST':

		# Get File Gambar yg telah diupload pengguna
	    uploaded_file = request.files['file']
	    filename      = secure_filename(uploaded_file.filename)
		
		# Periksa apakah ada file yg dipilih untuk diupload
	    if filename != '':
		
			# Set/mendapatkan extension dan path dari file yg diupload
	        file_ext        = os.path.splitext(filename)[1]
	        gambar_prediksi = '/static/images/uploads/' + filename
			
			# Periksa apakah extension file yg diupload sesuai (jpg)
	        if file_ext in app.config['UPLOAD_EXTENSIONS']:
				
				# Simpan Gambar
	            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
				
				# Memuat Gambar
	            test_image = Image.open('.' + gambar_prediksi)
				
				# Mengubah Ukuran Gambar
	            test_image_resized = test_image.resize((300,300))
				
				# Konversi Gambar ke Array
	            image_array        = np.array(test_image_resized)
	            test_image_x       = (image_array / 255) - 0.5
	            test_image_x       = np.array([image_array])
				
				# Prediksi Gambar
	            y_pred_test_single         = model3.predict(test_image_x)
	            y_pred_test_classes_single = np.argmax(y_pred_test_single, axis=1)
				
	            hasil_prediksi = cifar10_classes[y_pred_test_classes_single[0]]
				
				# Return hasil prediksi dengan format JSON
	            return jsonify({
					"prediksi": hasil_prediksi,
					"gambar_prediksi" : gambar_prediksi
				})
	        else:
				# Return hasil prediksi dengan format JSON
	            gambar_prediksi = '(none)'
	            return jsonify({
					"prediksi": hasil_prediksi,
					"gambar_prediksi" : gambar_prediksi
				})
    
    
    return render_template('mata.html')

# [Routing untuk About]
@app.route('/about')
def about():
    return render_template('about.html')

# [Routing untuk BMI]
@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    return render_template('bmi.html')

# [Routing untuk BMI]
@app.route('/cariObat', methods=['GET', 'POST'])
def cariObat():
    return render_template('cariObat.html')

@app.route("/ajaxlivesearch",methods=["POST","GET"])
def ajaxlivesearch():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur2 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
    if request.method == 'POST':
        search_word = request.form['query']
        print(search_word)
        if search_word == '':
            query = "SELECT * from employee ORDER BY id"
            cur.execute(query)
            employee = cur.fetchall()
        else:    
            query = "SELECT * from obatan WHERE nama_obat LIKE '%{}%' OR indikasi_umum LIKE '%{}%' OR metadata LIKE '%{}%' ORDER BY rating DESC LIMIT 20".format(search_word,search_word,search_word)
            cur.execute(query)
            numrows = int(cur.rowcount)
            employee = cur.fetchall()

            # query2 = "SELECT foto_obat from obatan WHERE nama_obat LIKE '%{}%' OR indikasi_umum LIKE '%{}%' OR metadata LIKE '%{}%' ORDER BY rating DESC LIMIT 20".format(search_word,search_word,search_word)
            # cur2.execute(query2)
            # numrows2 = int(cur2.rowcount)
            # ambilGambar = cur2.fetchall()
            # gmbr = ambilGambar[0][0]
            # img_byte = BytesIO(gmbr)
            # gambar = ImageTk.PhotoImage(Image.open(img_byte))
            # Label(root,image=gambar).pack()
            # root.image = gambar # Keep a reference 

            print(numrows)
    return jsonify({'htmlresponse': render_template('response-obat.html', employee=employee, numrows=numrows)})

# =[Main]========================================

if __name__ == '__main__':
	# Run Flask di localhost 
	app.run(host="localhost", port=5000, debug=True)
