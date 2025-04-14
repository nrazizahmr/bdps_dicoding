# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan perusahaan multinasional yang berdiri sejak tahun 2000, memiliki lebih dari 1000 karyawan yang tersebar di seluruh negeri. Namun mereka masih menghadapi tantangan dalam mengelola karyawannya. Salah satu dampak utama dari tantangan ini adalah tingginya *attrition rate*, yaitu rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan, yang mencapai lebih dari 10%. Tingginya *attrition rate* ini mengindikasikan adanya masalah dalam mempertahankan karyawan, yang dapat berdampak negatif pada produktivitas, biaya rekrutmen, dan stabilitas operasional perusahaan.

### Permasalahan Bisnis

1. Seberapa tinggi tingkat attrition di perusahaan ini?
2. Faktor apa saja yang mempengaruhi keputusan karyawan untuk meninggalkan perusahaan?
3. Apakah ada perbedaan tingkat attrition berdasarkan role atau departemen tertentu di perusahaan?
4. Bagaimana pengaruh overtime terhadap keputusan karyawan untuk keluar dari perusahaan?

### Cakupan Proyek

Analisis Data: Menganalisis data karyawan yang tersedia untuk menentukan faktor-faktor utama yang berkontribusi terhadap tingkat attrition
Visualisasi & Pelaporan: Mengembangkan dashboard bisnis yang dapat digunakan oleh manajer HR untuk memonitor dan menganalisis faktor-faktor tersebut secara visual.
Rekomendasi & Intervensi: Berdasarkan hasil analisis, memberikan rekomendasi untuk intervensi yang dapat dilakukan untuk mengurangi attrition rate dan meningkatkan kepuasan karyawan.

### Persiapan

Sumber data: dataset yang digunakan merupakan dataset [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

* Setup conda environment:

    ```
    python -m venv proyek-human-resources
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
    df.to_sql('orders', engine)
    ```
## Business Dashboard

Dashboard ini dibuat untuk membantu tim HR mendapatkan pemahaman menyeluruh terkait faktor-faktor yang memengaruhi keputusan karyawan untuk keluar dari perusahaan. Melalui dashboard ini, tim HR dapat:

- Menemukan divisi atau departemen dengan tingkat attrition yang tinggi.
- Menganalisis berbagai aspek seperti lembur, tingkat kepuasan kerja, serta karakteristik demografis yang berpotensi berpengaruh terhadap attrition.
- Mengambil langkah-langkah preventif guna meningkatkan retensi karyawan dan menekan biaya akibat pergantian tenaga kerja.

    <img src="https://raw.githubusercontent.com/nrazizahmr/bdps_dicoding/Submission1/images/dashboard.PNG">

## Conclusion

1. Seberapa tinggi tingkat attrition di perusahaan ini?
    * Jawaban: Tingkat attrition di perusahaan ini adalah sekitar 17%. Ini berarti bahwa satu dari enam karyawan meninggalkan perusahaan dalam jangka waktu tertentu, menunjukkan bahwa tingkat keluar karyawan cukup signifikan.

    <img src="https://raw.githubusercontent.com/nrazizahmr/bdps_dicoding/Submission1/images/attrition.PNG" width="500">

2. Faktor-faktor apa saja yang mempengaruhi keputusan karyawan untuk meninggalkan perusahaan?
    * Jawaban: Beberapa faktor utama yang mempengaruhi keputusan karyawan untuk meninggalkan perusahaan meliputi:
        * Overtime: Karyawan yang sering bekerja lembur cenderung memiliki kemungkinan lebih tinggi untuk keluar dari perusahaan.
        * Status Perkawinan: Karyawan yang berstatus Single cenderung memiliki tingkat attrition yang lebih tinggi, kemungkinan karena mereka lebih fleksibel untuk berpindah dan lebih terbuka terhadap peluang karier baru.

    <img src="https://raw.githubusercontent.com/nrazizahmr/bdps_dicoding/Submission1/images/factorattrition.png" width="500">

3. Apakah ada perbedaan tingkat attrition berdasarkan role atau departemen tertentu di perusahaan?
    * Jawaban: Ya, terdapat perbedaan tingkat attrition berdasarkan role dan departemen. Misalnya, role seperti Sales Representative dan departemen seperti Sales menunjukkan tingkat attrition yang lebih tinggi dibandingkan dengan posisi atau departemen lainnya. Ini mengindikasikan bahwa faktor seperti beban kerja, tingkat stres, dan kemungkinan struktur kompensasi di area tersebut dapat memengaruhi keputusan karyawan untuk keluar dari perusahaan.

    <img src="https://raw.githubusercontent.com/nrazizahmr/bdps_dicoding/Submission1/images/attritionby_jobrole.PNG" width="500">
    <img src="https://raw.githubusercontent.com/nrazizahmr/bdps_dicoding/Submission1/images/attritionby_department.PNG" width="500">

4. Bagaimana pengaruh overtime terhadap keputusan karyawan untuk keluar dari perusahaan?
    * Jawaban: Lembur memiliki pengaruh signifikan terhadap keputusan karyawan untuk meninggalkan perusahaan. Data menunjukkan bahwa karyawan yang sering bekerja lembur (overtime) memiliki tingkat attrition yang lebih tinggi. Ini mungkin terkait dengan tingkat stres yang lebih tinggi dan ketidakseimbangan antara kehidupan kerja dan pribadi.
    
    <img src="https://raw.githubusercontent.com/nrazizahmr/bdps_dicoding/Submission1/images/attritionby_overtime.PNG" width="500">

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

1. Pengelolaan Beban Kerja dan Lembur:
    * Lakukan peninjauan terhadap beban kerja karyawan dan sesuaikan jika diperlukan guna mengurangi lembur yang berlebihan. Hal ini penting untuk menjaga keseimbangan antara pekerjaan dan kehidupan pribadi, serta menurunkan risiko attrition.
2. Peningkatan Kepuasan dan Lingkungan Kerja:
    * Terapkan inisiatif untuk meningkatkan kepuasan kerja serta ciptakan atmosfer kerja yang lebih positif dan mendukung, agar karyawan merasa lebih dihargai dan termotivasi untuk bertahan di perusahaan.
3. Strategi Retensi di Departemen Penting:
    * Prioritaskan program retensi di departemen dan posisi yang memiliki tingkat attrition tinggi, seperti Sales. Strategi ini bisa meliputi pemberian insentif, pengakuan atas kontribusi karyawan, serta pengembangan jalur karier yang lebih terstruktur.
4. Pemantauan dan Respons Berkala:
    * Gunakan dashboard secara aktif untuk memantau dinamika yang memengaruhi attrition, serta ambil tindakan segera jika terdapat indikasi permasalahan agar dapat ditangani sebelum berkembang lebih jauh.

Melalui langkah-langkah ini, perusahaan diharapkan dapat mengurangi tingkat attrition, memperkuat retensi tenaga kerja, dan meningkatkan efektivitas serta keberlanjutan operasional.


