# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Selama lebih dari dua dekade, institusi ini telah berhasil mencetak banyak lulusan dengan reputasi yang sangat baik di berbagai bidang. Namun, seperti banyak institusi pendidikan lainnya, Jaya Jaya Institut juga menghadapi tantangan yang signifikan terkait dengan tingginya tingkat siswa yang tidak menyelesaikan pendidikannya alias dropout.

Masalah dropout ini merupakan masalah yang serius bagi institusi pendidikan, karena dropout yang tinggi dapat mempengaruhi citra institusi, mengurangi tingkat kelulusan, dan pada akhirnya berdampak pada daya tarik institusi bagi calon siswa di masa mendatang. Tingkat dropout yang tinggi juga bisa menjadi indikasi bahwa ada masalah mendasar dalam proses penerimaan siswa, pembelajaran, atau dukungan akademik yang disediakan oleh institusi.

### Permasalahan Bisnis

1. Bagaimana cara mengidentifikasi siswa-siswa yang berpotensi mengalami dropout sejak dini?
2. Faktor-faktor apa saja yang berpengaruh terhadap keputusan siswa untuk dropout?
3. Apa saja upaya yang dapat dilakukan untuk meningkatkan retensi siswa dan memastikan lebih banyak dari mereka menyelesaikan pendidikannya?

### Cakupan Proyek

- Analisis Data: Menggunakan data yang ada untuk mengidentifikasi faktor-faktor utama yang mempengaruhi dropout.
- Visualisasi & Pelaporan: Mengembangkan dashboard yang dapat digunakan untuk memonitor dan menganalisis faktor-faktor tersebut secara visual.
- Rekomendasi & Intervensi: Berdasarkan hasil analisis, memberikan rekomendasi untuk intervensi yang dapat dilakukan untuk mengurangi dropout.

### Persiapan

