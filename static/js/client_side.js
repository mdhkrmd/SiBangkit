$(document).ready(function(){
  
  // -[Animasi Scroll]---------------------------
  
  $(".navbar a, footer a[href='#halamanku']").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 900, function(){
        window.location.hash = hash;
      });
    } 
  });
  
  $(window).scroll(function() {
    $(".slideanim").each(function(){
      var pos = $(this).offset().top;
      var winTop = $(window).scrollTop();
        if (pos < winTop + 600) {
          $(this).addClass("slide");
        }
    });
  });

  
  // -[Prediksi Model]---------------------------
  
  // Fungsi untuk memanggil API ketika tombol prediksi ditekan
  $("#prediksi_submit").click(function(e) {
    e.preventDefault();
	
	// Set data pengukuran bunga iris dari input pengguna
	// disesuikan sama id yang ada di html
  var input_kehamilan 	= $("#kehamilan").val(); 
	var input_glukosa 		= $("#glukosa").val(); 
	var input_darah 			= $("#darah").val(); 
	var input_bmi  				= $("#bmi").val(); 
	var input_umur  			= $("#umur").val();

	if (input_kehamilan == "" || input_glukosa == "" || input_darah == "" || input_bmi == "" || input_umur == "" ) {
        alert("Please fill out the input fields!");
        return;
      }


	// Panggil API dengan timeout 1 detik (1000 ms)
	// disesuain sama app.py
    setTimeout(function() {
	  try {
			$.ajax({
			  url  : "/diabetes",
			  type : "POST",
			  data : {
		  					"kehamilan" : input_kehamilan,
							  "glukosa"  	: input_glukosa,
							  "darah" 		: input_darah,
							  "bmi"  			: input_bmi,
							  "umur"  		: input_umur,
			         },
			  success:function(res){
				// Ambil hasil prediksi spesies dan path gambar spesies dari API
				res_data_prediksi   = res['prediksi']
				res_gambar_prediksi = res['gambar_prediksi']

				if(res_data_prediksi == "No"){
					$("#some_id0").show();
					$("#some_id1").hide();
					$("#obatDiabetes").hide();
				}
				else if (res_data_prediksi == "Yes"){
			    $("#some_id1").show();
			    $("#obatDiabetes").show();
			    $("#some_id0").hide();
				}
				else{
					$("#some_id0").hide();
					$("#some_id0").hide();
					$("#obatDiabetes").hide();
				}		

				// Tampilkan hasil prediksi ke halaman web
			    generate_prediksi(res_data_prediksi, res_gambar_prediksi); 
			  }
			});
		}
		catch(e) {
			// Jika gagal memanggil API, tampilkan error di console
			console.log("Gagal !");
			console.log(e);
		} 
    }, 1000)
    
  })
    
  // Fungsi untuk menampilkan hasil prediksi model
  function generate_prediksi(data_prediksi, image_prediksi) {
    var str="";
    // str += "<h3>Hasil Prediksi </h3>";
    str += "<img src='" + image_prediksi + "' width=\"107\" height=\"107\"></img>"
    str += "<br>"
    str += "<h4>" + data_prediksi + "</h4>";
    
    $("#hasil_prediksi").html(str);
  }
})