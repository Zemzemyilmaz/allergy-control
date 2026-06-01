import PIL.Image
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

# Dil seçeneklerini genişletiyoruz
diller = ["tr", "en", "fi", "ru", "sv", "ar", "uk"]
lang = st.selectbox("Dil Seçin / Select Language / Valitse kieli", diller)

if st.button("Analiz Et", key="analiz_butonu"):
    st.write("Analiz ediliyor...")
    for alerjen, diller in ALLERGENS.items():
        kelimeler = diller.get(lang, [])
        if any(k in etiket.lower() for k in kelimeler):
            st.error(f"⚠️ RİSK: Bu üründe {alerjen} tespit edildi!")
        else:
            st.success(f"✅ {alerjen} bulunamadı.")

kamera_foto = st.camera_input("Ürün etiketini çek")
if kamera_foto is not None:
    # Fotoğrafı al ve görüntü nesnesine çevir
    img = PIL.Image.open(kamera_foto)
    st.image(img, caption="Etiket görüntüsü alındı", use_column_width=True)
    st.write("📸 Görüntü başarıyla işlendi! Şimdi analiz butonuna basabilirsin.")

st.warning("⚠️ ÖNEMLİ: Bu araç genel bilgi amaçlıdır. Çölyak ve bağırsak hassasiyeti gibi durumlarda mutlaka ürünün 'Glutensiz' sertifikasına bakın.")
import google.generativeai as genai

# Google API anahtarını kasadan (Secrets) çekiyoruz
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

def analyze_label(image, language):
    model = genai.GenerativeModel('gemini-1.5-flash')
    # Yapay zekaya annenin sağlığı için net bir talimat veriyoruz
    prompt = f"Bu etiketi {language} dilinde analiz et. İçindekiler listesinde gluten, süt, yumurta gibi riskli alerjenler varsa RİSKLİ de, yoksa GÜVENLİ de. Sadece sonucu söyle."
    response = model.generate_content([prompt, image])
    return response.text

# AI Analiz Butonu
if st.button("AI ile Analiz Et"):
    if kamera_foto:
        with st.spinner("🧠 Yapay zeka etiketi okuyor..."):
            analysis = analyze_label(img, lang)
            st.write(f"### Analiz Sonucu:")
            st.write(analysis)
    else:
        st.warning("Lütfen önce bir fotoğraf çek!")