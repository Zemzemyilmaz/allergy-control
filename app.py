import streamlit as st

ALLERGENS = 
ALLERGENS = {
    "tr": {
        "Gluten": ["buğday", "arpa", "çavdar", "yulaf", "gluten"],
        "Süt": ["süt", "peynir", "yoğurt", "tereyağı", "krema", "laktoz"],
        "Yumurta": ["yumurta", "yumurta akı", "yumurta sarısı"],
        "Fındık/Ceviz": ["fındık", "badem", "ceviz", "kaju", "antep fıstığı"],
        "Soya": ["soya", "soya sütü", "soya unu", "lesitin"],
        "Balık/Deniz Ürünleri": ["balık", "karides", "yengeç", "istakoz", "midye", "kalamar"],
        "Yer Fıstığı": ["yer fıstığı", "fıstık yağı"],
        "Kereviz": ["kereviz", "kereviz tohumu"],
        "Hardal": ["hardal", "hardal tohumu"],
        "Susam": ["susam", "tahin"],
        "Kükürt/Sülfit": ["kükürt", "sülfit"],
        "Acı Bakla": ["acı bakla", "lupin"]
    },
    "en": {
        "Gluten": ["wheat", "barley", "rye", "oat", "gluten"],
        "Milk": ["milk", "cheese", "yogurt", "butter", "cream", "lactose"],
        "Egg": ["egg", "egg white", "egg yolk"],
        "Nuts": ["hazelnut", "almond", "walnut", "cashew", "pistachio"],
        "Soy": ["soy", "soya milk", "soy flour", "lecithin"],
        "Fish/Seafood": ["fish", "shrimp", "crab", "lobster", "mussel", "squid"],
        "Peanut": ["peanut", "peanut oil"],
        "Celery": ["celery", "celery seed"],
        "Mustard": ["mustard", "mustard seed"],
        "Sesame": ["sesame", "tahini"],
        "Sulfites": ["sulfur", "sulfite"],
        "Lupin": ["lupin"]
    },
    # Buraya aynı mantıkla "fi" (Fince), "ru" (Rusça), "sv" (İsveççe), "ar" (Arapça), "uk" (Ukraynaca) ekleyebilirsin
}

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