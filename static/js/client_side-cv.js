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
	
	// Get File Gambar yg telah diupload pengguna
    var file_data = $('#input_gambar').prop('files')[0];   
    var pics_data = new FormData();                  
    pics_data.append('file', file_data);

	// Panggil API dengan timeout 1 detik (1000 ms)
    setTimeout(function() {
	  try {
			$.ajax({
				url         : "/kulit",
				type        : "POST",
				data        : pics_data,
				processData : false,
				contentType : false,
				success     : function(res){
					// Ambil hasil prediksi dan path gambar yang diprediksi dari API
					res_data_prediksi   = res['prediksi']
					res_gambar_prediksi = res['gambar_prediksi']

				if(res_data_prediksi == "Biduran"){
					$("#penjelasan_biduran").show();
					$("#penjelasan_kudis").hide();
					$("#penjelasan_kurap").hide();
					$("#penjelasan_panu").hide();
					$("#penjelasan_bisul").hide();

					$("#some_id0").show();
					$("#some_id1").hide();
					$("#some_id2").hide();
					$("#some_id3").hide();
					$("#some_id4").hide();
					$("#some_id5").hide();

					$("#obatBiduran").show();
					$("#obatKudis").hide();
					$("#obatKurap").hide();
					$("#obatPanu").hide();
					$("#obatBisul").hide();
				}
				else if (res_data_prediksi == "Bisul"){
			   	$("#penjelasan_biduran").hide();
					$("#penjelasan_kudis").hide();
					$("#penjelasan_kurap").hide();
					$("#penjelasan_panu").hide();
					$("#penjelasan_bisul").show();

			   	$("#some_id0").hide();
					$("#some_id1").hide();
					$("#some_id2").hide();
					$("#some_id3").hide();
					$("#some_id4").show();
					$("#some_id5").hide();

					$("#obatBiduran").hide();
					$("#obatKudis").hide();
					$("#obatKurap").hide();
					$("#obatPanu").hide();
					$("#obatBisul").show();
				}
				else if (res_data_prediksi == "Kudis"){
			   	$("#penjelasan_biduran").hide();
					$("#penjelasan_kudis").show();
					$("#penjelasan_kurap").hide();
					$("#penjelasan_panu").hide();
					$("#penjelasan_bisul").hide();

			   	$("#some_id0").hide();
					$("#some_id1").show();
					$("#some_id2").hide();
					$("#some_id3").hide();
					$("#some_id4").hide();
					$("#some_id5").hide();

					$("#obatBiduran").hide();
					$("#obatKudis").show();
					$("#obatKurap").hide();
					$("#obatPanu").hide();
					$("#obatBisul").hide();
				}
				else if (res_data_prediksi == "Kurap"){
			   	$("#penjelasan_biduran").hide();
					$("#penjelasan_kudis").hide();
					$("#penjelasan_kurap").show();
					$("#penjelasan_panu").hide();
					$("#penjelasan_bisul").hide();

			   	$("#some_id0").hide();
					$("#some_id1").hide();
					$("#some_id2").show();
					$("#some_id3").hide();
					$("#some_id4").hide();
					$("#some_id5").hide();

					$("#obatBiduran").hide();
					$("#obatKudis").hide();
					$("#obatKurap").show();
					$("#obatPanu").hide();
					$("#obatBisul").hide();
				}
				else if (res_data_prediksi == "Panu"){
			   	$("#penjelasan_biduran").hide();
					$("#penjelasan_kudis").hide();
					$("#penjelasan_kurap").hide();
					$("#penjelasan_panu").show();
					$("#penjelasan_bisul").hide();

			   	$("#some_id0").hide();
					$("#some_id1").hide();
					$("#some_id2").hide();
					$("#some_id3").show();
					$("#some_id4").hide();
					$("#some_id5").hide();

					$("#obatBiduran").hide();
					$("#obatKudis").hide();
					$("#obatKurap").hide();
					$("#obatPanu").show();
					$("#obatBisul").hide();
				}
				else{
					$("#penjelasan_biduran").hide();
					$("#penjelasan_kudis").hide();
					$("#penjelasan_kurap").hide();
					$("#penjelasan_panu").hide();
					$("#penjelasan_bisul").hide();

					$("#some_id0").hide();
					$("#some_id1").hide();
					$("#some_id2").hide();
					$("#some_id3").hide();
					$("#some_id4").hide();
					$("#some_id5").show();

					$("#obatBiduran").hide();
					$("#obatKudis").hide();
					$("#obatKurap").hide();
					$("#obatPanu").hide();
					$("#obatBisul").hide();
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
	
	if(image_prediksi == "(none)") {
		// str += "<h3>Hasil Prediksi </h3>";
		str += "<br>";
		str += "<h4>Silahkan masukkan file gambar (.jpg)</h4>";
	}
	else {
		// str += "<h3>Hasil Prediksi </h3>";
		str += "<br>";
		str += "<img src='" + image_prediksi + "' width=\"200\"></img>"
		str += "<h3>" + data_prediksi + "</h3>";
	}
	$("#hasil_prediksi").html(str);
  }  
})
  