Sumber data: dataset yang digunakan merupakan dataset [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

* Setup conda environment:

    ```
    python -m venv proyek-institusi-pendidikan
    ```
* Install requirements:
    ```
    pip install -r requirements.txt
    ```
* Setup metabase:
    ```
    docker pull metabase/metabase:v0.46.4
    docker run -p 3000:3000 --name metabase metabase/metabase
    ```
    Akses metabase pada http://localhost:3000/setup
* Setup database (supabase):

    * Buat akun dan login https://supabase.com/dashboard/sign-in.
    * Buat new project
    * Click Connect
    * Copy URI pada database setting -> Transaction pooler
    * Kirim dataset menggunakan sqlalchemy 
    ```python
    from sqlalchemy import create_engine
 
    URL = "DATABASE_URL"
    
    engine = create_engine(URL)
    df.to_sql('institut', engine)
    ```
## Business Dashboard

Dashboard ini dibuat untuk memberikan pemahaman menyeluruh kepada institusi mengenai berbagai faktor yang memengaruhi status siswa, baik yang dropout, masih terdaftar (enrolled), maupun telah lulus (graduated). Melalui dashboard ini, tim institusi dapat:

- Melakukan Pemantauan Dini terhadap Tingkat Dropout:
    Dengan adanya visualisasi data mengenai persentase siswa yang dropout, terdaftar, dan lulus, tim dapat melihat tren dropout secara langsung. Hal ini memungkinkan institusi untuk segera merespons jika terjadi lonjakan angka siswa yang keluar
- Menganalisis Penyebab Potensial Dropout:
    Dashboard ini juga menyajikan analisis mendalam mengenai pengaruh faktor-faktor seperti prestasi akademik, keberadaan beasiswa, biaya kuliah, serta latar belakang pendidikan orang tua terhadap status siswa. Dengan informasi ini, institusi dapat mengidentifikasi risiko lebih awal dan menyesuaikan kebijakan maupun strategi intervensi secara lebih efektif.

    <img src="https://raw.githubusercontent.com/nrazizahmr/bpds_dicoding/blob/main/Submission2/images/dashboard.PNG" width="500">

## Menjalankan Sistem Machine Learning

Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

Pada proyek ini telah disediakan sebuah prototype untuk melakukan prediksi terhadap model yang sudah dibuat. Untuk menjalankan protoype secara lokal jalankan perintah berikut di terminal: streamlit run app.py

Atau buka [Streamlit](https://bdpsdicoding-proyekinstitut.streamlit.app/) untuk membuka prototype yang sudah dijalankan pada streamlit community.

<img src="https://raw.githubusercontent.com/nrazizahmr/bpds_dicoding/blob/main/Submission2/images/streamlit.PNG" width="500">

## Conclusion

Proyek ini dirancang untuk menjawab sejumlah tantangan utama yang dihadapi oleh Jaya Jaya Institut terkait tingginya angka dropout siswa. Berikut ringkasan dari temuan proyek ini:

1. Bagaimana cara mengidentifikasi siswa-siswa yang berpotensi mengalami dropout sejak dini?

    Dengan membangun model prediktif menggunakan algoritma seperti Random Forest, Jaya Jaya Institut dapat mengidentifikasi siswa-siswa yang berpotensi mengalami dropout sejak dini. Model ini mampu mendeteksi siswa berisiko dengan tingkat akurasi yang memadai berdasarkan data historis dan faktor-faktor demografis, akademik, serta ekonomi.
2. Faktor-faktor apa saja yang paling berpengaruh terhadap keputusan siswa untuk dropout?

    Analisis korelasi dan pentingnya fitur dalam model prediktif menunjukkan bahwa beberapa faktor yang paling berpengaruh terhadap keputusan siswa untuk dropout antara lain latar belakang akademik (seperti nilai dan jumlah unit yang diambil) dan kondisi ekonomi (scholarship ataupun displaced) . Misalnya, siswa yang menghadapi kesulitan akademik dalam semester pertama atau kedua cenderung memiliki risiko lebih tinggi untuk dropout.
   
   <img src="https://raw.githubusercontent.com/nrazizahmr/bpds_dicoding/blob/main/Submission2/images/correlated.PNG" width="500">
   
4. Apa saja langkah yang bisa diambil untuk meningkatkan retensi siswa dan mendorong lebih banyak siswa menyelesaikan pendidikannya?

    Berdasarkan hasil model prediktif dan analisis data, Jaya Jaya Institut dapat menerapkan sejumlah strategi, seperti memperkuat pendampingan akademik, menyesuaikan kurikulum agar beban belajar lebih seimbang, serta memberikan bantuan finansial tambahan bagi siswa yang membutuhkan. Pendekatan intervensi yang lebih awal dan berbasis data dapat secara signifikan membantu meningkatkan jumlah siswa yang berhasil menyelesaikan studi mereka.

### Rekomendasi Action Items

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

1. Penerapan Sistem Pemantauan Siswa Berbasis Data
    * Institusi dapat mulai menerapkan model prediktif yang telah dikembangkan untuk melakukan pemantauan rutin terhadap siswa. Sistem ini berfungsi sebagai alat deteksi dini bagi siswa yang memiliki potensi tinggi untuk mengalami dropout, sehingga memungkinkan pemberian intervensi seperti bimbingan akademik atau bantuan lainnya secara tepat waktu.
2. Penguatan Program Dukungan Akademik dan Psikologis
    * Dengan mengacu pada faktor-faktor risiko yang telah diidentifikasi, institusi perlu memperkuat layanan pendukung, baik dalam aspek akademik maupun psikologis. Ini mencakup perluasan akses terhadap bimbingan belajar, layanan konseling, serta fasilitas dukungan kesehatan mental bagi siswa yang menunjukkan kerentanan.
3. Evaluasi dan Penyesuaian Kurikulum
    * Melakukan peninjauan terhadap program studi dengan tingkat dropout yang tinggi menjadi langkah penting. Penyesuaian bisa dilakukan pada kurikulum maupun metode pengajaran, misalnya dengan meningkatkan fleksibilitas jadwal perkuliahan atau menyediakan materi pembelajaran tambahan guna mengurangi beban akademik yang dirasakan oleh siswa.

Username: root@mail.com
Password: root123
