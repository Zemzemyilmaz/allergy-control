import streamlit as st
import streamlit as st

ALLERGENS = {
    "tr": {
        "Gluten": ["buğday", "arpa", "çavdar", "yulaf", "gluten"],
        "Süt": ["süt", "peynir", "yoğurt", "tereyağı", "krema", "laktoz"]
    },
    "en": {
        "Gluten": ["wheat", "barley", "rye", "oat", "gluten"],
        "Milk": ["milk", "cheese", "yogurt", "butter", "cream", "lactose"]
    }
}

# Bundan sonra st.set_page_config satırın gelsin...
st.set_page_config(page_title="Alerjen Asistanı", page_icon="🛡️")
    # Buraya aynı mantıkla "fi" (Fince), "ru" (Rusça), "sv" (İsveççe), "ar" (Arapça), "uk" (Ukraynaca) ekleyebilirsin}

st.set_page_config(page_title="Alerjen Asistanı", page_icon="🛡️")
st.title("🛡️ Alerjen Güvenlik Asistanı")

lang = st.selectbox("Dil Seçin / Select Language", ["tr", "en", "fi", "ru", "sv", "ar", "uk"])
etiket = st.text_area("İçindekiler listesini buraya yapıştırın:")

if st.button("Analiz Et", key="analiz_butonu"):
    st.write("Analiz ediliyor...")
    for alerjen, diller in ALLERGENS.items():
        kelimeler = diller.get(lang, [])
        if any(k in etiket.lower() for k in kelimeler):
            st.error(f"⚠️ RİSK: Bu üründe {alerjen} tespit edildi!")
        else:
            st.success(f"✅ {alerjen} bulunamadı.")

kamera_foto = st.camera_input("Ürün etiketini çek")
st.warning("⚠️ ÖNEMLİ: Bu araç genel bilgi amaçlıdır. Çölyak ve bağırsak hassasiyeti gibi durumlarda mutlaka ürünün 'Glutensiz' sertifikasına bakın.")