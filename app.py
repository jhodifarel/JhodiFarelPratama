import streamlit as st
from streamlit_option_menu import option_menu

# =========================
# Konfigurasi Halaman
# =========================
st.set_page_config(
    page_title="Website Pribadi Mahasiswa",
    page_icon="🎓",
    layout="wide"
)

# =========================
# Custom CSS
# =========================
st.markdown("""
<style>

/* Background utama */
.stApp{
    background: linear-gradient(135deg,#eef2f3,#d9e4f5);
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background: linear-gradient(180deg,#1e3c72,#2a5298);
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* Judul */
h1{
    color:#1f3b73;
    font-weight:800;
    text-align:center;
    letter-spacing:1px;
}

h2,h3{
    color:#244b8f;
    font-weight:bold;
}

/* Card */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

div[data-testid="stVerticalBlock"]{
    border-radius:18px;
}

/* Kotak informasi */
[data-testid="stMarkdownContainer"]{
    font-size:16px;
}

/* Success */
div[data-testid="stAlert"]{
    border-radius:15px;
}

/* Image */
img{
    border-radius:15px;
    box-shadow:0 8px 20px rgba(0,0,0,0.2);
}

/* Tombol */
.stButton>button{
    background:#1f3b73;
    color:white;
    border:none;
    border-radius:12px;
    padding:10px 25px;
    transition:0.3s;
}

.stButton>button:hover{
    background:#315fb3;
    transform:scale(1.03);
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"]{
    border-radius:10px;
}

/* Caption */
.css-1kyxreq{
    text-align:center;
}

/* Garis */
hr{
    border:1px solid #b7c7e3;
}

/* Card efek */
.element-container{
    background:white;
    padding:15px;
    border-radius:15px;
    margin-bottom:15px;
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# =========================
# Sidebar Menu
# =========================
selected = option_menu(
    menu_title=None,
    options=[
        "Home",
        "Profil",
        "Music Favorit",
        "Film Favorit",
        "Portofolio",
        "Kontak"
    ],
    icons=[
        "house-fill",
        "person-fill",
        "music-note-beamed",
        "film",
        "briefcase-fill",
        "telephone-fill"
    ],
    orientation="horizontal",
    default_index=0,
)

# =========================
# HOME
# =========================
if selected == "Home":

    st.title("🏠 HOME")

    st.subheader("Identitas Mahasiswa")

    st.write("**NIM :** 23111017")
    st.write("**Nama :** Jhodi Farel Pratama")
    st.write("**Semester :** 6")
    st.write("**Program Studi :** Sistem Informasi")

    st.markdown("---")

    st.subheader("💡 Motto Hidup")

    st.success(
        "Terus belajar, terus berkembang, dan jangan pernah menyerah sebelum berhasil."
    )

# =========================
# PROFIL
# =========================
elif selected == "Profil":

    st.title("👤 Profil Mahasiswa")

    col1, col2 = st.columns([1,2])

    with col1:
        st.image("foto_profil.jpg.jpeg", width=250)

    with col2:
        st.subheader("Biodata")

        st.write("**Nama :** Jhodi Farel Pratama")

        st.write("### Hobi")
        st.write("- Bermain Teater")
        st.write("- Bermain Musik")
        st.write("- Melukis")

        st.write("### Minat")
        st.write("- Kesenian")
        st.write("- Web Development")
        st.write("- Artificial Intelligence")

        st.write("### Kemampuan Diri")
        st.write("- Bermain seni")
        st.write("- office")

# =========================
# MUSIC FAVORIT
# =========================
elif selected == "Music Favorit":

    st.title("🎵 Playlist Music Favorit")

    playlist = {
        "Selamat Tinggal - Virgoun":
            "https://youtu.be/nnZpgbJQVXw?si=khyLCdmeu0nbbehD",

        "Raim Lode - Komang":
            "https://youtu.be/fKRtnMYMW08?si=f0DezVYpQVq7ovCa",

        "Someone Like You - Adele":
            "https://youtu.be/z7GCiVTlv04?si=hgEe4mmGyuw8L1HC",

        "Until I Found You - Stephen Sanchez":
            "https://youtu.be/GhQxrCrVSyw?si=ft4iPcFvjYgzt1x0",

        "Blue Jeans - Gangga":
            "https://youtu.be/UzKdy75GqXQ?si=8cTVsPNwP1OeRDCm"
    }

    pilihan = st.selectbox("🎧 Pilih Lagu", list(playlist.keys()))

    st.video(playlist[pilihan])

# =========================
# FILM FAVORIT
# =========================
elif selected == "Film Favorit":

    st.title("🎬 Film Favorit")

    films = [
    {
        "judul": "Agak Laen",
        "gambar": "film 1.jpg",
        "sinopsis": "Film horor komedi Agak Laen menceritakan empat sekawan...",
        "genre": "Horor Komedi",
        "rating": "⭐⭐⭐⭐ 9.5/10",
        "trailer": "https://youtu.be/0YLSPyGA4h0?si=SKRkMLKTHAfgwpjh"
    },
    {
        "judul": "KKN Didesa Penari",
        "gambar": "film 2.jpg",
        "sinopsis": "Film KKN di Desa Penari menceritakan enam mahasiswa...",
        "genre": "Horor, Drama, Misteri",
        "rating": "⭐⭐⭐⭐ 9.5/10",
        "trailer": "https://youtu.be/01BPk6M37qs?si=mm14fzQD6Lirn-Ur"
    },
    {
        "judul": "Sekawan Limo",
        "gambar": "film 3.png",
        "sinopsis": "Sekawan Limo adalah film horor komedi Indonesia...",
        "genre": "Horor Komedi",
        "rating": "⭐⭐⭐⭐ 9.5/10",
        "trailer": "https://youtu.be/ERZncVUuKlk?si=Mr9BBHYS37wN5IHs"
    },
    {
        "judul": "Dusun Mayit",
        "gambar": "film 4.jpg",
        "sinopsis": "Film Dusun Mayit menceritakan tentang empat mahasiswa...",
        "genre": "Horor, Adventure, Misteri",
        "rating": "⭐⭐⭐⭐ 9.5/10",
        "trailer": "https://youtu.be/3EK7e9pU6r8?si=DpjNQavBwI4d8OtU"
    }
]

    cols = st.columns(4)

    for i, film in enumerate(films):

        with cols[i]:

            st.image(film["gambar"], use_container_width=True)

            st.subheader(film["judul"])

            tab1, tab2, tab3, tab4 = st.tabs(
                ["📖 Sinopsis", "🎭 Genre", "⭐ Rating", "▶ Trailer"]
            )

            with tab1:
                st.write(film["sinopsis"])

            with tab2:
                st.write(film["genre"])

            with tab3:
                st.write(film["rating"])

            with tab4:
                st.video(film["trailer"])
# =========================
# PORTOFOLIO
# =========================
elif selected == "Portofolio":

    st.title("💼 Portofolio")

    st.subheader("Karya Selama Menjadi Mahasiswa")

    st.write("### Project 1")
    st.image("karya1.jpeg")

    st.write("Penghargaan terhadap pimpinan produksi event PLASTIK (Pagelaran Seni Kreasistik)")

    st.markdown("---")

    st.write("### Project 2")
    st.image("karya2.jpeg")

    st.write("Pemberian penghargaan dari cafe eleu")

    st.markdown("---")

    st.write("### Project 3")
    st.image("karya3.jpeg")

    st.write("Penampilan Teater Berjudul Dull muluk")

    st.markdown("---")

    st.write("### Project 4")
    st.image("karya4.jpeg")

    st.write("Pemberian penghargaan sebagai duta moderasi beragama di UNH")

    st.markdown("---")

    st.write("### Project 5")
    st.image("karya5.jpeg")

    st.write("Penampilan Teater Berjudul Habis Sudah")

    st.markdown("---")

   

# =========================
# KONTAK
# =========================
elif selected == "Kontak":

    st.title("📞 Kontak")

    st.subheader("📧 Email")
    st.markdown("[JhodiFarel03@gmail.com](mailto:jhodi@example.com)")

    st.subheader("🌐 Sosial Media")

    st.markdown("📷 **Instagram** : [@jhodifarel](https://www.instagram.com/jhodifarel)")
    st.markdown("👍 **Facebook** : [Jhodi Farel](https://www.facebook.com/jhodifarel)")
    st.markdown("💼 **LinkedIn** : [Jhodi Farel](https://www.linkedin.com/in/jhodifarel)")
    st.markdown("▶ **YouTube** : [Jhodi Farel](https://www.youtube.com/@jhodifarel)")