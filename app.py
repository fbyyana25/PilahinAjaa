import streamlit as st

def main():
    st.title("Aplikasi Edukatif Pemilah dan Pengolahan Sampah")
    st.subheader("Pelajari cara memilah dan mengolah sampah organik dan anorganik dengan benar!")

    st.sidebar.header("Navigasi")
    page = st.sidebar.radio("Pilih Halaman:", ["Pengenalan Sampah", "Cara Memilah", "Pengolahan Organik", "Pengolahan Anorganik", "Kuis"])

    if page == "Pengenalan Sampah":
        tampilkan_pengenalan()
    elif page == "Cara Memilah":
        tampilkan_cara_memilah()
    elif page == "Pengolahan Organik":
        tampilkan_pengolahan_organik()
    elif page == "Pengolahan Anorganik":
        tampilkan_pengolahan_anorganik()
    elif page == "Kuis":
        tampilkan_kuis()

def tampilkan_pengenalan():
    st.header("Apa itu Sampah?")
    st.write("Sampah adalah sisa kegiatan sehari-hari manusia dan/atau proses alam yang berbentuk padat.")
    st.subheader("Jenis-jenis Sampah:")
    st.write("- *Sampah Organik:* Berasal dari makhluk hidup, mudah terurai (misalnya sisa makanan, daun kering).")
    st.write("- *Sampah Anorganik:* Tidak mudah terurai, berasal dari bahan non-hayati (misalnya plastik, logam, kaca).")

def tampilkan_cara_memilah():
    st.header("Cara Memilah Sampah yang Benar")
    st.write("Memilah sampah sangat penting untuk memudahkan proses pengolahan dan mengurangi dampak buruk terhadap lingkungan.")
    st.subheader("Langkah-langkah Memilah:")
    st.markdown("""
    1. Siapkan dua jenis wadah sampah: untuk organik dan anorganik.
    2. Pisahkan sampah basah (sisa makanan) dan sampah kering (daun kering) ke dalam wadah organik.
    3. Pisahkan sampah plastik, kertas, logam, dan kaca ke dalam wadah anorganik.
    4. Pastikan wadah sampah diberi label yang jelas.
    5. Buang sampah sesuai jadwal dan tempat yang ditentukan.
    """)
    st.image("contoh_pemilahan_sampah.jpg", caption="Contoh Pemilahan Sampah di Rumah", use_column_width=True) # Ganti dengan path gambar Anda

def tampilkan_pengolahan_organik():
    st.header("Pengolahan Sampah Organik")
    st.write("Sampah organik dapat diolah menjadi kompos yang berguna untuk menyuburkan tanaman.")
    st.subheader("Metode Pengomposan Sederhana:")
    st.markdown("""
    1. Siapkan wadah atau lubang komposter.
    2. Masukkan sampah organik seperti sisa makanan, daun kering, dan rumput ke dalam komposter.
    3. Tambahkan sedikit air untuk menjaga kelembaban.
    4. Aduk secara berkala untuk mempercepat proses penguraian.
    5. Kompos siap digunakan setelah beberapa minggu/bulan, ditandai dengan warna hitam dan tekstur remah.
    """)
    st.image("contoh_komposter.jpg", caption="Contoh Komposter Sederhana", use_column_width=True) # Ganti dengan path gambar Anda

def tampilkan_pengolahan_anorganik():
    st.header("Pengolahan Sampah Anorganik")
    st.write("Sampah anorganik seperti plastik, logam, dan kaca dapat didaur ulang menjadi barang yang berguna.")
    st.subheader("Contoh Proses Daur Ulang:")
    st.write("- *Plastik:* Dilebur dan dibentuk menjadi produk baru seperti botol, ember, atau bijih plastik.")
    st.write("- *Logam:* Dilebur dan dicetak kembali menjadi berbagai produk logam.")
    st.write("- *Kertas:* Diproses menjadi kertas daur ulang.")
    st.image("contoh_daur_ulang.jpg", caption="Contoh Produk Daur Ulang", use_column_width=True) # Ganti dengan path gambar Anda

def tampilkan_kuis():
    st.header("Kuis Pengetahuan Sampah")
    st.write("Uji pengetahuanmu tentang pemilahan dan pengolahan sampah!")

    pertanyaan = [
        {"pertanyaan": "Sisa makanan termasuk jenis sampah...", "jawaban": "Organik", "pilihan": ["Organik", "Anorganik"]},
        {"pertanyaan": "Plastik sebaiknya dibuang ke wadah...", "jawaban": "Anorganik", "pilihan": ["Organik", "Anorganik"]},
        {"pertanyaan": "Proses penguraian sampah organik menjadi pupuk disebut...", "jawaban": "Pengomposan", "pilihan": ["Pembakaran", "Pengomposan", "Penimbunan"]},
        {"pertanyaan": "Botol kaca dapat diolah melalui proses...", "jawaban": "Daur Ulang", "pilihan": ["Pembakaran", "Daur Ulang", "Penimbunan"]},
    ]

    skor = 0
    for i, soal in enumerate(pertanyaan):
        st.subheader(f"Pertanyaan {i+1}:")
        jawaban_user = st.radio(soal["pertanyaan"], soal["pilihan"])
        if jawaban_user == soal["jawaban"]:
            skor += 1

    st.write(f"Skor Anda: {skor} dari {len(pertanyaan)}")
    if skor == len(pertanyaan):
        st.success("Selamat! Pengetahuanmu tentang sampah sangat baik!")
    else:
        st.warning("Tingkatkan lagi pengetahuanmu tentang pemilahan dan pengolahan sampah!")

if _name_ == "_main_":
    main()
        
