import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pytesseract

# Alerjenlerin çok dilli sözlüğü
allergy_dictionary = {
    "gluten": ["gluteeni", "gluten"],
    "peanut": ["maapähkinä", "jordnöt"],
    "lactose": ["laktoosi", "laktos"],
    "milk": ["maito", "mjölk"],
    "egg": ["kananmuna", "ägg"]
}

# Kullanıcının seçtiği alerjiler (Varsayılan olarak ikisi seçili gelsin)
user_allergies = ["gluten", "lactose"]

def check_image_for_allergies(image_path):
    try:
        # Fotoğrafı aç ve Tesseract ile oku
        img = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(img, lang='fin+swe')
        ingredients_lower = extracted_text.lower()
        
        detected_allergens = []
        for allergen in user_allergies:
            if allergen in allergy_dictionary:
                for translation in allergy_dictionary[allergen]:
                    if translation in ingredients_lower:
                        if allergen not in detected_allergens:
                            detected_allergens.append(allergen)
        
        # Sonuçları ekrandaki yazı alanına basıyoruz
        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, f"📝 SCANNED TEXT:\n{extracted_text}\n" + "-"*40 + "\n")
        
        if detected_allergens:
            label_status.config(text=f"❌ NOT SAFE! ({', '.join(detected_allergens).upper()})", fg="red")
            messagebox.showwarning("Allergy Alert", f"Warning! Detected allergens: {', '.join(detected_allergens).upper()}")
        else:
            label_status.config(text="✅ SAFE TO EAT (TURVALLINEN)", fg="green")
            messagebox.showinfo("Safe", "No matching allergens found!")
            
    except Exception as e:
        messagebox.showerror("Error", f"Could not scan image: {e}")

def open_file_dialog():
    # Kullanıcının bilgisayardan fotoğraf seçmesini sağlayan pencere
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png")])
    if file_path:
        label_file.config(text=f"Selected: {file_path.split('/')[-1]}")
        
        # Seçilen resmi ekranda önizleme olarak gösterelim
        img = Image.open(file_path)
        img.thumbnail((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        panel_image.config(image=img_tk)
        panel_image.image = img_tk
        
        # Analizi başlat
        check_image_for_allergies(file_path)

# ---- ARAYÜZ (GUI) TASARIMI ----
root = tk.Tk()
root.title("Allergy Scanner App - Finland")
root.geometry("450x600")
root.config(bg="#f5f5f5")

# Başlık
label_title = tk.Label(root, text="🛡️ Allergy Label Scanner", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333")
label_title.pack(pady=15)

# Buton
btn_select = tk.Button(root, text="📸 Select Product Photo", font=("Arial", 12, "bold"), bg="#007aff", fg="black", padx=10, pady=5, command=open_file_dialog)
btn_select.pack(pady=10)

# Seçilen dosya adı
label_file = tk.Label(root, text="No file selected", font=("Arial", 10, "italic"), bg="#f5f5f5", fg="#666")
label_file.pack()

# Resim Önizleme Paneli
panel_image = tk.Label(root, bg="#f5f5f5")
panel_image.pack(pady=10)

# Güvenlik Durumu (Safe / Not Safe)
label_status = tk.Label(root, text="Waiting for scan...", font=("Arial", 14, "bold"), bg="#f5f5f5", fg="#555")
label_status.pack(pady=10)

# Okunan Yazıların Görüneceği Alan
text_result = tk.Text(root, height=12, width=50, font=("Arial", 10))
text_result.pack(pady=10, padx=15)

# Uygulamayı döngüye sokup ekranda tutuyoruz
root.mainloop()
